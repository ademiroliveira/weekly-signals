#!/usr/bin/env python3
"""Tooling for the signals archive. Standard library only.

  python3 scripts/signals.py prior    [--today YYYY-MM-DD] [--dir signals]
  python3 scripts/signals.py validate signals/YYYY-MM-DD.md [--dir signals]
  python3 scripts/signals.py render   --out PATH [--dir signals ...]

prior     prints the report window, the previous report and every URL already
          covered (the "seen" list) as JSON.
validate  checks a report's frontmatter and structure against CLAUDE.md. Exit 1
          on errors. Reports generated before CUTOVER are checked leniently
          (new rules become warnings).
render    builds the artifact page (all weeks, newest first) from the markdown.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
CUTOVER = "2026-10-13"  # reports generated on/after this date follow the current rules
MAX_WINDOW_DAYS = 7
REPO_SIGNALS_URL = "https://github.com/ademiroliveira/weekly-signals/tree/main/signals"

TAGS = [
    "[IACR paper]", "[arXiv paper]", "[Usable security paper]", "[EIP]", "[W3C spec]",
    "[NIST pub]", "[BIS paper]", "[FSB report]", "[FATF guidance]", "[Regulatory filing]",
    "[Institutional report]", "[Audit]", "[Vendor security report]", "[GitHub release]",
    "[Protocol blog]", "[Verified journalism]",
]
SECTIONS = {"top", "ux", "radar"}
LEGACY_SECTIONS = {"weak": "radar"}
STRENGTHS = {"strong", "emerging", "weak"}
STAGES = {"early", "formal", "in-force"}
ORIGINS = {"academic", "standards", "regulatory", "institutional", "technical", "journalism"}
DOMAINS = {"key-mgmt", "recovery", "identity", "hardware", "threat", "post-quantum",
           "regulation", "sovereign-adoption", "agentic", "ux"}
LEGACY_DOMAINS = {"narrative"}
# Strength allowed per stage (CLAUDE.md rubric). Journalism caps are checked separately.
STAGE_STRENGTH = {"early": {"weak", "emerging"}, "formal": {"emerging", "strong"}, "in-force": {"strong", "emerging"}}
REQUIRED_H2 = ["Top 3 Signals", "UX & Interaction Signals", "On the radar", "Pulses",
               "Patterns across weeks", "Source Audit"]
# sha256 of lower-cased internal names that must never appear in this public repo.
FORBIDDEN_HASHES = {"01735c5ff1608734e4c38449a00b74bb9a8d5423ed548238da70178e9e803483"}
SKIP_RENDER_H2 = re.compile(r"^por" r"to\b", re.I)  # retired internal section in older reports

DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
WEEK_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})\.\.(\d{4}-\d{2}-\d{2})$")


# ---------------------------------------------------------------- parsing

def _split_list(inner: str) -> list[str]:
    out, buf, quote = [], "", None
    for ch in inner:
        if quote:
            buf += ch
            if ch == quote:
                quote = None
        elif ch in "\"'":
            quote = ch
            buf += ch
        elif ch == ",":
            out.append(buf)
            buf = ""
        else:
            buf += ch
    if buf.strip():
        out.append(buf)
    return out


def parse_scalar(raw: str):
    v = raw.strip()
    if not v:
        return None
    if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
        return v[1:-1].replace('\\"', '"')
    if len(v) >= 2 and v[0] == "'" and v[-1] == "'":
        return v[1:-1]
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        return [parse_scalar(x) for x in _split_list(inner)] if inner else []
    if " #" in v:
        v = v.split(" #", 1)[0].rstrip()
    return v or None


def split_report(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("unterminated frontmatter")
    fm_text, body = text[4:end], text[end + 5:]
    fm: dict = {}
    items: list[dict] = []
    cur = None
    in_items = False
    for line in fm_text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if not line.startswith(" "):
            key, _, val = line.partition(":")
            key = key.strip()
            if key == "items":
                in_items = True
                fm["items"] = items
                continue
            in_items = False
            fm[key] = parse_scalar(val)
        elif in_items:
            s = line.strip()
            if s.startswith("- "):
                cur = {}
                items.append(cur)
                s = s[2:]
            if cur is None:
                raise ValueError(f"item field outside an item: {line!r}")
            key, _, val = s.partition(":")
            cur[key.strip()] = parse_scalar(val)
    fm.setdefault("items", items)
    return fm, body


def load_reports(dirs: list[pathlib.Path]) -> list[dict]:
    seen_names, reports = set(), []
    for d in dirs:
        for p in sorted(d.glob("*.md")):
            if not DATE_RE.match(p.stem) or p.name in seen_names:
                continue
            seen_names.add(p.name)
            fm, body = split_report(p.read_text(encoding="utf-8"))
            m = WEEK_RE.match(str(fm.get("week") or ""))
            reports.append({
                "path": p, "name": p.stem, "fm": fm, "body": body,
                "start": m.group(1) if m else None, "end": m.group(2) if m else p.stem,
            })
    reports.sort(key=lambda r: r["name"])
    return reports


def load_ux_patterns() -> tuple[set[str], list[tuple[str, str]]]:
    path = ROOT / "reference" / "ux-patterns.md"
    slugs, legacy = set(), []
    if not path.exists():
        return slugs, legacy
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2 or not line.lstrip().startswith("|"):
            continue
        if re.fullmatch(r"`[a-z0-9-]+`", cells[0]):
            slugs.add(cells[0].strip("`"))
        elif re.fullmatch(r"`[a-z0-9-]+`", cells[1]) and not cells[0].startswith("-"):
            legacy.append((cells[0].lower(), cells[1].strip("`")))
    return slugs, legacy


def map_pattern(value: str | None, slugs: set[str], legacy: list[tuple[str, str]]) -> str | None:
    if not value:
        return None
    v = value.strip().strip('"')
    if v in slugs:
        return v
    low = v.lower()
    for prefix, slug in legacy:
        if low.startswith(prefix):
            return slug
    return None


def d(s: str) -> dt.date:
    return dt.date.fromisoformat(s)


# ---------------------------------------------------------------- prior

def compute_prior(reports: list[dict], today: dt.date) -> dict:
    earlier = [r for r in reports if r["name"] < today.isoformat()]
    exists_today = any(r["name"] == today.isoformat() for r in reports)
    prev = earlier[-1] if earlier else None
    gap_days = 0
    if prev:
        start = d(prev["end"]) + dt.timedelta(days=1)
        floor = today - dt.timedelta(days=MAX_WINDOW_DAYS - 1)
        if start < floor:
            gap_days = (floor - start).days
            start = floor
    else:
        start = today - dt.timedelta(days=MAX_WINDOW_DAYS - 1)
    slugs, legacy = load_ux_patterns()
    seen, patterns = [], {}
    for r in earlier:
        for it in r["fm"].get("items", []):
            urls = [it.get("url")] + list(it.get("also") or [])
            for u in urls:
                if u:
                    seen.append({"id": it.get("id"), "url": u, "title": it.get("title"), "report": r["name"]})
            slug = map_pattern(it.get("ux_pattern"), slugs, legacy)
            if slug:
                patterns.setdefault(slug, []).append(it.get("id"))
    return {
        "today": today.isoformat(),
        "window": {"start": start.isoformat(), "end": today.isoformat(),
                   "days": (today - start).days + 1, "empty": start > today},
        "previous_report": {"file": f"signals/{prev['name']}.md", "week": prev["fm"].get("week")} if prev else None,
        "gap_days": gap_days,
        "report_exists_for_today": exists_today,
        "seen": seen,
        "ux_patterns_seen": patterns,
    }


# ---------------------------------------------------------------- validate

def forbidden_words(text: str) -> set[str]:
    hits = set()
    for w in set(re.findall(r"[A-Za-z]+", text)):
        if hashlib.sha256(w.lower().encode()).hexdigest() in FORBIDDEN_HASHES:
            hits.add(w)
    return hits


def validate(path: pathlib.Path, reports: list[dict]) -> tuple[list[str], list[str]]:
    errors, warnings = [], []
    try:
        fm, body = split_report(path.read_text(encoding="utf-8"))
    except ValueError as e:
        return [f"frontmatter: {e}"], []
    name = path.stem
    strict = name >= CUTOVER
    soft = errors if strict else warnings

    def need(cond, msg, hard=True):
        if not cond:
            (errors if hard else soft).append(msg)

    need(DATE_RE.match(name) is not None, "file name must be YYYY-MM-DD.md")
    need(fm.get("report") == "self-custody-sovereignty", "report: must be self-custody-sovereignty")
    need(fm.get("generated") == name, f"generated: must equal the file date ({name})")
    for k in ("verified", "killed"):
        need(str(fm.get(k, "")).isdigit(), f"{k}: must be a whole number")
    m = WEEK_RE.match(str(fm.get("week") or ""))
    need(m is not None, "week: must be YYYY-MM-DD..YYYY-MM-DD")
    w_start, w_end = (m.group(1), m.group(2)) if m else (None, None)
    if m:
        need(w_end == name, f"week: must end on the run date {name}", hard=False)
        expected = compute_prior([r for r in reports if r["name"] < name], d(name))["window"]
        need(w_start == expected["start"],
             f"week: should start {expected['start']} (day after the previous report's window), found {w_start}",
             hard=False)

    prior = compute_prior([r for r in reports if r["name"] < name], d(name)) if DATE_RE.match(name) else {"seen": []}
    seen_urls: dict = {}
    for s in prior["seen"]:
        seen_urls.setdefault(s["url"], s)
    seen_ids = {s["id"] for s in prior["seen"]}
    slugs, legacy = load_ux_patterns()

    items = fm.get("items") or []
    need(len(items) > 0, "items: empty (a quiet week still lists what it includes; use 'No new signals' in the body only)", hard=False)
    ids, url_sections = set(), {}
    tops = 0
    for i, it in enumerate(items, 1):
        label = f"item {i} ({it.get('id') or it.get('title') or '?'})"
        for k in ("id", "title", "section", "strength", "origin", "domains", "source_type", "url", "published"):
            need(it.get(k) not in (None, "", []), f"{label}: missing {k}")
        need("stage" in it or not strict, f"{label}: missing stage")
        iid = it.get("id") or ""
        need(iid.startswith(name + "-"), f"{label}: id must start with {name}-", hard=False)
        need(iid not in ids, f"{label}: duplicate id")
        ids.add(iid)
        sec = it.get("section")
        if sec in LEGACY_SECTIONS:
            if strict:
                errors.append(f"{label}: section '{sec}' is legacy, use '{LEGACY_SECTIONS[sec]}'")
            sec = LEGACY_SECTIONS[sec]
        need(sec in SECTIONS, f"{label}: section must be one of {sorted(SECTIONS)}")
        tops += sec == "top"
        st = it.get("strength")
        need(st in STRENGTHS, f"{label}: strength must be one of {sorted(STRENGTHS)}")
        stage = it.get("stage")
        if stage is not None:
            need(stage in STAGES, f"{label}: stage must be one of {sorted(STAGES)}")
            if stage in STAGE_STRENGTH and st in STRENGTHS:
                need(st in STAGE_STRENGTH[stage], f"{label}: strength '{st}' doesn't fit stage '{stage}' (see rubric)")
        need(it.get("origin") in ORIGINS, f"{label}: origin '{it.get('origin')}' not in {sorted(ORIGINS)}", hard=False)
        doms = it.get("domains") or []
        if not isinstance(doms, list):
            errors.append(f"{label}: domains must be a [list]")
            doms = []
        bad = [x for x in doms if x not in DOMAINS]
        need(not [x for x in bad if x not in LEGACY_DOMAINS], f"{label}: unknown domains {bad}", hard=False)
        tag = it.get("source_type")
        if isinstance(tag, list):
            errors.append(f'{label}: quote the tag, e.g. source_type: "[Protocol blog]"')
        else:
            need(tag in TAGS, f"{label}: source_type {tag!r} is not an approved tag")
        also = it.get("also") or []
        if tag == "[Verified journalism]" and not also and st in STRENGTHS:
            need(st == "weak", f"{label}: a single journalism article is capped at weak", hard=False)
        pub = it.get("published")
        if pub and w_start and DATE_RE.match(str(pub)):
            need(w_start <= pub <= w_end, f"{label}: published {pub} is outside the window {w_start}..{w_end}")
        elif pub:
            errors.append(f"{label}: published must be YYYY-MM-DD")
        url = it.get("url")
        if url in seen_urls:
            s = seen_urls[url]
            need(False, f"{label}: URL already covered in {s['report']} ({s['id']})", hard=False)
        upd = it.get("update_of")
        if upd:
            need(upd in seen_ids, f"{label}: update_of '{upd}' is not an id from an earlier report")
            need(str(it.get("title", "")).startswith("Update:"), f"{label}: Updates must be titled 'Update: …'", hard=False)
        if url:
            url_sections.setdefault(url, []).append(sec)
        if sec == "ux":
            pat = it.get("ux_pattern")
            if strict:
                need(pat in slugs, f"{label}: ux_pattern '{pat}' is not a slug in reference/ux-patterns.md")
            else:
                need(map_pattern(pat, slugs, legacy) is not None,
                     f"{label}: ux_pattern '{pat}' doesn't map to reference/ux-patterns.md", hard=False)
    need(tops <= 3, f"{tops} items in section top (max 3; merge corroborating sources into also:)", hard=False)
    for url, secs in url_sections.items():
        if len(secs) > 1:
            msg = f"same URL used by {len(secs)} items ({', '.join(secs)}): {url}"
            if "ux" in secs:
                soft.append(msg + " (a UX item needs its own source)")
            else:
                warnings.append(msg + " (fine only if the items are unrelated stories)")

    h2 = [h.strip() for h in re.findall(r"^## (.+)$", body, re.M)]
    for req in REQUIRED_H2 if strict else []:
        need(any(h.startswith(req) for h in h2), f"body: missing section '## {req}'", hard=False)
    hits = forbidden_words(path.read_text(encoding="utf-8"))
    need(not hits, f"contains an internal name that must not be published: {sorted(hits)}", hard=False)
    return errors, warnings


# ---------------------------------------------------------------- render

EMOJI = {"🔴": "Strong", "🟠": "Emerging", "🟡": "Weak"}
TAG_RE = re.compile("|".join(re.escape(html.escape(t)) for t in TAGS))
MD_LINK_RE = re.compile(r"\[([^\]\n]+)\]\((https?://[^)\s]+)\)")
URL_RE = re.compile(r"https?://[^\s<>()]+")


def short_url(u: str) -> str:
    s = re.sub(r"^https?://(www\.)?", "", u).rstrip("/")
    return s if len(s) <= 64 else s[:61] + "…"


def inline(text: str) -> str:
    ph: list[str] = []

    def keep(s: str) -> str:
        ph.append(s)
        return f"\x00{len(ph) - 1}\x00"

    t = html.escape(text, quote=False)
    t = MD_LINK_RE.sub(lambda m: keep(f'<a href="{html.escape(m[2])}" target="_blank" rel="noopener">{m[1]}</a>'), t)

    def bare(m):
        u = m[0]
        trail = ""
        while u and u[-1] in ".,;:":
            trail = u[-1] + trail
            u = u[:-1]
        return keep(f'<a href="{html.escape(u)}" target="_blank" rel="noopener">{html.escape(short_url(u))}</a>') + trail

    t = URL_RE.sub(bare, t)
    t = re.sub(r"`([^`\n]+)`", lambda m: keep(f"<code>{m[1]}</code>"), t)
    t = TAG_RE.sub(lambda m: keep(f'<span class="tag">{m[0]}</span>'), t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*([^*\n]+)\*(?![\w*])", r"<em>\1</em>", t)
    t = re.sub(r"(🔴|🟠|🟡)", r'<span class="dot">\1</span>', t)
    return re.sub(r"\x00(\d+)\x00", lambda m: ph[int(m[1])], t)


def meta_line(text: str) -> str:
    m = re.match(r"^(🔴|🟠|🟡)\s*(Strong|Emerging|Weak)?\s*[·|]?\s*(.*)$", text)
    emoji, word, rest = m.group(1), m.group(2) or EMOJI[m.group(1)], m.group(3)
    parts = [p.strip() for p in re.split(r"\s+[·|]\s+", rest) if p.strip()]
    chips = "".join(f'<span class="chip">{inline(p)}</span>' for p in parts)
    return f'<p class="meta"><span class="badge">{emoji} {word}</span>{chips}</p>'


def blocks(md: str) -> list[tuple[str, object]]:
    out: list[tuple[str, object]] = []
    lines = md.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        if not s:
            i += 1
            continue
        if s.startswith("#"):
            level = len(s) - len(s.lstrip("#"))
            out.append((f"h{min(level, 4)}", s[level:].strip()))
        elif re.fullmatch(r"-{3,}", s):
            pass
        elif s.startswith(">"):
            quote = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip()[1:].strip())
                i += 1
            out.append(("quote", " ".join(quote)))
            continue
        elif re.match(r"^(- |\* |\d+\. )", s):
            ordered = bool(re.match(r"^\d+\. ", s))
            items: list[str] = []
            while i < len(lines):
                t = lines[i].strip()
                if re.match(r"^(- |\* |\d+\. )", t):
                    items.append(re.sub(r"^(- |\* |\d+\. )", "", t))
                elif t and items and lines[i].startswith(("  ", "\t")):
                    items[-1] += " " + t
                elif not t:
                    j = i + 1
                    while j < len(lines) and not lines[j].strip():
                        j += 1
                    if j < len(lines) and re.match(r"^(- |\* |\d+\. )", lines[j].strip()):
                        i = j
                        continue
                    break
                else:
                    break
                i += 1
            out.append(("ol" if ordered else "ul", items))
            continue
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not re.match(r"^(#|>|- |\* |\d+\. |-{3,}$)", lines[i].strip()):
                para.append(lines[i].strip())
                i += 1
            out.append(("p", para))
            continue
        i += 1
    return out


def render_blocks(bl) -> str:
    h = []
    for kind, val in bl:
        if kind == "p":
            if val and val[0][:1] in EMOJI and len(val) == 1:
                h.append(meta_line(val[0]))
            else:
                h.append("<p>" + "<br>".join(inline(x) for x in val) + "</p>")
        elif kind in ("ul", "ol"):
            h.append(f"<{kind}>" + "".join(f"<li>{inline(x)}</li>" for x in val) + f"</{kind}>")
        elif kind == "quote":
            h.append(f'<p class="note">{inline(val)}</p>')
        elif kind == "h4":
            h.append(f"<h4>{inline(val)}</h4>")
    return "\n".join(h)


def fmt_range(week: str | None, fallback: str) -> str:
    m = WEEK_RE.match(week or "")
    if not m:
        return fallback
    a, b = d(m.group(1)), d(m.group(2))
    if a.year != b.year:
        return f"{a:%b} {a.day}, {a.year} – {b:%b} {b.day}, {b.year}"
    if a.month != b.month:
        return f"{a:%b} {a.day} – {b:%b} {b.day}, {b.year}"
    return f"{a:%b} {a.day} – {b.day}, {b.year}"


def render_week(r: dict, active: bool) -> str:
    fm = r["fm"]
    bl = blocks(r["body"])
    sections: list[tuple[str, list]] = []
    for kind, val in bl:
        if kind == "h1":
            continue
        if kind == "h2":
            sections.append((val, []))
        elif sections:
            sections[-1][1].append((kind, val))
        else:
            sections.append(("", [(kind, val)]))
    rng = fmt_range(fm.get("week"), r["name"])
    stats = f"{fm.get('verified', '?')} verified · {fm.get('killed', '?')} killed · generated {fm.get('generated', r['name'])}"
    out = [f'<section class="week" id="w{r["name"]}" data-range="{html.escape(rng)}"{"" if active else " hidden"}>',
           f'<div class="week-head"><h1>Week of {html.escape(rng)}</h1><p class="stats">{stats}</p></div>']
    for title, content in sections:
        if title and SKIP_RENDER_H2.match(title):
            continue
        low = title.lower()
        if title:
            label = "On the radar" if low.startswith("weak signals") else title
            out.append(f'<h2 class="label">{inline(label)}</h2>')
        if low.startswith("source audit"):
            kill = re.search(r"Kill count:\s*\**(\d+)", "\n".join(str(v) for _, v in content))
            summ = f"Source audit · {kill.group(1)} killed" if kill else "Source audit"
            out.append(f'<details class="card audit"><summary>{summ}</summary>{render_blocks(content)}</details>')
            continue
        cards, loose = [], []
        for kind, val in content:
            if kind == "h3":
                cards.append([val, []])
            elif cards:
                cards[-1][1].append((kind, val))
            else:
                loose.append((kind, val))
        cls = "card patterns" if low.startswith("patterns") else "card"
        if loose:
            out.append(f'<div class="{cls}">{render_blocks(loose)}</div>')
        for h3, body in cards:
            title_txt = re.sub(r"^\d+\.\s*", "", h3)
            out.append(f'<article class="{cls}"><h3>{inline(title_txt)}</h3>{render_blocks(body)}</article>')
    out.append("</section>")
    return "\n".join(out)


CSS = """
:root {
  /* Layout: one 720px reading column under a sticky bar; week chips switch the column's content. */
  --base: #0e0e0e; --surface: #1c1c1c; --line: #2a2a2a; --accent: #F7931A;
  --text: #e8e8e8; --muted: #8f8f8f; --link: #aaaaaa; --faint: #5c5c5c; --white: #ffffff;
  --sans: 'Inter', system-ui, -apple-system, sans-serif;
  --mono: 'JetBrains Mono', 'Fira Code', ui-monospace, monospace;
  color-scheme: dark;
}
* { box-sizing: border-box; }
body { margin: 0; background: var(--base); color: var(--text); font: 15px/1.7 var(--sans); }
a { color: var(--link); text-decoration: none; overflow-wrap: anywhere; }
a:hover { color: var(--accent); text-decoration: underline; text-underline-offset: 3px; }
a:focus-visible, button:focus-visible, select:focus-visible, summary:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }
.bar { position: sticky; top: env(safe-area-inset-top, 0px); z-index: 5; background: var(--surface); border-bottom: 1px solid var(--line);
  min-height: 56px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 4px 16px; padding-block: 10px; padding-inline: 24px; }
