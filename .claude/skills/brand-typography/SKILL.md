---
name: brand-typography
description: PyConZA 2026 type system — Space Grotesk (headline), Inter (body), JetBrains Mono. Web/print type scale, line-heights, letter-spacing, pairing rules, and don'ts. Use when setting headings, body copy, or code in any medium.
---

# Typography

All three typefaces are free, open-source, and available on Google Fonts. License: SIL Open Font License 1.1 for all three.

## The three roles

| Role     | Typeface        | Why |
|----------|-----------------|-----|
| Headline | **Space Grotesk** | Contemporary geometric sans with slightly condensed proportions and a confident, slightly quirky character — reads as modern without feeling corporate. Committed choice; do not substitute. |
| Body     | **Inter**        | Highly legible humanist sans designed specifically for UI and extended reading at small sizes. Excellent hinting on low-DPI screens, broad language support including the African language diacritics we may need. |
| Mono     | **JetBrains Mono** | Modern monospace with high legibility at small sizes, clear disambiguation of `0/O`, `1/l/I`, and `rn/m`. Used for dates, URLs, numeric callouts, and code. |

## Web loading

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

## Type scale

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
| Mono   | URLs, dates, code      | 15     | 24 (1.60)       | 0              | 400    | 10       | JetBrains Mono |

**Minimums:** body never below 16px on web or 10pt in print.

## Pairing rules

- Every page/surface uses at most these three typefaces. Do not introduce a fourth.
- Headlines and body come from Space Grotesk and Inter respectively; do not swap — Inter is not a headline face at 48px, and Space Grotesk at 16px for body is tiring to read.
- Monospace is for dates, URLs, numeric callouts (e.g. "2026", "Day 2, Track 3"), and any actual code. It is not a decorative display face.
- For the Protea Pink contrast rule (see the brand-colors skill): Pink headlines must be 24px+ or 18.66px+ bold to pass AA-large on Cream.

## Don'ts

Do not:

- Substitute Space Grotesk with Futura, Avenir, Montserrat, Poppins, or other "near enough" geometrics. The choice is specific.
- Set body copy in all-caps. Reserve uppercase for H6 labels and the rare short eyebrow.
- Letter-space body copy (0 is correct). Only display sizes and uppercase labels use tracking.
- Use italic as a stylistic flourish. Italic is for titles of works and genuine emphasis only.
- Underline text except for links.
- Justify body copy. Left-align (ragged right) in English.
