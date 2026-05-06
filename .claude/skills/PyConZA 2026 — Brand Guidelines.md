# PyConZA 2026 — Brand Guidelines

**Cape Town, October 2026**

**Version:** 1.0 (draft)
**Issued:** 2026
**Next review:** before CFP launch
**Owner:** PyConZA 2026 organising committee

---

## Table of contents

1. Introduction & brand positioning
2. Logo & wordmark
3. Colour system
4. Typography
5. Motif kit & illustration
6. Layout & grid
7. Voice & tone
8. Application examples
9. Accessibility summary
10. File naming, handoff, and sources
11. Appendix A — CSS variables

---

## 1. Introduction & brand positioning

### 1.1 Brand statement

PyConZA 2026 is the South African national Python conference, held in Cape Town in October 2026. Our 2026 identity is anchored in a single place and a single light: late-afternoon Atlantic light over Sea Point — deep indigo sea, pale sandstone rock, a confident hit of protea pink. The visual system reads as coastal, considered, and adult. It sounds warm and technically credible, quietly confident without being corporate. We want every poster, slide, and social post to read as "a Python event that knows exactly where it is" — welcoming to anyone arriving from Nairobi, Lagos, Accra, Berlin or Buenos Aires, unmistakably made in the Cape.

### 1.2 Brand principles

Five principles guide every design and copy decision. When a decision is unclear, run it past these in order.

**1. Distinctly Capetonian.** The identity is specific to this city in this season. It references Table Mountain, Lion's Head, the Atlantic seaboard, and fynbos — directly, not as generic "African" imagery. In practice this means: we use the motif kit in section 5 rather than reaching for sunsets, acacia trees, or safari imagery. It rules out pan-African visual shorthand that could apply equally to a conference in any other city on the continent.

**2. Technically credible.** We are a conference for engineers, researchers, educators, and students who work in Python. The identity respects their intelligence: clean typography, accurate code samples when code appears, monospace used with precision, no decorative "fake code" on graphics. In practice: if a graphic shows code, it is valid Python. It rules out terminal-window chrome, ASCII art, and code-as-decoration.

**3. Warm and unpretentious.** The conference belongs to its community, not to its organisers. Copy addresses people directly, admits mistakes plainly, and avoids marketing language. In practice: we write "the schedule is live" not "we are thrilled to announce that the schedule has officially dropped". It rules out superlatives, hype, and the performative register common in tech marketing.

**4. Pan-African-aware.** PyConZA sits within a continental Python community. We host speakers and attendees from across Africa and beyond, and our visual and verbal choices reflect that. In practice: copy avoids South-Africa-only idioms without translation, the motif kit does not borrow from traditions outside the Cape without explicit sourcing, and we note Shweshwe's origin when we use its visual vocabulary. It rules out flattening the continent into a single aesthetic and rules out using "African" as a catch-all adjective.

**5. Accessible by default.** WCAG 2.2 AA is a floor, not a target. Every colour combination in this document has been checked for contrast. Type sizes are set for readability first. In practice: if a combination fails AA, it is not used for text — no exceptions, no "it's only a decorative heading". It rules out decisions that trade legibility for style.



## 2. Logo & wordmark

### 2.1 Status

The PyConZA 2026 wordmark is a **placeholder** throughout this document. Final logo files (SVG, PNG at multiple sizes, monochrome variants) will be delivered to both teams separately. The rules in this section apply to the final files when they arrive.

### 2.2 Composition

The 2026 mark is a wordmark — "PyConZA 2026" set in our headline typeface — locked with a small Python two-snake glyph. Three variants will be supplied:

- **Primary** — wordmark in Deep Indigo on Sandstone Cream.
- **Reverse** — wordmark in Sandstone Cream on Deep Indigo.
- **Monochrome** — wordmark in Ink Black or Off-White, single colour only.

Always use the supplied files. Never re-typeset the wordmark by hand in a slide or social graphic.

### 2.3 Clear space

The minimum clear space around the wordmark is equal to the cap height of the "P" in "PyConZA". No other element — text, motif, logo, photo edge — may enter this zone.

```
         [ clear space = 1× cap-height ]
    ┌─────────────────────────────────────┐
    │                                     │
    │     PyConZA 2026  🐍                │
    │                                     │
    └─────────────────────────────────────┘
         [ clear space = 1× cap-height ]
```

### 2.4 Minimum sizes

| Medium   | Minimum wordmark height |
|----------|-------------------------|
| Web / digital | 24 px |
| Favicon / app icon | use supplied icon-only mark, not the wordmark |
| Print (offset or digital) | 8 mm |
| Large-format (signage, banners) | 40 mm |
| Merch embroidery | 12 mm, simplified supplied version only |

Below these sizes the mark becomes illegible and should not be used.

### 2.5 Relationship to the Python two-snake mark

The Python mark is the property of the Python Software Foundation and appears on PyConZA 2026 materials by convention, not by ownership. Rules:

- Use only the **monochrome** version on PyConZA materials (single colour — Deep Indigo, Ink Black, Sandstone Cream, or Off-White depending on background).
- Do not recolour the Python mark in Protea Pink, Fynbos Olive, or any palette colour other than the four listed above.
- Default placement is the **footer zone** of the composition — bottom-left or bottom-right, scaled to sit alongside the event URL.
- The Python mark is not a decorative element. It is not pattern-repeated, enlarged as a hero, or used as a background watermark.
- Clear space around the Python mark is half its height on all sides.

### 2.6 Don'ts

Do not:

- Stretch, skew, or rotate the wordmark.
- Recolour the wordmark outside the primary palette (sections 3.1–3.2).
- Place the wordmark on busy photographic backgrounds or on any of the motif patterns at full opacity.
- Add drop shadows, glows, bevels, outlines, or any effect not in the supplied files.
- Re-typeset the wordmark by hand in slides, emails, or social graphics.
- Crop the wordmark or use any part of it (e.g. just "ZA") as a standalone graphic.
- Place the wordmark inside a coloured pill, button, or badge.

---

## 3. Colour system

### 3.1 Primary palette

The palette has four anchor colours drawn from late-afternoon Atlantic light: deep sea, sandstone rock, a single protea, and fynbos undergrowth.

| Name            | Hex       | RGB             | CMYK (approx.)      | Pantone (nearest) | Primary use |
|-----------------|-----------|-----------------|---------------------|-------------------|-------------|
| Deep Indigo     | `#1A2B4C` | 26, 43, 76      | 96 / 82 / 38 / 35   | PMS 281 C         | Dominant background, dark text, hero blocks |
| Sandstone Cream | `#E8DDC8` | 232, 221, 200   | 9 / 12 / 22 / 0     | PMS 9184 C        | Dominant background for light layouts, breathing room |
| Protea Pink     | `#C2185B` | 194, 24, 91     | 20 / 100 / 55 / 12  | PMS 214 C         | Single accent; focal hit — headlines, callouts, one CTA per surface |
| Fynbos Olive    | `#4A6B3F` | 74, 107, 63     | 68 / 37 / 91 / 30   | PMS 574 C         | Secondary accent; dividers, motif fills, subdued callouts |

Pantone and CMYK values are approximate and intended for briefing printers. Always ask the printer for a proof and a Pantone draw-down before signing off on large runs.

