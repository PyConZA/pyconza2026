# PyConZA 2026 Rebrand — Execution Plan

## Context

The PyConZA 2026 site (Django + Tailwind v4) is currently styled with a legacy palette: yellow/green/blue/red brand colours, generic gradients, gray-700 header, mixed weights and headings. A new 2026 brand identity has been defined across seven brand skills in `.claude/skills/` (`brand-colors`, `brand-css-tokens`, `brand-typography`, `brand-layout`, `brand-voice`, `brand-positioning`, `brand-accessibility`). The goal of this plan is to bring every active surface (templates, CSS, copy) onto the new brand without breaking layout or accessibility.

This plan is written to be executed step-by-step by fresh agents that will not have the conversation history. Each step is self-contained: it lists the files to read, the files to edit, the brand skills to load, and how to validate. **Run phases in order** — later phases assume earlier ones are merged. Human validation gates are interleaved.

**Rule for every phase:** load the named brand skill(s) before editing. The skills are the source of truth for hexes, type scale, breakpoints, voice rules, and accessibility floors. Do not duplicate their content into this plan.

---

## File map — what gets touched

**Foundational (changes ripple everywhere):**
- `static/css/main.css` — Tailwind v4 `@theme` block, `@layer base`, `@layer components`, `@layer utilities`
- `templates/_base.html` — `<head>` (fonts), header, footer
- `templates/wafer/base.html` — minimal extender; usually no edits
- `templates/partial_header.html` — logo + nav container
- `templates/wafer/nav.html` — desktop nav, mobile hamburger, dropdown

**High-impact pages:**
- `templates/website/page_home.html`
- `templates/website/page_beginners_day.html`
- `templates/website/page_in_person_event.html`
- `templates/website/page_sprints.html`
- `templates/website/page_donations.html`
- `templates/website/page_remote_experience.html`
- `templates/website/page_volunteering.html`
- `templates/website/page_dinner.html`
- `templates/website/page_tickets.html`

**Form / list pages:**
- `templates/visa/visa_letter_form.html`, `visa_letter_detail.html`
- `grants/templates/grants/application_form.html`, `application_detail.html`
- `templates/accommodations/accommodation_recommendations.html`

**Markdown / wafer:**
- `templates/wafer.pages/page.html` (renders markdown content)
- Markdown sources in `pages_md/` — content edits only if voice pass needs them.

---

## Phase 1 — CSS foundation: tokens, fonts, base layer (AI)

**Goal:** Replace the brand layer in `static/css/main.css` so every existing utility class downstream picks up the new palette and type without further edits.

**Skills to load:** `brand-css-tokens` (primary), `brand-colors`, `brand-typography`.

**Files to edit:** `static/css/main.css` only.

**Decision before starting:** legacy `pycon-yellow/green/blue/red` tokens — keep as deprecated aliases that map to new tokens (default, lets Phases 2–7 land without breakage), or remove now and replace every usage as part of those phases. Mark choice: `[KEEP-AS-ALIAS / REMOVE-NOW]`.

**What to do:**

1. Read `static/css/main.css` end-to-end and the `brand-css-tokens` skill.
2. Replace the `@theme` block so it exposes the full new palette and type stacks as Tailwind v4 theme tokens (colour names and font names per `brand-css-tokens`). This makes utility classes like `bg-indigo`, `text-cream`, `font-headline` available downstream.
3. **Per the alias decision:** if KEEP-AS-ALIAS, also expose temporary `--color-pycon-*` aliases mapped per the table below. If REMOVE-NOW, omit them.

   | Legacy | New |
   |---|---|
   | yellow | pink |
   | green | olive |
   | blue | indigo |
   | red | pink |
   | light-blue | cream |

