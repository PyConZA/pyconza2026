---
name: brand-colors
description: PyConZA 2026 colour palette (Deep Indigo, Sandstone Cream, Protea Pink, Fynbos Olive), neutral scale, full WCAG 2.2 AA contrast matrix, and 60/25/10/5 usage proportions. Use when picking colours for any text/background pair or composition.
---

# Colour system

## Primary palette

The palette has four anchor colours drawn from late-afternoon Atlantic light: deep sea, sandstone rock, a single protea, and fynbos undergrowth.

| Name            | Hex       | RGB             | CMYK (approx.)      | Pantone (nearest) | Primary use |
|-----------------|-----------|-----------------|---------------------|-------------------|-------------|
| Deep Indigo     | `#1A2B4C` | 26, 43, 76      | 96 / 82 / 38 / 35   | PMS 281 C         | Dominant background, dark text, hero blocks |
| Sandstone Cream | `#E8DDC8` | 232, 221, 200   | 9 / 12 / 22 / 0     | PMS 9184 C        | Dominant background for light layouts, breathing room |
| Protea Pink     | `#C2185B` | 194, 24, 91     | 20 / 100 / 55 / 12  | PMS 214 C         | Single accent; focal hit — headlines, callouts, one CTA per surface |
| Fynbos Olive    | `#4A6B3F` | 74, 107, 63     | 68 / 37 / 91 / 30   | PMS 574 C         | Secondary accent; dividers, motif fills, subdued callouts |

Pantone and CMYK values are approximate and intended for briefing printers. Always ask the printer for a proof and a Pantone draw-down before signing off on large runs.

## Extended neutral scale

Brand colours alone are not enough for UI and body text. This neutral scale fills the gaps. **None of these introduce a fifth brand colour** — they are grey/off-white utilities.

| Name       | Hex       | RGB             | Primary use |
|------------|-----------|-----------------|-------------|
| Ink Black  | `#0E1420` | 14, 20, 32      | Body text on light backgrounds when Deep Indigo is too warm; print black |
| Off-White  | `#FAF6EE` | 250, 246, 238   | Body text backgrounds, card surfaces, slide backgrounds |
| Grey 700   | `#3A3F47` | 58, 63, 71      | Secondary body text, metadata, form labels |
| Grey 500   | `#6B7280` | 107, 114, 128   | Disabled states, placeholder text, non-essential metadata — **not for body text on any brand background (see contrast matrix below)** |
| Grey 300   | `#B9BEC6` | 185, 190, 198   | Borders, dividers, subtle rules — **never text** |

## Accessibility — contrast matrix

WCAG 2.2 AA thresholds:

- **Normal text** (below 18pt / 24px, or below 14pt / 18.66px bold): **4.5:1**
- **Large text** (18pt+ / 24px+, or 14pt+ / 18.66px+ bold): **3:1**
- **Non-text & UI components** (icons, focus rings, graphical boundaries): **3:1**

Each cell below is "foreground on background". Ratios calculated from the WCAG 2.2 relative-luminance formula. `AA` means passes normal-text 4.5:1; `AA-Lg` means passes large-text / UI 3:1 but fails normal text; `✗` means fails all thresholds and **must not be used for text or informative UI**.