### 3.2 Extended neutral scale

Brand colours alone are not enough for UI and body text. This neutral scale fills the gaps. **None of these introduce a fifth brand colour** — they are grey/off-white utilities.

| Name       | Hex       | RGB             | Primary use |
|------------|-----------|-----------------|-------------|
| Ink Black  | `#0E1420` | 14, 20, 32      | Body text on light backgrounds when Deep Indigo is too warm; print black |
| Off-White  | `#FAF6EE` | 250, 246, 238   | Body text backgrounds, card surfaces, slide backgrounds |
| Grey 700   | `#3A3F47` | 58, 63, 71      | Secondary body text, metadata, form labels |
| Grey 500   | `#6B7280` | 107, 114, 128   | Disabled states, placeholder text, non-essential metadata — **not for body text on any brand background (see 3.3)** |
| Grey 300   | `#B9BEC6` | 185, 190, 198   | Borders, dividers, subtle rules — **never text** |

### 3.3 Accessibility — contrast matrix

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

- **Protea Pink on Sandstone Cream** is our signature accent pairing, and it fails normal-text AA at 4.37:1. It passes AA-large at 3:1. **Use it for display headlines ≥24px or ≥18.66px bold only.** Never use it for body copy, captions, form labels, or anything below 24px.
- **Fynbos Olive on Sandstone Cream** passes AA at 4.50:1 — just. Treat it as legitimate for body copy but avoid long reading passages; it is a tight pass and loses ground at smaller sizes on low-quality screens.

### 3.4 Usage proportions

Use these as a starting target per composition. They produce the "late-afternoon Atlantic" feel rather than a flat colour block.

- **~60% Deep Indigo** — dominant field, including backgrounds and dark blocks.
- **~25% Sandstone Cream** — breathing room, cards, counterpoint to indigo.
- **~10% Protea Pink** — one confident focal hit per surface. If the composition has two pink elements, the second is probably a mistake.
- **~5% Fynbos Olive** — dividers, motif fills, small accents.

Deviate when the surface demands it — a light-background email will invert to ~60% cream / 25% indigo — but keep Protea Pink under ~15% and Fynbos Olive under ~10% in every case. Pink is a focal hit, not a field colour.

### 3.5 Don'ts

Do not:

- Create gradients between any two brand colours. The palette is flat. No indigo-to-pink fades, no olive-to-cream washes.
- Introduce tints or shades beyond the nine named values in 3.1 and 3.2. If you need lighter or darker, use one of the named greys.
- Add off-palette accents — no teals, oranges, "hot pink" substitutes, or neon versions of the brand colours.
- Combine Protea Pink and Fynbos Olive as foreground-on-background in either direction. They are near-identical in luminance (contrast 1.03:1) and illegible when paired.
- Use Grey 500 for body text on Cream or Off-White. It fails AA.
- Apply brand colours at reduced opacity to simulate tints (e.g. Indigo at 40% on Cream). This produces unpredictable contrast. Use named greys instead.

---

## 4. Typography

All three typefaces are free, open-source, and available on Google Fonts. License: SIL Open Font License 1.1 for all three.

### 4.1 The three roles

| Role     | Typeface        | Why |
|----------|-----------------|-----|
| Headline | **Space Grotesk** | Contemporary geometric sans with slightly condensed proportions and a confident, slightly quirky character — reads as modern without feeling corporate. Committed choice; do not substitute. |
| Body     | **Inter**        | Highly legible humanist sans designed specifically for UI and extended reading at small sizes. Excellent hinting on low-DPI screens, broad language support including the African language diacritics we may need. |
| Mono     | **JetBrains Mono** | Modern monospace with high legibility at small sizes, clear disambiguation of `0/O`, `1/l/I`, and `rn/m`. Used for dates, URLs, numeric callouts, and code. |