4. Replace `@layer base` `:root` font variables with the new font stacks from `brand-typography`. Drop Kanchenjunga and Open Sans entirely.
5. Update the element-level rules so headings use the headline stack and body elements use the body stack. Update each `h1..h6` `@apply` block to match the brand type scale (see `brand-typography`). Use mobile-first sizes that step up at `lg:` to the desktop scale.
6. Replace heading colour utilities (`text-gray-900` etc.) with `text-indigo`.
7. Add a `body { @apply bg-cream text-indigo font-body; }` rule in `@layer base`.
8. Keep the default `a` styling (underline + cursor). Add focus-visible: `a:focus-visible { @apply outline-2 outline-offset-2 outline-indigo; }`. Also add focus-visible rules for `input`, `textarea`, `select`.
9. Update `@layer components` to use brand tokens — semantic mappings:
   - `.btn` → indigo bg / cream text / pink focus ring
   - `.btn-success` → olive
   - `.btn-secondary` → pink (the accent CTA)
   - `.nav-item` → cream text, pink hover
   - `.alert-primary` → cream + indigo border
   - `.alert-danger` / `.bg-danger` → pink border, cream-tint fill (pink is the destructive accent — there is no red in this palette)
   - `.alert-warning` → olive border, cream-tint fill
   - `.alert-success` → olive border, off-white fill
   - `.alert-info` → indigo border, off-white fill
   - `.card` → off-white bg, grey-300 border, rounded
   - `.badge` → grey-300 border, indigo text, cream-tint bg
   - `.django-markitup-widget` → off-white bg, indigo text, grey-300 border
10. Legacy `.text-pycon-*` / `.bg-pycon-*` utilities in `@layer utilities`:
    - KEEP-AS-ALIAS: redirect each to the new token. Cover both `text-` and `bg-` variants since templates use `bg-pycon-blue/10` etc.
    - REMOVE-NOW: delete; later phases replace every usage.
11. Update `.bg-translucent` to use indigo with a backdrop blur. Leave `.fa-bluesky` alone.

**Validation (AI):**
- Rebuild Tailwind. No build errors. Unknown-class errors usually mean a token wasn't exposed in `@theme` — re-check step 2.

**Validation (HUMAN):**
- [ ] Visit `/`, `/sprints`, `/beginners-day`, `/donations`. Cream background, indigo body text, indigo buttons with cream text, headline font visibly distinct from body.
- [ ] No invisibly low-contrast text. Check the forbidden pair (Pink + Olive) and the AA-large-only rule (Pink on Cream) per `brand-colors`.
- [ ] Mobile / tablet / desktop scale correctly. Body stays ≥16px.
- [ ] If structural breakage (collapsed layouts, missing nav), pause and brief the next AI step.

---

## Phase 2 — Base templates: head, header, footer, nav (AI)

**Goal:** Update the structural shell so every page inherits the new look.

**Skills to load:** `brand-typography`, `brand-layout`, `brand-colors`, `brand-accessibility`.

