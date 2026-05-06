---
name: brand-layout
description: PyConZA 2026 grids, breakpoints (mobile/tablet/desktop/wide), social formats (1080×1080, 1080×1920), whitespace philosophy, footer zone placement, and canonical wireframes for social/web/email/slide. Use when laying out any composition.
---

# Layout & grid

## Twelve-column grid — web

| Breakpoint  | Min width | Max width | Columns | Gutter | Outer margin |
|-------------|-----------|-----------|---------|--------|--------------|
| Mobile      | 320 px    | 639 px    | 4       | 16 px  | 16 px (5% min) |
| Tablet      | 640 px    | 1023 px   | 8       | 24 px  | 32 px |
| Desktop     | 1024 px   | 1439 px   | 12      | 24 px  | 48 px |
| Desktop-wide| 1440 px   | 1920 px   | 12      | 32 px  | 80 px |
| Large       | 1920 px+  | —         | 12      | 32 px  | max content width 1440 px, centred |

Content inside the grid never exceeds a maximum text-measure of **72 characters** for body copy. At desktop widths this means body text columns occupy 6–8 grid columns, not the full 12.

## Grid — 1080×1080 social graphics

- 12 columns, 60 px gutter.
- Outer margin: **96 px** on all sides (≈9% of canvas). This is our quantified "generous" — never less.
- Safe zone for all essential content: 96 px from each edge, giving an 888×888 active area.

## Grid — 1080×1920 social story (9:16)

- 6 columns, 48 px gutter.
- Outer margin: 72 px sides, 160 px top (below status bar), 240 px bottom (above controls).
- Essential content inside the central 1520 px of vertical space.

## Whitespace philosophy

"Generous whitespace" quantified:

- Minimum margin around any hero element: **8% of the shorter canvas dimension**.
- Minimum whitespace between motif and text: 1× the motif's shorter dimension.
- Minimum whitespace between two text blocks of different hierarchy: 1× the line-height of the larger block.

If the composition feels tight, the first move is to remove an element, not to shrink the margins.

## Logo, URL, and date placement zones

The canonical footer-zone layout for social and print:

```
┌──────────────────────────────────────────────┐
│ [PyConZA 2026 wordmark]                      │  ← top-left, ~15% canvas width
│                                              │
│                                              │
│            [hero content]                    │
│                                              │
│                                              │
│                                              │
│ 🐍                          za.pycon.org     │  ← Python mark bottom-left
│ October 2026 · Cape Town, South Africa       │  ← URL bottom-right, mono
└──────────────────────────────────────────────┘
```

- **Wordmark:** top-left, ~15% of canvas width. Clear space per the brand-logo skill.
- **URL:** bottom-right, monospace (JetBrains Mono), sized so cap height ≈ 2% of canvas height.
- **Date line:** bottom-centre or aligned with URL, mixing Inter and mono.
- **Python mark:** bottom-left or bottom-right, paired with URL or date as in the brand-logo skill.

## Common-layout wireframes

**Social square (1080×1080) — save-the-date:**

```
┌──────────────────────────────────────────────┐
│ PyConZA 2026                                 │
│                                              │
│               ╱╲  ╱╲  ╱╲                     │
│              (  🌺  )   ← Protea hero       │
│               ╲╱  ╲╱  ╲╱                     │
│       "PyConZA 2026"                         │
│      October · Cape Town                     │
│                                              │
│ ╱╲╱╲   Table Mtn + Lion's Head silhouette    │
│                                              │
│ 🐍 za.pycon.org                              │
│ ████████████████  ← Shweshwe strip bottom   │
└──────────────────────────────────────────────┘
```

**Social story (1080×1920):**

```
┌────────────────────┐
│ PyConZA 2026       │
│                    │
│                    │
│                    │
│      🌺            │
│     Protea         │
│    (smaller)       │
│                    │
│                    │
│   Headline         │
│   subhead          │
│                    │
│                    │
│  ╱╲╱╲ ridge        │
│                    │
│ 🐍  za.pycon.org   │
│ ██████ Shweshwe    │
└────────────────────┘
```

**Web hero (desktop 1440):**

```
┌─────────────────────────────────────────────────────────────────┐
│ [nav]                                                       [☰] │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  H1 headline              │   🌺                               │
│  Inter body lead          │  Protea                             │
│  [CTA button — Pink]      │   (right 40% of hero)              │
│                                                                 │
│  ╱╲╱╲ ridge silhouette spanning full width                      │
└─────────────────────────────────────────────────────────────────┘
```

**Email header:**

```
┌──────────────────────────────────────┐
│ PyConZA 2026                         │
│ ───── indent-bars                    │
│   [Email subject as H2]              │
└──────────────────────────────────────┘
```

**Slide title (16:9):**

```
┌──────────────────────────────────────────────────┐
│                                                  │
│                🌺                                │
│                                                  │
│            Talk title                            │
│            Speaker name — affiliation            │
│                                                  │
│ 🐍 za.pycon.org · October 2026                   │
│ ███████████ Shweshwe strip                       │
└──────────────────────────────────────────────────┘
```