### 4.2 Web loading

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap">
```

CSS font-family stacks:

```css
--font-headline: "Space Grotesk", system-ui, -apple-system, "Segoe UI", sans-serif;
--font-body:     "Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
--font-mono:     "JetBrains Mono", ui-monospace, "SF Mono", Consolas, monospace;
```

Self-host the woff2 files for the conference site in production to avoid third-party requests and to meet POPIA data-minimisation expectations. Google Fonts is acceptable for slides, emails, and rapid prototypes.

### 4.3 Type scale

Web sizes are the baseline. Print sizes apply to the programme booklet, signage, and print collateral.

| Step   | Use                    | Web px | Web line-height | Letter-spacing | Weight | Print pt | Typeface |
|--------|------------------------|--------|-----------------|----------------|--------|----------|----------|
| H1     | Page / hero headline   | 48     | 56 (1.17)       | −0.01em        | 700    | 36       | Space Grotesk |
| H2     | Section headline       | 36     | 44 (1.22)       | −0.005em       | 600    | 28       | Space Grotesk |
| H3     | Sub-section headline   | 28     | 36 (1.29)       | 0              | 600    | 22       | Space Grotesk |
| H4     | Card / block headline  | 22     | 30 (1.36)       | 0              | 600    | 18       | Space Grotesk |
| H5     | Small headline / eyebrow | 18   | 26 (1.44)       | 0.02em         | 500    | 14       | Space Grotesk |
| H6     | Label / micro headline | 14     | 22 (1.57)       | 0.06em, uppercase | 500 | 11       | Space Grotesk |
| Body   | Default paragraph      | 16     | 26 (1.63)       | 0              | 400    | 11       | Inter |
| Body-L | Lead paragraph         | 18     | 30 (1.67)       | 0              | 400    | 12       | Inter |
| Small  | Secondary copy         | 14     | 22 (1.57)       | 0              | 400    | 10       | Inter |
| Caption | Image caption, footnote | 13    | 20 (1.54)       | 0.01em         | 400    | 9        | Inter |
| Mono   | URLs, dates, code      | 15     | 24 (1.60)       | 0              | 400    | 10       | JetBrains Mono |

**Minimums:** body never below 16px on web or 10pt in print. Captions at 13px web / 9pt print are the absolute floor, and should only be used for legitimate caption content, never for space-saving on body copy.

### 4.4 Pairing rules

- Every page/surface uses at most these three typefaces. Do not introduce a fourth.
- Headlines and body come from Space Grotesk and Inter respectively; do not swap — Inter is not a headline face at 48px, and Space Grotesk at 16px for body is tiring to read.
- Monospace is for dates, URLs, numeric callouts (e.g. "2026", "Day 2, Track 3"), and any actual code. It is not a decorative display face.
- For the section 3.3 rule: Protea Pink headlines must be 24px+ or 18.66px+ bold to pass AA-large on Cream.

### 4.5 Don'ts

Do not:

- Substitute Space Grotesk with Futura, Avenir, Montserrat, Poppins, or other "near enough" geometrics. The choice is specific.
- Set body copy in all-caps. Reserve uppercase for H6 labels and the rare short eyebrow.
- Letter-space body copy (0 is correct). Only display sizes and uppercase labels use tracking.
- Use italic as a stylistic flourish. Italic is for titles of works and genuine emphasis only.
- Underline text except for links.
- Justify body copy. Left-align (ragged right) in English.

---

## 5. Motif kit & illustration

The motif kit is the reusable visual vocabulary of PyConZA 2026. Every graphic draws from this kit. Nothing in the kit is optional window-dressing — each element has a defined role.

### 5.1 Geometric King Protea

The **hero anchor** of the identity. The King Protea is South Africa's national flower and the signature bloom of the Cape fynbos biome. Our version is a stylised geometric illustration — not a botanical rendering.

**Construction principles.**

- Flat vector, no photorealism, no gradients, no soft shadows.
- Built from simple geometric shapes: concentric petal rows as pointed arcs, a central dome as stacked semi-circles or a hexagonal core. Symmetrical on the vertical axis.
- Limited to two or three palette colours per instance — typically Protea Pink petals on an Indigo or Cream ground, with Olive or Cream used for the inner dome.
- A 4–6 row petal structure is the canonical form. Avoid over-detailing with 10+ petal rows; the flower should read instantly at thumbnail size.
- Outlines are uniform thickness or absent. No variable-width strokes.

**Scale guidance.**

| Surface            | Protea width (approx. % of canvas) |
|--------------------|------------------------------------|
| Social 1080×1080 (hero use)   | 40–50% |
| Social 1080×1920 story       | 35–45% |
| Web hero (desktop, 1440w)    | 25–35% |
| Slide title                   | 20–30% |
| Programme booklet cover       | 40–55% |
| Lanyard / badge              | do not use hero protea; use indent-bars motif instead |
| T-shirt front                | 30–45% of printable area |

**When to use.** Ceremonial, atmospheric, or "opener" surfaces: save-the-date, CFP launch, programme cover, t-shirt front, slide section dividers.

**When not to use.** Schedule rows, speaker cards, body content, sponsor pages, functional UI. The protea is the hero — deploying it everywhere flattens its impact.

### 5.2 Table Mountain + Lion's Head silhouette

A **two-line ridge** across the composition. Reads as the Cape Town skyline from the Atlantic seaboard side. Used as a grounding band, usually toward the lower third of a composition.

**Construction.**

- Two continuous lines representing the Table Mountain plateau (flat, characteristic) and Lion's Head (peaked, rounded).
- Simplified, geometric, flat — same drawing vocabulary as the protea.
- Single colour fill or single-colour line. Typically Indigo on Cream, or Cream on Indigo.
- Proportion: the ridge occupies 8–15% of canvas height, placed between 60% and 75% down the canvas.

**When to use.** Hero graphics, section dividers, programme cover, slide section dividers, signage. Pair with the protea sparingly — if the protea is hero, the ridge is grounding; they cohabit with whitespace between them.

**When not to use.** Speaker cards, schedule rows, email body blocks, merch where the silhouette would sit awkwardly at small scale.

### 5.3 Shweshwe-inspired geometric strip

A **geometric pattern strip** running along one full edge of the canvas. Visually recalls the discharge-print vocabulary of **Shweshwe** — bold, symmetric geometric blocks.

**A note on Shweshwe.** Shweshwe (isishweshwe) is a printed dyed cotton fabric with a long and specific South African history. It is manufactured by Da Gama Textiles in the Eastern Cape under the Three Cats brand and carries deep cultural meaning in South African dress, particularly in Xhosa, Sotho, and Tswana traditions. Our motif is **inspired by the visual vocabulary** — symmetric geometric blocks, bold positive-negative rhythm, precise small-scale repeat — and is **never a direct copy** of any specific traditional Shweshwe motif or pattern. We acknowledge the tradition by naming it in design credits and the programme colophon. This is respectful adjacency, not appropriation.

**Construction principles.**

- Symmetric geometric blocks: diamonds, squares, crosses, chevrons, dotted grids. Two-colour only per strip (typically Indigo and Cream, or Pink and Cream).
- A repeating unit of 2–4 shapes that tiles along the edge.
- Strip height 4–8% of canvas.
- Runs along **one full edge** — top, bottom, left, or right. Not wrapped around multiple edges, not used as a full background field.

**When to use.** One strip per composition as a finishing edge — hero graphics, programme cover, slide title slide, t-shirt back, tote bag.

**When not to use.** As a background field, as a frame on all four edges, or combined with other patterns. If the strip is present, no other pattern is.

**Design review check.** Before shipping, ask: "Does this pattern resemble a specific identifiable Shweshwe design?" If yes, redesign.

### 5.4 Indent-bars motif

A **small typographic/graphic device** — 3 to 5 short parallel bars, like the visual rhythm of code indentation. Our nod to the craft, without resorting to fake code or terminal windows.

**Construction.**

- 3–5 horizontal bars, each shorter than the last (or in a stepped indent pattern).
- Bars are uniform thickness, 2–4px on web, 0.5–1mm in print.
- Single colour — typically Pink on Indigo, or Indigo on Cream.
- Compact: the whole motif is 1–3% of canvas width.

**When to use.** Small decorative accents on lanyards, badges, email signatures, slide corners, stickers. The "quiet" motif — appears where the protea and ridge are too heavy.

**When not to use.** As a hero element. As a repeat pattern. Anywhere it would be mistaken for a bar chart.

### 5.5 Python two-snake mark

Covered in section 2.5. Summary for this section:

- Monochrome only on PyConZA materials.
- Footer zone placement (bottom-left or bottom-right, scaled to sit with the event URL).
- Not a decorative element. Not pattern-repeated. Not a hero.

### 5.6 Combination rules

One hero, one grounding element, one finishing edge. That's the canonical grammar.

| Motif combination                         | Verdict |
|-------------------------------------------|---------|
| Protea + ridge + Shweshwe strip + Python mark | ✓ Canonical hero layout — save-the-date, programme cover |
| Protea + ridge, no strip                  | ✓ Calmer hero — CFP announcement |
| Ridge + Shweshwe strip, no protea         | ✓ Section divider, secondary graphic |
| Indent-bars + Python mark only            | ✓ Lanyard, badge, email signature |
| Protea + Shweshwe strip, no ridge         | ✗ Avoid — composition floats without the grounding ridge |
| Two proteas in one composition            | ✗ Avoid — dilutes the hero |
| Shweshwe strip on multiple edges          | ✗ Avoid — becomes a frame, reads as decoration rather than finishing |
| Protea + indent-bars together             | ✗ Avoid — redundant; bars are the quiet motif for when protea is absent |
| Any motif inside a Python mark clear zone | ✗ Avoid — violates clear space (section 2.5) |

**Whitespace requirements.** Between any two motifs, minimum clearance is equal to the height of the smaller motif. The composition should feel generous. If it feels crowded, remove the smallest element first.

### 5.7 Must avoid — reproducing and extending the reference-prompt list

Do not use, anywhere on any PyConZA 2026 surface:

- **Acacia trees** or silhouette-tree-at-sunset imagery.
- **Generic African sunsets** — orange-red gradient skies as a decorative ground.
- **Safari animals** — the Big Five, silhouettes of lions/elephants/giraffes, animal tracks.
- **Tribal-style display fonts** — any typeface marketed as "African", "tribal", or "jungle". Our typefaces are listed in section 4; no exceptions.
- **Ndebele patterns copied directly** — the geometric house-painting tradition of Ndebele artists (and specifically the work of Esther Mahlangu and her lineage) is not our vocabulary. The Shweshwe-inspired strip is our one referential pattern and is clearly sourced.
- **Realistic snakes** — the Python mark is stylised; we do not use photographic or realistic snake imagery.
- **Terminal window chrome** — no fake terminal windows as compositional frames or decoration.
- **Code snippets as decoration** — code appears on PyConZA materials only when it is the subject of the content (talk abstracts, speaker slides by the speakers themselves). We do not scatter code fragments across graphics as "tech" texture.
- **ASCII art** — not a decorative style for our identity.
- **Photorealistic rendering** — no 3D renders of proteas, no photographic Table Mountain sunsets used as backgrounds, no stock photography behind graphics.
- **Stock-photo business aesthetics** — no "diverse group of smiling professionals around a laptop", no handshake-over-globe, no lens-flare tech imagery.
- **Generic tech-startup gradients** — no purple-to-blue, no pink-to-orange, no hero gradient washes. Our palette is flat.
- **The word "Mzansi" as decoration** — see section 7.7 on word choices.

---

## 6. Layout & grid

### 6.1 Twelve-column grid — web

| Breakpoint  | Min width | Max width | Columns | Gutter | Outer margin |
|-------------|-----------|-----------|---------|--------|--------------|
| Mobile      | 320 px    | 639 px    | 4       | 16 px  | 16 px (5% min) |
| Tablet      | 640 px    | 1023 px   | 8       | 24 px  | 32 px |
| Desktop     | 1024 px   | 1439 px   | 12      | 24 px  | 48 px |
| Desktop-wide| 1440 px   | 1920 px   | 12      | 32 px  | 80 px |
| Large       | 1920 px+  | —         | 12      | 32 px  | max content width 1440 px, centred |

Content inside the grid never exceeds a maximum text-measure of **72 characters** for body copy. At desktop widths this means body text columns occupy 6–8 grid columns, not the full 12.

### 6.2 Grid — 1080×1080 social graphics

- 12 columns, 60 px gutter.
- Outer margin: **96 px** on all sides (≈9% of canvas). This is our quantified "generous" — never less.
- Safe zone for all essential content: 96 px from each edge, giving an 888×888 active area.

### 6.3 Grid — 1080×1920 social story (9:16)

- 6 columns, 48 px gutter.
- Outer margin: 72 px sides, 160 px top (below status bar), 240 px bottom (above controls).
- Essential content inside the central 1520 px of vertical space.

### 6.4 Whitespace philosophy

"Generous whitespace" quantified:

- Minimum margin around any hero element: **8% of the shorter canvas dimension**.
- Minimum whitespace between motif and text: 1× the motif's shorter dimension.
- Minimum whitespace between two text blocks of different hierarchy: 1× the line-height of the larger block.

If the composition feels tight, the first move is to remove an element, not to shrink the margins.

### 6.5 Logo, URL, and date placement zones

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

- **Wordmark:** top-left, ~15% of canvas width. Clear space per section 2.3.
- **URL:** bottom-right, monospace (JetBrains Mono), sized so cap height ≈ 2% of canvas height.
- **Date line:** bottom-centre or aligned with URL, mixing Inter and mono.
- **Python mark:** bottom-left or bottom-right, paired with URL or date as section 2.5.

### 6.6 Common-layout wireframes

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

---

## 7. Voice & tone

### 7.1 Brand voice

PyConZA 2026 writes like a thoughtful colleague who knows their subject and their audience. Warm, technically credible, unpretentious, pan-African-aware, quietly confident. We are not a tech startup. We are not a corporate event. We are a community conference that takes its craft and its attendees seriously.

We use plain language. We favour short sentences. We address the reader directly. We admit mistakes clearly. We do not hype, we do not use superlatives, and we do not write copy that sounds like a press release.

### 7.2 Voice attributes — we are X, not Y

- **We are welcoming, not ingratiating.** We say "glad you're here". We do not say "we're so beyond excited to have you".
- **We are confident, not boastful.** We say "PyConZA is South Africa's Python conference". We do not say "the continent's premier world-class gathering of visionary developers".
- **We are specific, not generic.** We say "the workshop runs from 09:30 to 12:00 in Hall B". We do not say "join us for an amazing interactive session".
- **We are plain, not simple.** We write so any competent English reader can follow. We do not talk down, avoid technical words when they are the right words, or soften detail into vagueness.

### 7.3 Tone variation

Voice is constant. **Tone** shifts with context — the register turns up or down depending on what the reader needs in that moment.

- **CFP announcement** — energetic, inviting, specific about what we want. Register slightly warm.
  - *"The CFP is open. We're looking for talks, tutorials, and posters from the African Python community and the wider world — first-time speakers especially welcome. Submissions close 15 June."*
- **Schedule reminder** — informational, calm, practical. Register neutral.
  - *"Your talk is scheduled for Thursday, 14:00, in Hall B. Tech check is at 13:30. Slides in 16:9, please."*
- **Post-conference thank-you** — warm, specific, reflective. Register warm.
  - *"Thanks for being at PyConZA 2026. A conference is the people in the room, and this year's room was a good one. Talk recordings will be up on the site within six weeks."*
- **Apology for an issue** — direct, accountable, no excuses, no performative hand-wringing. Register even.
  - *"The registration site was down between 09:00 and 10:15 this morning. We've fixed the cause, extended early-bird by 48 hours, and refunded anyone who was charged twice. If you're still stuck, reply to this email and we'll sort it."*

### 7.4 Copy examples — before and after

#### 7.4.1 Social post: CFP opening

**Before (off-brand):**

> 🚀🚀🚀 HUGE news, friends!! We are BEYOND thrilled to announce that the CFP for #PyConZA2026 is OFFICIALLY open!! 🎉 We can't wait to see what amazing talks you'll bring to Cape Town this October!! Submit now and join the movement! 🐍🔥 #TechTwitter #Python #Mzansi

**After (on-brand):**

> The PyConZA 2026 call for proposals is open.
>
> We're looking for talks, tutorials, and posters from across the African Python community and beyond. Talks are 25 minutes; tutorials run 90 minutes. First-time speakers are especially welcome — we run a mentorship track.
>
> Submissions close 15 June. Full details: za.pycon.org/cfp

**Rationale.** The before version reaches for hype ("HUGE", "BEYOND thrilled", emoji pile-up) and uses "Mzansi" as decorative hashtag padding. The after version states the news, names what we want, gives the deadline, and points to detail. Confident without boasting, specific about formats, and welcoming in a way that is actionable ("mentorship track") rather than performative.

#### 7.4.2 Email: schedule reminder

**Before (off-brand):**

> **Subject:** 🎉 Don't miss out! Your PyConZA experience starts soon!
>
> Hi there! We hope this email finds you well! We're super excited to have you joining us at PyConZA 2026 — it's going to be an INCREDIBLE event packed with amazing content, networking opportunities, and unforgettable moments!

**After (on-brand):**

> **Subject:** PyConZA 2026 — your schedule and practical details
>
> Hi [first name],
>
> The conference starts on Monday. Here's what you need before you arrive: your badge QR code is attached; doors open at 08:00; the opening keynote is at 09:15 in the main hall. Full schedule and venue map: za.pycon.org/schedule.

**Rationale.** The before version is all warmth, no information, and the subject line tells the reader nothing. The after version treats the reader as an adult with a plane to catch — the subject line previews the content, the body delivers the three things they actually need (badge, doors, keynote location), and points to the rest.

#### 7.4.3 Website homepage hero — headline + subhead

**Before (off-brand):**

> # Unleash the power of Python in the heart of Africa
>
> Join us for a transformative journey of innovation, collaboration, and cutting-edge tech at PyConZA 2026 — the most exciting developer event on the continent.

**After (on-brand):**

> # PyConZA 2026
>
> ## South Africa's Python conference — Cape Town, October 2026.
>
> Three days of talks, tutorials, and conversation. Tickets and schedule from June.

**Rationale.** The before version is cliché-dense and says nothing concrete ("transformative journey", "cutting-edge tech", "most exciting on the continent"). The after version names the event, the place, the month, the format, and when to come back for tickets — in four short lines. Confident because it is specific.

#### 7.4.4 Slide template footer microcopy

**Before (off-brand):**

> Thanks for listening! 🐍 Don't forget to follow us on social media and use hashtag #PyConZA2026! Made with ❤️ in Cape Town

**After (on-brand):**

> za.pycon.org · #PyConZA2026 · Cape Town, October 2026

**Rationale.** Slide footers are read at a glance during a talk. One line, monospace, no sentiment. The URL, the hashtag, the place and date — that's all a slide footer needs. "Made with ❤️" belongs nowhere in our voice.

#### 7.4.5 Post-conference thank-you

**Before (off-brand):**

> 🥺✨ WOW. What a journey. PyConZA 2026 was absolutely everything and more. From the mind-blowing keynotes to the incredible hallway conversations, this community never ceases to amaze us. You are all rockstars. Until next time, never stop shipping! 🚀

**After (on-brand):**

> PyConZA 2026 is over. Thanks for being part of it.
>
> A conference is the people in the room, and this year's room was a good one — 420 attendees from 14 countries, 48 talks, 6 tutorials, and one power cut we handled better than we expected.
>
> Talk recordings will be on the site within six weeks. Feedback form: za.pycon.org/2026/feedback. If you ran into any problem we haven't addressed, reply here — we'd rather hear it than not.
>
> See you in 2027.

**Rationale.** The before version is a parody of tech-community farewells — performative gratitude, no specifics, a "rockstar" label most attendees would wince at. The after version says thank you, backs the thanks with numbers, acknowledges a real operational glitch without dwelling on it, provides a concrete next step (recordings, feedback), and opens a channel for problems. Warm because it is specific and honest.

### 7.5 Code-switching

South Africa is a multilingual country and PyConZA hosts attendees from across the continent. Code-switching — slipping between languages, registers, or cultural references — is welcome in conversational copy, but never forced and never tokenising.

- **Do.** Use local words where the word is the right word: *braai*, *bakkie*, *robot* (the traffic light), *Sea Point*, *Kirstenbosch*. Translate or gloss in contexts where international readers need it.
- **Don't.** Sprinkle local words into copy for flavour when the English word would do. Do not write "Howzit, are you lekker?" as a greeting. Do not use isiXhosa or isiZulu words in headline copy as decoration without speaker or author fluency.

### 7.6 Inclusivity

- **Gender-neutral language.** "Attendees", "speakers", "organisers", "folks", "people" — never "guys". "They" as singular pronoun when the gender is unknown or unspecified.
- **L2 English readers.** A significant share of our audience speaks English as a second or third language. Avoid idioms that do not translate: "knock it out of the park", "the whole nine yards", "piece of cake", "rain check". Prefer direct phrasing.
- **Accessibility in copy.** Spell out acronyms on first use. Avoid jargon in public-facing copy; keep it in speaker-facing copy where the audience is technical.
- **Naming.** When referring to attendees and speakers in lists and programmes, follow the form they register with — including diacritics, hyphenation, and name order. Do not westernise names or strip diacritics to fit a system.

### 7.7 Word choices

**Preferred terms.**

- *Attendee* (not *delegate*, not *participant* as default).
- *Speaker* (not *presenter* unless referring to a specific panel role).
- *Talk* (25-minute session). *Tutorial* (90-minute hands-on session). *Keynote* (invited headline talk).
- *Organiser*, *committee*, *volunteer* — we are volunteers, name it.
- *Code of conduct* (spelled out, lowercase unless at the start of a sentence; the document itself is titled "Code of Conduct").
- *Cape Town, South Africa* on first mention. *Cape Town* thereafter.
- *African Python community* (not *Africa's Python scene*).

**Terms to avoid.**

- *Mzansi* — acceptable in conversational contexts by South African team members writing in their own voice, e.g. a personal post from an organiser. **Not acceptable as decorative copy, hashtag filler, or headline word** ("Mzansi's Python event", "from Mzansi with love"). It reads as touristic when used as branding.
- *Rainbow Nation* — avoid entirely. Dated, politicised, not our register.
- *Synergy, disrupt, 10x, paradigm shift, leverage (as a verb), drive, unlock, deliver value, ecosystem (of a product), move the needle, at scale, crush it, ship fast, reach out* — Silicon-Valley tech jargon. Delete and rewrite.
- *Rockstar, ninja, guru, wizard* — not how we refer to engineers, speakers, or attendees.
- *Diverse* as a compliment applied to individuals ("a diverse speaker"). Describes groups, not people.
- *Amazing, incredible, unforgettable, game-changing, must-attend* — superlatives that bleach out. If something is good, say what is good about it.
- *Guys* (as gender-neutral) — use *folks*, *everyone*, *all of you*.
- *Going forward* — means "later" and is longer.
- *Folks* — widely acceptable; use naturally, not as a replacement for every third noun.

---

## 8. Application examples

Each application specifies the motifs, colour proportions, type sizes, layout, and an accessibility check. All examples assume the canonical footer zone from section 6.5 unless noted.

### 8.1 Social — 1080×1080 square

**Motifs.** Protea (hero, 40–50% width, centred slightly above vertical centre) + Table Mountain / Lion's Head ridge across lower third + Shweshwe-inspired strip along bottom edge + Python mark and URL in footer zone.

**Colour proportions.** ~60% Deep Indigo ground, ~25% Sandstone Cream negative space around protea, ~10% Protea Pink for the flower itself, ~5% Fynbos Olive for ridge and inner protea detail.

**Type sizes.** Headline ("PyConZA 2026") in Space Grotesk 700, 96 px on canvas; subhead (date + location) in Inter 500, 36 px; URL in JetBrains Mono 400, 24 px.

**Layout.** Wordmark top-left at 15% canvas width; headline centred below protea; date + location in lower-centre zone at 75% canvas height; URL bottom-right; Python mark bottom-left.

**Accessibility check.** Cream text on Indigo: 10.45:1 — AA. Pink protea on Indigo: decorative (not text), 2.39:1 — acceptable, meets 3:1 for adjacent colour distinction against cream. Headline (Pink on Cream if used for emphasis): 4.37:1 — AA-large only; only usable at the ≥24px display size here. Add alt text describing the protea, ridge, and conference details when posted.

### 8.2 Social — 1080×1920 story (9:16)

**Motifs.** Protea smaller (35–45% width) higher in canvas; ridge silhouette optional — typically omit for stories to keep vertical rhythm; Shweshwe strip along bottom edge above system controls; Python mark + URL bottom.

**Colour proportions.** ~65% Indigo, ~25% Cream, ~8% Pink, ~2% Olive.

**Type sizes.** Headline 84 px, subhead 30 px, URL 22 px.

**Layout.** Stack vertically: wordmark top, 200 px gap, protea, 120 px gap, headline, subhead, 240 px bottom zone reserved for controls.

**Accessibility check.** Same contrast pairings as 8.1. Remember Instagram/Facebook story UI overlays the top 160 px and bottom 240 px — keep all meaningful content out of those zones.

### 8.3 Social — Twitter/LinkedIn header

**Motifs.** Ridge silhouette full-width; Shweshwe strip along top edge; no protea (too decorative for a banner); Python mark and URL at bottom-right.

**Colour proportions.** ~70% Indigo, ~20% Cream, ~10% Pink (accent in headline).

**Type sizes.** Wordmark only + small tagline. Tagline in Inter 500, 28 px.

**Accessibility check.** Cream text on Indigo: 10.45:1 — AA. Platform crops differ (Twitter/X, LinkedIn personal vs company) — keep critical content inside a central safe zone of 1200×300 px for a 1500×500 canvas.

### 8.4 Web — homepage hero

**Motifs.** Protea right-aligned at 30–35% of hero width; ridge silhouette across full hero width at the hero's lower boundary; no Shweshwe strip on web hero (reserve for section dividers and footer).

**Colour proportions.** ~60% Indigo hero background, ~25% Cream for text column, ~10% Pink for CTA button, ~5% Olive for ridge accents.

**Type sizes.** H1 at 48 px (mobile) / 64–72 px (desktop, may step up beyond the default H1 size for hero impact); lead body at 18 px; CTA button text at 16 px with 44 px minimum tap height.

**Layout.** Two-column hero on desktop — text left (columns 1–6), protea right (columns 8–12); single-column stack on mobile with protea above text.

**Accessibility check.** Cream on Indigo headline: 10.45:1 — AA. CTA button: Cream on Pink: 5.45:1 — AA. Focus ring: Cream outline on Pink at 2 px, offset 2 px — 5.45:1 ratio between ring and background, passes 3:1 for non-text UI.

### 8.5 Web — speaker card

**Motifs.** None — speaker cards are functional UI. Optional indent-bars motif in Pink as a small decorative element top-left of the card at 1–2% of card width.

**Colour proportions.** Card on Off-White surface, Indigo name, Grey 700 title/affiliation, Pink session link.

**Type sizes.** Name in Space Grotesk 600 at 22 px; title/affiliation in Inter 400 at 14 px; session title in Inter 500 at 16 px; link in Inter 500 at 16 px.

**Layout.** Speaker photo (if provided) as a 120×120 px circle or square, name + affiliation right of photo on desktop, stacked on mobile. Card padding 24 px, border 1 px Grey 300.

**Accessibility check.** Indigo on Off-White: 13.04:1 — AA. Grey 700 on Off-White: 9.83:1 — AA. Pink link on Off-White: 5.45:1 — AA. Link underlined and bold on hover, focus ring Indigo at 2 px offset 2 px.

### 8.6 Web — schedule row

**Motifs.** None.

**Colour proportions.** Alternating row backgrounds — Off-White and a very light Cream variant (`#F4EEE1`, introduced here as a pure utility tint of Cream; this is the only sanctioned tint). Indigo for time + title; Grey 700 for room; Pink for talk tags.