**Files to edit:**
- `templates/_base.html`
- `templates/partial_header.html`
- `templates/wafer/nav.html`
- (Read but probably don't edit) `templates/wafer/base.html`

**What to do:**

1. **`_base.html` `<head>`:** add Google Fonts preconnect + stylesheet for the three brand families and weights specified in `brand-typography`. Remove leftover Kanchenjunga / Open Sans `<link>` tags or local `@font-face` references (search `static/css/`).
2. **Header:** `<header class="bg-gray-700">` → `<header class="bg-indigo">`. Cream-on-indigo passes AA.
3. **Footer:** prefer `bg-indigo text-cream` (matches brand's indigo-dominant proportion). Sponsor logos sit on off-white/cream cards with padding (transparent logos disappear on indigo otherwise). Social icons `text-cream hover:text-pink`. Copyright line `text-grey-300 text-sm`.
4. **`partial_header.html`:** keep structure. If the logo is dark-on-transparent it'll vanish on indigo — flag to the user and request a cream-on-indigo variant; do not silently invert.
5. **`wafer/nav.html`:** verify desktop nav uses the `.nav-item` class. Mobile hamburger gets `focus-visible` cream ring. Mobile dropdown panel `bg-indigo border border-grey-700` with cream items. Same treatment for the user dropdown.
6. **Skip-to-main-content link:** add as the first child of `<body>` in `_base.html`. Add `id="main"` to the `<main>` element (or wrap `{% block content %}` if no `<main>` exists).

**Validation (HUMAN):**
- [ ] Header indigo, nav cream, hover pink. Footer as decided.
- [ ] Tab from URL bar — skip link appears first, every nav link gets a visible cream focus ring.
- [ ] Mobile hamburger opens an indigo dropdown with cream readable text.
- [ ] Logo visible. If not, flag for next AI step.

---

## Phase 3 — Home page (AI)

**Goal:** The highest-visibility surface, fully on-brand.

**Skills to load:** `brand-positioning`, `brand-layout`, `brand-colors`, `brand-typography`, `brand-voice`.

**File to edit:** `templates/website/page_home.html`.

**What to do:**

1. Read the file fully and the `brand-positioning` skill.
2. **Hero:** background `bg-indigo`. Hero image (if any) layered with `bg-translucent` for text scrim. Headline cream, sub-copy cream/off-white. CTAs: one primary `.btn` and at most one `.btn-secondary` — pick **one** pink hit per surface.
3. **Below the fold:** alternate cream (page) and off-white (cards). Replace `bg-gradient-to-br from-pycon-*` blocks with flat `bg-off-white border border-grey-300`. Brand forbids gradients between brand colours (see `brand-colors`).
4. **Dates / URLs:** wrap in `font-mono`.
5. **Voice pass** on hero copy per `brand-voice`. Confirm "Cape Town, South Africa" on first mention, "Cape Town" thereafter.
6. Remove arbitrary inline colour values (`text-[#FFD700]` etc.) — always use brand tokens.

**Validation (HUMAN):**
- [ ] Mobile / tablet / desktop. Reads "coastal, considered, adult" — indigo dominant, cream breathing room, one pink focal hit, sparse olive (proportions per `brand-colors`).
- [ ] Read every word; flag marketing-email phrasing for Phase 8.
- [ ] Contrast-check hero headline + sub-copy against `brand-accessibility` floors.
- [ ] Sparse-feeling wide-screen layouts are intentional — verify against `brand-layout` whitespace philosophy before tightening.

---

## Phase 4 — Content pages, batch A: beginners-day, in-person, sprints (AI)

**Goal:** The three heaviest pages — most legacy colours and gradient cards live here.

**Skills to load:** `brand-colors`, `brand-layout`, `brand-typography`, `brand-voice`.

**Files to edit (in order):**
1. `templates/website/page_beginners_day.html`
2. `templates/website/page_in_person_event.html`
3. `templates/website/page_sprints.html`

**What to do (per file):**

1. Replace legacy colour utilities per the alias table in Phase 1. If a page ends up with six pink callouts, keep one and demote the rest to indigo or olive — the 60/25/10/5 proportion in `brand-colors` is binding.
2. Flatten gradients: `bg-gradient-to-* from-X/10 to-Y/10` → `bg-off-white border border-grey-300`.
3. Status / level badges: success/easy → olive tint, info/intermediate → indigo tint, advanced/hot → pink tint. Keep badge shape.
4. Workshop logos sit on off-white/white cards with padding — never on indigo if transparent.
5. Section dividers: alternate cream / off-white. At most one indigo section per page. Olive only for thin dividers.
6. Hover effects (`hover:scale-105 transition-transform`) are fine; transitions ≤300ms (project CLAUDE.md).
7. Voice pass per `brand-voice`. Beginners-day especially has marketing-tone copy.

**Validation (HUMAN):**
- [ ] Each page at mobile / tablet / desktop. Indigo / cream / off-white dominant, ≤10% pink, ~5% olive.
- [ ] No gradients remain.
- [ ] No pink-on-cream small text, no pink-on-olive adjacency.
- [ ] Spot-check contrast on one body paragraph and one badge per page.

---

## Phase 5 — Content pages, batch B: donations, remote, volunteering, dinner, tickets (AI)

**Skills to load:** `brand-colors`, `brand-layout`, `brand-typography`, `brand-voice`.

**Files to edit:**
- `templates/website/page_donations.html`
- `templates/website/page_remote_experience.html`
- `templates/website/page_volunteering.html`
- `templates/website/page_dinner.html`
- `templates/website/page_tickets.html`

**What to do:** apply Phase 4 substitutions. Page-specific notes:
- `page_donations.html`: yellow alert blocks → cream + grey-300 border. The "give" CTA is the natural pink moment.
- `page_remote_experience.html`: dark Discord-ish block → `bg-indigo text-cream`.
- `page_volunteering.html`: role-card icon circles — pick **two** brand colours for visual rhythm, not three.
- `page_dinner.html`: gradient block → flat off-white. Italic blockquote is fine (genuine emphasis per `brand-voice`).
- `page_tickets.html`: short page; voice-pass placeholder copy.

**Validation (HUMAN):**
- [ ] Each URL. Same checklist as Phase 4. Spot-check on a real phone if possible.

---

## Phase 6 — Forms and authenticated pages: visa, grants (AI)

**Goal:** Forms are brand-critical. Crispy Forms emits markup; Tailwind only keeps classes it sees, so the class-list comment in `_base.html` matters.

**Skills to load:** `brand-colors`, `brand-typography`, `brand-accessibility` (forms section), `brand-voice`.

**Files to read first:**
- `templates/_base.html` (find the Crispy Forms class-list comment)
- `templates/visa/visa_letter_form.html`
- `templates/visa/visa_letter_detail.html`
- `grants/templates/grants/application_form.html`
- `grants/templates/grants/application_detail.html`

**What to do:**

1. **Crispy class-list comment:** swap `border-gray-300 bg-white text-gray-700` patterns to brand equivalents. Add focus-visible classes there too — without them in the comment, Tailwind purges them.
2. Visible `<label>` per field (Crispy default). Never placeholder-only labels.
3. Required-field marker: `*` plus the word "required" per `brand-accessibility`. Flag (don't fix) if Crispy needs an override.
4. Error states: pink fill/border/text plus an icon — never colour alone (`brand-accessibility`).
5. Status badges in `visa_letter_detail.html`:
   - approved → olive
   - pending → cream-tint + indigo + grey-300
   - rejected / permanently rejected → pink
6. `application_detail.html`: read-only display. Section headings H3.
7. Voice pass on form copy and helper text.

**Validation (HUMAN):**
- [ ] Log in, visit `/visa_letters/` and `/opportunity_grants/`. Tab through inputs — indigo focus ring visible.
- [ ] Submit an invalid form — error uses pink + text + icon, never colour alone.
- [ ] Detail pages: status badges read clearly.

---

## Phase 7 — Lists, accommodations, markdown pages (AI)

**Skills to load:** `brand-colors`, `brand-layout`, `brand-typography`.

**Files to edit:**
- `templates/accommodations/accommodation_recommendations.html`
- `templates/wafer.pages/page.html`

**What to do:**

1. **Accommodations cards:**
   - Surface: off-white + grey-300 border + softer shadow (heavy shadows look bad on cream).
   - Discount-code highlight: olive tint.
   - Pagination active → indigo + cream; inactive → grey-300 border, indigo on hover.
   - Amenity badges → cream-tint + indigo + grey-300, rounded-full.
2. **Markdown page template:**
   - Wrap rendered content in a constrained-width container. If `@tailwindcss/typography` isn't installed (check `package.json`), define a `.markdown-body` class in `static/css/main.css` `@layer components` covering `h1..h6, p, ul, ol, blockquote, code, pre`. Ensure `code` uses `font-mono` and the measure stays ≤72ch (`brand-layout`).
   - Wrapper element: `<main id="main" class="max-w-prose mx-auto px-4 py-8 markdown-body">{{ page.cached_render|safe }}</main>`.
   - Admin "edit / compare" buttons inherit `.btn` updates from Phase 1.

**Validation (HUMAN):**
- [ ] `/accommodations` cards readable, hover subtle, pagination on-brand.
- [ ] `/pages/about_us/`, `/pages/code_of_conduct/`, `/pages/speaking_guidelines/` — body ≥16px, sane measure, headings styled, code blocks in mono.

---

## Phase 8 — Voice & copy pass (AI, with HUMAN review)

**Goal:** Palette correct ≠ copy correct. Scrub every active template and markdown source for voice violations.

**Skills to load:** `brand-voice` (primary), `brand-positioning`.

**Files to read (review pass — don't edit yet):**
- All `templates/website/page_*.html`
- All `pages_md/**/*.md`

**What to do:**

1. Grep across the project for the avoid-list terms in `brand-voice` (the skill is the source of truth — don't reproduce the list here).
2. For each hit, propose a rewrite per `brand-voice` examples. **Do not commit copy changes silently** — produce a single diff-style summary at `static/REBRAND_COPY_NOTES.md` listing every hit with a proposed replacement, then ask the user to approve.
3. Markdown files in `pages_md/` are loaded into the DB via `load_md_content.py` — content edits require running that command after merging. Note this in the summary.
4. Spot-check inclusivity (gendered language, idioms, unspelled acronyms).
5. First-mention rule: "Cape Town, South Africa" on first mention per page, "Cape Town" thereafter. Pick one date format per surface.

**Validation (HUMAN):**
- [ ] Read `static/REBRAND_COPY_NOTES.md`. Approve / edit / reject each rewrite. A follow-up AI pass commits the approved edits.

---

## Phase 9 — Final accessibility audit (AI + HUMAN)

**Skills to load:** `brand-accessibility` (run the full pre-ship checklist).

**AI tasks:**
1. Automated contrast scan against the dev server (e.g. `pa11y` if available) for all active routes. Report failures with file/line context.
2. Grep for any remaining off-palette colour usages: `grep -rE "(bg|text|border)-(red|orange|yellow|green|blue|indigo|purple|pink|gray)-[0-9]+" templates/ static/css/ grants/`. Each hit should be a deliberate Tailwind grey, or a leftover to replace with a brand token.
3. Verify focus rings on every interactive element (tab through, or describe a keyboard test for the human).
4. Verify all `<img>` tags have `alt` (`grep -rEn "<img[^>]*>" templates/ | grep -v "alt="` should be zero hits, or every hit is intentionally `alt=""`).
5. Verify body text ≥16px per `brand-typography` (search `text-xs`, `text-sm` and confirm uses are non-body — captions, badges).

**HUMAN tasks:**
- [ ] Walk the `brand-accessibility` checklist on each page.
- [ ] Test with at least one screen reader on `/` and `/visa_letters/`.
- [ ] DevTools → Rendering → Emulate vision deficiencies. Cycle protanopia / deuteranopia / tritanopia / achromatopsia. No information lost.

---

## Phase 10 — Cleanup & alias removal (AI)

**Goal:** If Phase 1 chose KEEP-AS-ALIAS, remove the legacy `pycon-*` tokens now that all templates have migrated.

**Skills to load:** `brand-css-tokens`.

**What to do:**
1. Grep for remaining `pycon-yellow|pycon-green|pycon-blue|pycon-red|pycon-light-blue` usages across `templates/`, `grants/`, `accommodations/`, `visa/`, `static/`. Should be zero.
2. If zero, delete the alias rules from `static/css/main.css` (`@theme` legacy entries and `@layer utilities` `.text-pycon-*` / `.bg-pycon-*` rules).
3. Rebuild Tailwind.

**Validation (HUMAN):**
- [ ] Smoke-test all pages. Build size should drop slightly.

---

## Notes for fresh agents executing this plan

- **Always load the relevant brand skill** at the start of a phase. The skills are the source of truth for hexes, type scale, breakpoints, voice rules, and accessibility floors. Do not duplicate their content into commits or PR descriptions — link or reference instead.
- **Never** introduce a new colour, font, or gradient that isn't sanctioned by the brand. If a design choice isn't covered, ask the user.
- **Tailwind v4 specific:** colour and font tokens live in `@theme` in `static/css/main.css`. Adding a token means adding a `--color-X` / `--font-X` line there, not extending `tailwind.config.js` (the project doesn't use one).
- **If a phase reveals scope** the plan didn't anticipate (e.g. hardcoded inline `style="..."` colours), stop and report rather than improvising.
- **Test responsiveness in the dev server**, not just by reading code. Type-check / build success ≠ visual correctness — `CLAUDE.md` is explicit on this.
- **Static files:** if a CSS edit doesn't appear in the browser, check whether Tailwind is rebuilding and whether Django's static-file collection needs re-running.
