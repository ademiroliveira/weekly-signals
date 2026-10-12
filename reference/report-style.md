# Signal Report: artifact visual spec

The artifact page is **generated** by `python3 scripts/signals.py render`. Don't hand-write the HTML. Change the CSS in `scripts/signals.py`, and update this spec to match. The page carries every archived week, and a week switcher selects which one is shown (newest by default, deep-linkable as `#wYYYY-MM-DD`).

It is a single dark theme on purpose: `color-scheme: dark` and an explicit body background, following the 60-30-10 color system strictly with no other colors.

## Color
- **60% base** `#0e0e0e`: page background.
- **30% surface** `#1c1c1c`: cards, header bar, dividers; borders `1px solid #2a2a2a`.
- **10% accent** `#F7931A`, used only for:
  - strength badges
  - link hover
  - the title wordmark
  - source type tags
  - the active week chip
  - the left border of the **Patterns across weeks** cards

  Never use it as a fill on large areas.

## Type
- `'Inter', system-ui, -apple-system, sans-serif` (Google Fonts)
- Body `#e8e8e8`, 15px, line-height 1.7
- Labels, chips and tags in `'JetBrains Mono', 'Fira Code', monospace` (Google Fonts), muted `#8f8f8f`, 11–12px
- Section headings `#fff`, 13px uppercase, letter-spacing 0.1em
- Strength emoji 14px inline

## Layout
- Reading column: max-width 720px, centered, side padding 24px (16px under 600px)
- **Header:** sticky (`top: env(safe-area-inset-top, 0px)`), `#1c1c1c`, at least 56px tall. Title `#F7931A` 14px/600 mono, and the selected week's date range `#888` 12px, right-aligned. It wraps onto two lines on phones.
- **Week switcher:** chips for the six newest weeks (1px `#2a2a2a` border, radius 3px; the active one has an accent border and text), plus an "All weeks" select.
- **Week heading:** "Week of <range>" in 20px/600 white, then a mono stats line: verified · killed · generated.
- **Cards:** `#1c1c1c`, `1px solid #2a2a2a`, radius 6px, padding 20px (16px on phones), margin-bottom 12px.
- **Patterns across weeks cards:** `border-left: 3px solid #F7931A`.
- **Meta line** under each item title: strength badge, then mono chips for stage, origin and domains, then the tag.
- **Source tags:** mono, `#F7931A`, 11px, no background.
- **Strength badge:** transparent, `1px solid #F7931A`, `#F7931A`, 11px, radius 3px, padding 1px 6px.
- **Links:** `#aaa`, shown as a shortened host/path. Underlined and `#F7931A` on hover. Visible focus outline in accent.
- **Source audit:** a collapsed `<details>` card whose summary shows the kill count.
- **Footer:** `#5c5c5c`, 11px mono, centered, padding 32px 0. Text: "Generated [date] · 7-day window, no repeats across weeks · IACR · arXiv · EIPs · Regulatory bodies · Institutional research · Audit firms", the number of weekly reports, and a link to the markdown archive on GitHub.

## Don't
- No gradients, shadows, glows, decoration, colored card backgrounds, large orange fills, serif fonts or animations.
- No download links: the artifact viewer blocks them. Past weeks are browsed in the page.