**Type sizes.** Time in JetBrains Mono 500 at 15 px; title in Space Grotesk 600 at 18 px; speaker name in Inter 500 at 16 px; room in Inter 400 at 14 px.

**Layout.** Four columns at desktop (time | title + speaker | room | tags), stacks to time-title-room stack on mobile. Row padding 16 px vertical, 24 px horizontal.

**Accessibility check.** Indigo on Off-White: 13.04:1 — AA. Grey 700 on Off-White: 9.83:1 — AA. Pink tag text: render tags as Pink background with Off-White text (5.45:1 — AA), not Pink text on Cream which is AA-large only. Always accompany tag colour with the tag label — no information in colour alone.

### 8.7 Email — newsletter header

**Motifs.** Wordmark top-left, indent-bars motif below wordmark, optional small ridge silhouette full-width below the bars. No protea (too heavy for inbox render).

**Colour proportions.** Indigo bar across top at ~80 px tall; Cream body.

**Type sizes.** Wordmark at 24 px cap height; subject-as-H2 in body at 28 px.

**Layout.** 600 px max email width; single column; body copy at 16 px Inter 400. Use table-based layout for client compatibility (Outlook).

**Accessibility check.** Cream on Indigo in header: AA. Indigo body text on Cream body: AA. Alt text on wordmark image: "PyConZA 2026". Every image has alt text; images never carry information not also in text.