.mark { font: 600 14px/1.3 var(--mono); color: var(--accent); letter-spacing: 0.02em; }
.range { font: 12px/1.3 var(--mono); color: var(--muted); font-variant-numeric: tabular-nums; }
.page { max-width: 720px; margin: 0 auto; padding-inline: 24px; padding-block: 20px 0; }
.weeks { display: flex; flex-wrap: wrap; align-items: center; gap: 8px; margin-bottom: 8px; }
.wk { font: 12px/1 var(--mono); color: var(--muted); background: transparent; border: 1px solid var(--line); border-radius: 3px; padding: 7px 10px; cursor: pointer; font-variant-numeric: tabular-nums; }
.wk:hover { color: var(--text); border-color: var(--faint); }
.wk[aria-current="true"] { color: var(--accent); border-color: var(--accent); }
.weeks select { font: 12px/1 var(--mono); color: var(--muted); background: var(--surface); border: 1px solid var(--line); border-radius: 3px; padding: 6px 8px; max-width: 100%; }
.week-head { margin: 20px 0 4px; }
.week-head h1 { font: 600 20px/1.3 var(--sans); color: var(--white); margin: 0; text-wrap: balance; }
.stats { margin: 4px 0 0; font: 12px/1.5 var(--mono); color: var(--muted); font-variant-numeric: tabular-nums; }
.label { font: 600 13px/1.4 var(--sans); color: var(--white); text-transform: uppercase; letter-spacing: 0.1em; margin: 32px 0 12px; }
.card { background: var(--surface); border: 1px solid var(--line); border-radius: 6px; padding: 20px; margin-bottom: 12px; min-width: 0; }
.card.patterns { border-left: 3px solid var(--accent); }
.card h3 { font: 600 15px/1.4 var(--sans); color: var(--white); margin: 0 0 8px; text-wrap: balance; }
.card p { margin: 0 0 10px; }
.card p:last-child, .card ul:last-child, .card ol:last-child { margin-bottom: 0; }
.card ul, .card ol { margin: 0 0 10px; padding-left: 20px; display: grid; gap: 10px; }
.meta { display: flex; flex-wrap: wrap; align-items: center; gap: 6px 10px; margin-bottom: 12px !important; }
.badge { border: 1px solid var(--accent); color: var(--accent); font: 11px/1.6 var(--mono); border-radius: 3px; padding: 1px 6px; white-space: nowrap; }
.chip { font: 12px/1.5 var(--mono); color: var(--muted); }
.tag { font: 11px/1.5 var(--mono); color: var(--accent); white-space: nowrap; }
.dot { font-size: 14px; }
code { font: 12px/1.5 var(--mono); color: var(--muted); background: var(--base); border: 1px solid var(--line); border-radius: 3px; padding: 0 4px; overflow-wrap: anywhere; }
strong { color: var(--white); font-weight: 600; }
.note { font-size: 13px; color: var(--muted); }
details.audit summary { cursor: pointer; font: 12px/1.5 var(--mono); color: var(--muted); text-transform: uppercase; letter-spacing: 0.06em; }
details.audit[open] summary { margin-bottom: 12px; }
details.audit { font-size: 13px; line-height: 1.6; }
footer { max-width: 720px; margin: 0 auto; text-align: center; color: var(--faint); font: 11px/1.8 var(--mono); padding-block: 32px 48px; padding-inline: 24px; }
footer a { color: var(--muted); }
@media (max-width: 600px) {
  .bar, .page, footer { padding-inline: 16px; }
  .card { padding: 16px; }
}
"""

JS = """
(function () {
  var weeks = Array.prototype.slice.call(document.querySelectorAll('.week'));
  var chips = Array.prototype.slice.call(document.querySelectorAll('.wk'));
  var select = document.getElementById('week-select');
  var range = document.getElementById('range');
  function show(id, push) {
    var target = document.getElementById(id);
    if (!target || !target.classList.contains('week')) return;
    weeks.forEach(function (w) { w.hidden = w !== target; });
    chips.forEach(function (c) { c.setAttribute('aria-current', c.dataset.week === id ? 'true' : 'false'); });
    if (select) select.value = id;
    if (range) range.textContent = target.dataset.range;
    if (push) { try { history.replaceState(null, '', '#' + id); } catch (e) {} window.scrollTo(0, 0); }
  }
  chips.forEach(function (c) { c.addEventListener('click', function () { show(c.dataset.week, true); }); });
  if (select) select.addEventListener('change', function () { show(select.value, true); });
  window.addEventListener('hashchange', function () { show(location.hash.slice(1), false); });
  if (location.hash) show(location.hash.slice(1), false);
})();
"""


def render(reports: list[dict]) -> str:
    reports = sorted(reports, key=lambda r: r["name"], reverse=True)
    if not reports:
        raise SystemExit("no reports to render")
    latest = reports[0]
    chips = "".join(
        f'<button type="button" class="wk" data-week="w{r["name"]}" aria-current="{"true" if i == 0 else "false"}">'
        f'{d(r["name"]):%b} {d(r["name"]).day}</button>'
        for i, r in enumerate(reports[:6]))
    options = "".join(f'<option value="w{r["name"]}">{html.escape(fmt_range(r["fm"].get("week"), r["name"]))}</option>'
                      for r in reports)
    weeks_html = "\n".join(render_week(r, i == 0) for i, r in enumerate(reports))
    return f"""<title>Self-Custody &amp; Sovereignty Signal Report</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&family=JetBrains+Mono:wght@400;600&display=swap">