| ↓ FG \ BG →    | Indigo | Cream | Pink | Olive | Black | Off-W | G700 | G500 | G300 |
|----------------|--------|-------|------|-------|-------|-------|------|------|------|
| **Indigo**     | —       | 10.45 AA | 2.39 ✗ | 2.32 ✗ | 1.31 ✗ | 13.04 AA | 1.33 ✗ | 2.91 ✗ | 7.53 AA |
| **Cream**      | 10.45 AA | —      | 4.37 AA-Lg | 4.50 AA | 13.70 AA | 1.25 ✗ | 7.88 AA | 3.59 AA-Lg | 1.39 ✗ |
| **Pink**       | 2.39 ✗ | 4.37 AA-Lg | — | 1.03 ✗ | 3.14 AA-Lg | 5.45 AA | 1.80 ✗ | 1.21 ✗ | 3.14 AA-Lg |
| **Olive**      | 2.32 ✗ | 4.50 AA | 1.03 ✗ | — | 3.04 AA-Lg | 5.62 AA | 1.75 ✗ | 1.25 ✗ | 3.24 AA-Lg |
| **Black**      | 1.31 ✗ | 13.70 AA | 3.14 AA-Lg | 3.04 AA-Lg | — | 17.10 AA | 1.74 ✗ | 3.81 AA-Lg | 9.87 AA |
| **Off-White**  | 13.04 AA | 1.25 ✗ | 5.45 AA | 5.62 AA | 17.10 AA | — | 9.83 AA | 4.48 AA-Lg | 1.73 ✗ |
| **Grey 700**   | 1.33 ✗ | 7.88 AA | 1.80 ✗ | 1.75 ✗ | 1.74 ✗ | 9.83 AA | — | 2.19 ✗ | 5.67 AA |
| **Grey 500**   | 2.91 ✗ | 3.59 AA-Lg | 1.21 ✗ | 1.25 ✗ | 3.81 AA-Lg | 4.48 AA-Lg | 2.19 ✗ | — | 2.59 ✗ |
| **Grey 300**   | 7.53 AA | 1.39 ✗ | 3.14 AA-Lg | 3.24 AA-Lg | 9.87 AA | 1.73 ✗ | 5.67 AA | 2.59 ✗ | — |

**Rules derived from this table.**

- **Body text pairings (AA normal):** Indigo on Cream, Indigo on Off-White, Indigo on Grey 300; Cream on Indigo, Cream on Black, Cream on Olive, Cream on Grey 700; Off-White on Indigo, Off-White on Pink, Off-White on Olive, Off-White on Black, Off-White on Grey 700; Black on Cream, Black on Off-White, Black on Grey 300; Grey 700 on Cream, Grey 700 on Off-White, Grey 700 on Grey 300; Grey 300 on Indigo, Grey 300 on Black, Grey 300 on Grey 700.
- **Headline-only pairings (AA large, 3:1 – 4.5:1):** Pink on Cream, Pink on Black, Pink on Grey 300; Olive on Black, Olive on Grey 300; Black on Pink, Black on Olive, Black on Grey 500; Cream on Pink, Cream on Grey 500; Off-White on Grey 500; Grey 500 on Cream, Grey 500 on Black, Grey 500 on Off-White. These are only usable at 24px+ or 18.66px+ bold. Do not use for body copy.
- **Never for text:** any combination marked ✗.

Two specific combinations to watch:

- **Protea Pink on Sandstone Cream** is our signature accent pairing, and it fails normal-text AA at 4.37:1. It passes AA-large at 3:1. **Use it for display headlines ≥24px or ≥18.66px bold only.** Never use it for body copy, form labels, or anything below 24px.
- **Fynbos Olive on Sandstone Cream** passes AA at 4.50:1 — just. Treat it as legitimate for body copy but avoid long reading passages; it is a tight pass and loses ground at smaller sizes on low-quality screens.

## Usage proportions

Use these as a starting target per composition. They produce the "late-afternoon Atlantic" feel rather than a flat colour block.

- **~60% Deep Indigo** — dominant field, including backgrounds and dark blocks.
- **~25% Sandstone Cream** — breathing room, cards, counterpoint to indigo.
- **~10% Protea Pink** — one confident focal hit per surface. If the composition has two pink elements, the second is probably a mistake.
- **~5% Fynbos Olive** — dividers, motif fills, small accents.

Deviate when the surface demands it — a light-background email will invert to ~60% cream / 25% indigo — but keep Protea Pink under ~15% and Fynbos Olive under ~10% in every case. Pink is a focal hit, not a field colour.

## Don'ts

Do not:

- Create gradients between any two brand colours. The palette is flat. No indigo-to-pink fades, no olive-to-cream washes.
- Introduce tints or shades beyond the nine named values above. If you need lighter or darker, use one of the named greys.
- Add off-palette accents — no teals, oranges, "hot pink" substitutes, or neon versions of the brand colours.
- Combine Protea Pink and Fynbos Olive as foreground-on-background in either direction. They are near-identical in luminance (contrast 1.03:1) and illegible when paired.
- Use Grey 500 for body text on Cream or Off-White. It fails AA.
- Apply brand colours at reduced opacity to simulate tints (e.g. Indigo at 40% on Cream). This produces unpredictable contrast. Use named greys instead.