### 8.8 Email — campaign CTA block

**Motifs.** None. Plain CTA block.

**Colour proportions.** Indigo background block, Cream text, Pink CTA button with Off-White text.

**Type sizes.** Block headline at 24 px Space Grotesk 600; body at 16 px Inter 400; CTA button at 16 px, button height 48 px.

**Layout.** Block full width of 600 px container, 32 px internal padding.

**Accessibility check.** Cream on Indigo: AA. Off-White on Pink (button): 5.45:1 — AA. Make the CTA a real anchor tag, not an image.

### 8.9 Slides — title slide

**Motifs.** Protea left at 25% width; Shweshwe strip along bottom edge; Python mark + URL in footer zone.

**Colour proportions.** Indigo background, Cream headline, Pink for talk title emphasis if any.

**Type sizes.** Talk title in Space Grotesk 700 at 54 pt; speaker name + affiliation in Inter 500 at 24 pt; footer text in JetBrains Mono 400 at 14 pt.

**Layout.** 16:9 canvas; title centred vertically, 40% from top; protea left of title as a motif block.

**Accessibility check.** Cream on Indigo: AA. Pink on Indigo would be 2.39:1 and fails — do **not** use Pink text on Indigo on slides. If Pink emphasis is needed, use Pink underline or Pink inline block with Cream text.

