# Signal Report — artifact visual spec

A self-contained HTML page with all CSS and JS inline. Follow the 60-30-10 color system strictly and use no other colors.

## Color
- **60% base** `#0e0e0e`: page background.
- **30% surface** `#1c1c1c`: cards, header bar, dividers; borders `1px solid #2a2a2a`.
- **10% accent** `#F7931A`: only for strength badges, link hover, the title wordmark, source type tags, and the Porto lens left border. Never use it as a fill on large areas.

## Type
- `'Inter', system-ui, -apple-system, sans-serif` (Google Fonts)
- Body `#e8e8e8`, 15px, line-height 1.7
- Labels and tags `#888`, 12px, `'JetBrains Mono', 'Fira Code', monospace` (Google Fonts)
- Section headings `#fff`, 13px uppercase, letter-spacing 0.1em
- Strength emoji 14px inline

## Layout
- Max-width 720px, centered, padding 0 24px
- Header: full-width `#1c1c1c`, 56px tall; title `#F7931A` 14px/600 mono; date range `#888` 12px, right-aligned
- Cards: `#1c1c1c`, `1px solid #2a2a2a`, radius 6px, padding 20px, margin-bottom 12px
- Porto lens card: `border-left: 3px solid #F7931A`
- Source tags: mono, `#F7931A`, 11px, no background
- Strength badge: transparent, `1px solid #F7931A`, `#F7931A`, 11px, radius 3px, padding 1px 6px
- Links `#aaa`, underlined and `#F7931A` on hover
- Footer `#555`, 11px, centered, padding 32px 0. Text: "Generated [date] · 7-day recency gate applied · IACR · arXiv · EIPs · Regulatory bodies · Institutional research · Audit firms", plus a link to the `signals/` archive.

## Don't
No gradients, shadows, glows, decoration, colored card backgrounds, large orange fills, serif fonts or animations.
