---
name: brand-accessibility
description: PyConZA 2026 WCAG 2.2 AA pre-ship checklist — contrast, type sizes, alt text, colour-blind safety, motion, keyboard/focus, forms. Use as a final accessibility check before publishing any asset (web, social, slides, print).
---

# Accessibility summary

**WCAG 2.2 AA is the baseline for every asset.** Run this checklist before shipping anything.

## Contrast

- Every text/background pair passes AA — 4.5:1 for body text, 3:1 for large text (24px+ or 18.66px+ bold), 3:1 for non-text UI and focus rings.
- Verify against the contrast matrix in the brand-colors skill. If the pair is not in the passing list, change the pair or increase the size to large-text threshold.
- Protea Pink on Sandstone Cream is AA-large only. Never use it for body copy.

## Type size

- Body text: minimum 16 px web, 10 pt print.
- Line-height matches the type scale in the brand-typography skill; don't tighten to fit.

## Alt text

- Every informative image has alt text. Decorative-only motifs use `alt=""` (empty) to be skipped by screen readers.
- Alt text describes the image content and purpose, not the filename. Example: `alt="Stylised geometric protea illustration in pink on deep indigo, with Table Mountain ridge silhouette beneath"`.
- For social graphics, include the full text of any copy in the image as part of the alt text or in the post body.

## Colour-blind safety

- **Never encode information in colour alone.** If a schedule has tracks differentiated by colour, also label the track with text. If a status is "open/closed", also use a word or icon.
- The palette was checked against common colour-vision deficiencies (deuteranopia, protanopia, tritanopia). Protea Pink and Fynbos Olive have a 1.03:1 contrast ratio and are indistinguishable to some colour-blind viewers — never pair them to convey information.
- Lanyard role-coding: colour + text label + shape/icon, minimum.

## Motion

- Any animated GIF or motion graphic lasting more than 3 seconds must be pausable, must not flash more than 3 times per second, and must have a still-frame alternative.

## Keyboard and focus

- Every interactive element on the site is reachable by keyboard.
- Focus ring is visible against every background — Cream outline on Indigo; Indigo outline on Cream; always 2 px minimum with 2 px offset.
- Skip-to-main-content link at the top of every page.

## Forms

- Every form input has a visible label (placeholder alone is not a label).
- Error messages use colour plus text plus icon — never colour alone.
- Required fields marked with both an asterisk and the word "required" in the field label or hint.