<style>{CSS}</style>
<header class="bar">
  <span class="mark">SELF-CUSTODY &amp; SOVEREIGNTY SIGNAL REPORT</span>
  <span class="range" id="range">{html.escape(fmt_range(latest["fm"].get("week"), latest["name"]))}</span>
</header>
<main class="page">
  <nav class="weeks" aria-label="Report weeks">
    {chips}
    <label class="chip" for="week-select">All weeks</label>
    <select id="week-select">{options}</select>
  </nav>
{weeks_html}
</main>
<footer>
  Generated {html.escape(str(latest["fm"].get("generated", latest["name"])))} · 7-day window, no repeats across weeks · IACR · arXiv · EIPs · Regulatory bodies · Institutional research · Audit firms<br>
  {len(reports)} weekly reports · <a href="{REPO_SIGNALS_URL}" target="_blank" rel="noopener">Markdown archive on GitHub</a>
</footer>
<script>{JS}</script>
"""


# ---------------------------------------------------------------- cli

def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p1 = sub.add_parser("prior")
    p1.add_argument("--today")
    p1.add_argument("--dir", action="append")
    p2 = sub.add_parser("validate")
    p2.add_argument("file")
    p2.add_argument("--dir", action="append")
    p3 = sub.add_parser("render")
    p3.add_argument("--out", required=True)
    p3.add_argument("--dir", action="append")
    a = ap.parse_args(argv)
    dirs = [pathlib.Path(x) for x in (a.dir or [str(ROOT / "signals")])]
    reports = load_reports(dirs)
    if a.cmd == "prior":
        today = d(a.today) if a.today else dt.datetime.now(dt.timezone.utc).date()
        print(json.dumps(compute_prior(reports, today), indent=2, ensure_ascii=False))
        return 0
    if a.cmd == "validate":
        path = pathlib.Path(a.file)
        errors, warnings = validate(path, [r for r in reports if r["name"] != path.stem])
        for w in warnings:
            print(f"warning: {w}")
        for e in errors:
            print(f"ERROR: {e}")
        print(f"{path.name}: {len(errors)} errors, {len(warnings)} warnings")
        return 1 if errors else 0
    if a.cmd == "render":
        out = pathlib.Path(a.out)
        out.write_text(render(reports), encoding="utf-8")
        print(f"wrote {out} ({out.stat().st_size:,} bytes, {len(reports)} weeks)")
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
