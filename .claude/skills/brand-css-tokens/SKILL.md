---
name: brand-css-tokens
description: PyConZA 2026 CSS custom-property block — palette, neutral scale, semantic colour aliases, typeface stacks, type scale, weights, spacing scale, grid, and focus-ring tokens. Use when implementing the brand in code on the conference website or any web surface.
---

# Appendix A — CSS variables

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