### 8.10 Slides — content slide

**Motifs.** Indent-bars motif in top-right corner; Python mark + URL in footer zone.

**Colour proportions.** Cream background, Indigo text. This inverts the title slide deliberately — content slides read longer, and Indigo-on-Cream is the most comfortable reading pair.

**Type sizes.** Slide headline in Space Grotesk 600 at 36 pt; body bullets in Inter 400 at 24 pt; code in JetBrains Mono 400 at 20 pt minimum.

**Layout.** Headline top; content below; footer with URL + page number bottom. Generous margins — 8% of slide shortest side (so ~60 pt on a 10-inch slide).

**Accessibility check.** Indigo on Cream: 10.45:1 — AA. Code (Mono on Cream): same pairing — AA. Speakers bringing their own slides are asked to follow the same contrast rule; link to this document from the speaker handbook.

### 8.11 Slides — section divider

**Motifs.** Protea hero (40% width) + ridge silhouette + Shweshwe strip. Full motif kit, ceremonial pause.

**Colour proportions.** Indigo ground, Cream type, Pink protea.

**Type sizes.** Section title in Space Grotesk 700 at 72 pt.

**Accessibility check.** As title slide.

### 8.12 Slides — thank-you slide

**Motifs.** Indent-bars motif; Python mark + URL.

**Colour proportions.** Cream background, Indigo thank-you headline, Pink accent on URL.

**Type sizes.** "Thank you" in Space Grotesk 700 at 96 pt; URL in JetBrains Mono 500 at 28 pt.

**Layout.** Centred. Single statement, the URL, and the Python mark.

**Accessibility check.** Indigo on Cream: AA. Pink URL on Cream: 4.37:1 — AA-large only, fine at 28 pt display size.

### 8.13 Print — lanyard

**Motifs.** Indent-bars motif at top of the card area; Python mark small at bottom.

**Colour proportions.** Indigo strap, Cream card face, Indigo text.

**Type sizes.** Attendee name in Space Grotesk 600 at 22 pt; role/track in Inter 500 at 12 pt; pronouns field in Inter 400 at 10 pt.

**Layout.** Standard 90×55 mm card area; name top, role below, pronouns and any access accommodations on reverse. Lanyard strap in Indigo with wordmark repeat at 6 pt mono.

**Accessibility check.** Indigo on Cream: AA. Name readable from ~1 metre — the 22 pt name size is the minimum for that distance. **Never encode role information in lanyard colour alone.** If different role colours are used (e.g. volunteer vs speaker vs attendee), always combine with a printed text label; and pair each role with both a colour and a shape/icon for colour-vision-deficient readers.

### 8.14 Print — A2 signage

**Motifs.** Protea hero + ridge + Shweshwe strip bottom. Full kit.

**Colour proportions.** ~65% Indigo, ~25% Cream, ~10% Pink.

**Type sizes.** Directional or event signage headline in Space Grotesk 700 at 180 pt; supporting body in Inter 500 at 48 pt.

**Layout.** Wordmark top, directional content centred, footer zone with URL. Read from 3–5 metres.

**Accessibility check.** Cream on Indigo at 180 pt: AA. Arrow icons (if used) in Cream at minimum 60 pt stroke thickness.

### 8.15 Print — A5 programme booklet cover

**Motifs.** Protea hero (50% width) + ridge + Shweshwe strip along right edge + Python mark and URL footer.

**Colour proportions.** ~60% Indigo, ~25% Cream, ~10% Pink, ~5% Olive.

**Type sizes.** "PyConZA 2026" in Space Grotesk 700 at 48 pt; "Cape Town · October 2026" in Inter 500 at 18 pt; URL in JetBrains Mono 500 at 14 pt.

**Layout.** Protea dominant; wordmark top; date + location centred in lower third; Shweshwe strip as finishing edge along one side (not wrapping).

**Accessibility check.** Cream on Indigo: AA. Print on uncoated stock slightly reduces perceived contrast; specify to the printer.

### 8.16 Print — programme interior spread

**Motifs.** Indent-bars motif as section-header device. No heavy motifs in interior pages — the programme is for reading.

**Colour proportions.** Cream or Off-White background, Indigo body, Pink section headers, Olive small accents (room-code labels).

**Type sizes.** Body at 10 pt Inter 400; schedule time in 10 pt JetBrains Mono 500; talk title in 12 pt Space Grotesk 600; section header in 18 pt Space Grotesk 700 in Pink.

**Layout.** Two-column grid on A5 spread, 10 mm outer margin, 8 mm gutter, 12 mm top/bottom. Running header with page number in mono.

**Accessibility check.** Indigo on Cream body: AA. Pink headers at 18 pt meet AA-large. Minimum body at 10 pt is at the edge — print clean on white-point-matched stock, avoid low-grade recycled paper.

### 8.17 Merch — t-shirt front (motif-only)

**Motifs.** Protea hero on chest, centred, ~18–22 cm wide on an adult-size shirt. No wordmark on front. No URL on front.

**Colour proportions.** Depends on shirt colour:
- On Indigo shirt: Cream and Pink protea, Cream inner detail.
- On Cream/natural shirt: Indigo and Pink protea.
- On Off-White shirt: Indigo and Pink protea.

**Print method.** Screen print or DTG, 2–3 colour max. No 4-colour-process on merch.

**Accessibility check.** Not applicable in contrast terms; but verify the protea reads at 2-metre distance — thin stroke widths ≤1 mm tend to clog on screen print.

### 8.18 Merch — t-shirt back (wordmark)

**Motifs.** Wordmark centred on upper back, Python mark below wordmark small, URL below Python mark in mono.

**Colour proportions.** Same as front; monochrome wordmark acceptable.

**Type sizes.** Wordmark ~16 cm wide; URL in mono at ~2 cm cap height.

### 8.19 Merch — tote bag

**Motifs.** Shweshwe strip along bottom edge of the bag face; wordmark centred above strip.

**Colour proportions.** Cream or natural canvas bag, Indigo print. Single-colour print.

**Type sizes.** Wordmark ~22 cm wide; tagline "Cape Town · October 2026" in Inter 500 at 3 cm cap height below wordmark.

### 8.20 Merch — sticker set

A small sticker set as speaker/attendee giveaway. Each sticker uses one motif only.

- **Sticker 1:** Protea on Indigo circle, 60 mm diameter.
- **Sticker 2:** Ridge silhouette on Cream rectangle, 80×30 mm.
- **Sticker 3:** Shweshwe strip on Cream rectangle, 80×30 mm.
- **Sticker 4:** Python mark + "PyConZA 2026" on Indigo square, 60×60 mm.
- **Sticker 5:** Indent-bars + URL on Cream rectangle, 80×30 mm.

**Accessibility check.** Text on stickers at minimum 14 pt equivalent. Don't combine multiple motifs on one sticker — they're small enough that the rule "one hero, one grounding, one finishing" collapses to "one motif each".

---

## 9. Accessibility summary

**WCAG 2.2 AA is the baseline for every asset.** Run this checklist before shipping anything.

**Contrast.**

- Every text/background pair passes AA — 4.5:1 for body text, 3:1 for large text (24px+ or 18.66px+ bold), 3:1 for non-text UI and focus rings.
- Verify against section 3.3. If the pair is not in the passing list, change the pair or increase the size to large-text threshold.
- Protea Pink on Sandstone Cream is AA-large only. Never use it for body copy.

**Type size.**

- Body text: minimum 16 px web, 10 pt print.
- Caption text: minimum 13 px web, 9 pt print — and only for legitimate caption content.
- Line-height matches the type scale in section 4.3; don't tighten to fit.

**Alt text.**

- Every informative image has alt text. Decorative-only motifs use `alt=""` (empty) to be skipped by screen readers.
- Alt text describes the image content and purpose, not the filename. Example: `alt="Stylised geometric protea illustration in pink on deep indigo, with Table Mountain ridge silhouette beneath"`.
- For social graphics, include the full text of any copy in the image as part of the alt text or in the post body.

**Colour-blind safety.**

- **Never encode information in colour alone.** If a schedule has tracks differentiated by colour, also label the track with text. If a status is "open/closed", also use a word or icon.
- The palette was checked against common colour-vision deficiencies (deuteranopia, protanopia, tritanopia). Protea Pink and Fynbos Olive have a 1.03:1 contrast ratio and are indistinguishable to some colour-blind viewers — never pair them to convey information.
- Lanyard role-coding: colour + text label + shape/icon, minimum.

**Captions and transcripts.**

- Every recorded talk gets captions (auto-generated then human-reviewed) and a transcript.
- Every social video gets captions burnt in or as a sidecar SRT file.
- Any animated GIF or motion graphic lasting more than 3 seconds must be pausable, must not flash more than 3 times per second, and must have a still-frame alternative.

**Keyboard and focus.**

- Every interactive element on the site is reachable by keyboard.
- Focus ring is visible against every background — Cream outline on Indigo; Indigo outline on Cream; always 2 px minimum with 2 px offset.
- Skip-to-main-content link at the top of every page.

**Forms.**

- Every form input has a visible label (placeholder alone is not a label).
- Error messages use colour plus text plus icon — never colour alone.
- Required fields marked with both an asterisk and the word "required" in the field label or hint.

---

## 10. File naming, handoff, and sources

### 10.1 File-naming convention

Pattern: `pyconza2026_<asset-type>_<variant>_<size>_<date>.<ext>`

- `<asset-type>` — `logo`, `wordmark`, `social`, `slide`, `print`, `email`, `merch`, `motif`.
- `<variant>` — a short descriptor: `cfp-open`, `schedule-reminder`, `programme-cover`, `speaker-card`.
- `<size>` — dimensions or format: `1080x1080`, `1080x1920`, `a5`, `a2`, `600w`.
- `<date>` — `yyyy-mm-dd` of the file version.
- `<ext>` — `svg`, `png`, `jpg`, `pdf`, `webp`.

Examples:

- `pyconza2026_social_cfp-open_1080x1080_2026-04-12.png`
- `pyconza2026_logo_primary_svg_2026-03-01.svg`
- `pyconza2026_print_programme-cover_a5_2026-09-05.pdf`

Use hyphens inside segments, underscores between segments, lowercase throughout.

### 10.2 Source files

- **Master design files:** [to be linked]
- **Figma library:** [to be linked]
- **Logo package (SVG, PNG, monochrome):** [to be linked]
- **Motif kit (SVG):** [to be linked]
- **Slide templates (Google Slides + .pptx):** [to be linked]
- **Email templates (MJML or HTML):** [to be linked]
- **Print-ready files (PDF/X-1a):** [to be linked]

### 10.3 Additions, exceptions, and gaps

For additions to this document, exceptions to a rule, or a situation not covered here: ask the organising committee design lead [placeholder — name and contact to be filled in on publication].

**Known gaps, deferred to v1.1:**

- Sponsor logo lockups and co-branding rules (tier hierarchy, placement relative to PyConZA wordmark).
- Motion and animation specifications (easing, duration, video intro/outro templates).
- Dark-mode variants of the website palette.
- Long-form podcast cover art specifications, if relevant.

### 10.4 Versioning

| Field        | Value                              |
|--------------|------------------------------------|
| Version      | 1.0 (draft)                        |
| Issued       | 2026                               |
| Next review  | Before CFP launch                  |
| Owner        | PyConZA 2026 organising committee  |
| Contact      | [to be linked]                     |

---

## 11. Appendix A — CSS variables

Copy-paste block for the website team. Consolidates the palette and type scale.

```css
:root {
  /* Primary palette */
  --color-indigo:       #1A2B4C;
  --color-cream:        #E8DDC8;
  --color-pink:         #C2185B;
  --color-olive:        #4A6B3F;

  /* Neutral scale */
  --color-black:        #0E1420;
  --color-off-white:    #FAF6EE;
  --color-grey-700:     #3A3F47;
  --color-grey-500:     #6B7280;
  --color-grey-300:     #B9BEC6;

  /* Sanctioned Cream tint — schedule alternating rows only */
  --color-cream-tint:   #F4EEE1;

  /* Semantic aliases — prefer these over raw palette names */
  --color-bg-default:         var(--color-cream);
  --color-bg-surface:         var(--color-off-white);
  --color-bg-dark:            var(--color-indigo);
  --color-text-default:       var(--color-indigo);
  --color-text-on-dark:       var(--color-cream);
  --color-text-muted:         var(--color-grey-700);
  --color-text-disabled:      var(--color-grey-500);
  --color-accent:             var(--color-pink);
  --color-accent-secondary:   var(--color-olive);
  --color-border:             var(--color-grey-300);

  /* Typefaces */
  --font-headline: "Space Grotesk", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-body:     "Inter", system-ui, -apple-system, "Segoe UI", Roboto, sans-serif;
  --font-mono:     "JetBrains Mono", ui-monospace, "SF Mono", Consolas, monospace;

  /* Type scale — web px */
  --fs-h1:      48px;   --lh-h1:  56px;   --ls-h1:  -0.01em;
  --fs-h2:      36px;   --lh-h2:  44px;   --ls-h2:  -0.005em;
  --fs-h3:      28px;   --lh-h3:  36px;   --ls-h3:  0;
  --fs-h4:      22px;   --lh-h4:  30px;   --ls-h4:  0;
  --fs-h5:      18px;   --lh-h5:  26px;   --ls-h5:  0.02em;
  --fs-h6:      14px;   --lh-h6:  22px;   --ls-h6:  0.06em;
  --fs-body:    16px;   --lh-body: 26px;  --ls-body: 0;
  --fs-body-l:  18px;   --lh-body-l: 30px;
  --fs-small:   14px;   --lh-small: 22px;
  --fs-caption: 13px;   --lh-caption: 20px;
  --fs-mono:    15px;   --lh-mono: 24px;

  /* Weights */
  --fw-regular: 400;
  --fw-medium:  500;
  --fw-semi:    600;
  --fw-bold:    700;

  /* Spacing scale — 4px base */
  --sp-1: 4px;
  --sp-2: 8px;
  --sp-3: 12px;
  --sp-4: 16px;
  --sp-5: 24px;
  --sp-6: 32px;
  --sp-7: 48px;
  --sp-8: 64px;
  --sp-9: 96px;

  /* Grid */
  --grid-cols-mobile:  4;
  --grid-cols-tablet:  8;
  --grid-cols-desktop: 12;
  --gutter-mobile:  16px;
  --gutter-tablet:  24px;
  --gutter-desktop: 24px;
  --margin-mobile:  16px;
  --margin-tablet:  32px;
  --margin-desktop: 48px;
  --max-content:    1440px;

  /* Focus ring */
  --focus-ring-width: 2px;
  --focus-ring-offset: 2px;
  --focus-ring-on-light: var(--color-indigo);
  --focus-ring-on-dark:  var(--color-cream);
}

/* Example usage */
body {
  background: var(--color-bg-default);
  color: var(--color-text-default);
  font-family: var(--font-body);
  font-size: var(--fs-body);
  line-height: var(--lh-body);
}
h1 {
  font-family: var(--font-headline);
  font-size: var(--fs-h1);
  line-height: var(--lh-h1);
  letter-spacing: var(--ls-h1);
  font-weight: var(--fw-bold);
}
code, .mono {
  font-family: var(--font-mono);
  font-size: var(--fs-mono);
}
:focus-visible {
  outline: var(--focus-ring-width) solid var(--focus-ring-on-light);
  outline-offset: var(--focus-ring-offset);
}
```

---

*End of PyConZA 2026 Brand Guidelines v1.0 (draft).*