# PHI Fiduciaire — Brand & Design Style Guide
*Version 1.0 — March 2026 — Living document, updated as project evolves*

---

## 1. Brand Identity

**Name:** PHI Fiduciaire
**Location:** Geneva, Switzerland
**Positioning:** Premium Swiss fiduciary — rigorous, local, multilingual
**Tagline pairing:** "La rigueur suisse. *L'expertise genevoise.*"
**Symbol:** φ (phi) — the golden ratio. Used as ghost texture on dark sections (560px, 2.5% opacity). The name itself encodes the design system.

---

## 2. Color Palette

| Name | Hex | Usage |
|---|---|---|
| Primary (teal) | `#1b3f3f` | Main brand color — nav, headings, dark sections |
| Footer dark | `#0f2626` | Darkest teal — footer, nav logo row, bottom hero band |
| Accent (red) | `#ef3a24` | Sparingly — max 2–3 per viewport. Labels underline, card top rule, open FAQ border |
| White | `#ffffff` | Text on dark, button fill, card backgrounds |
| Off-white | `#f8f6f2` | Page background, blog section background |
| Border | `rgba(27,63,63,0.12)` | Card borders, dividers |

**Red discipline:** Never use red as a fill or background. Only as a 2px or 3px line/rule. The eye should find it as a punctuation mark, not a block.

---

## 3. Typography

### Typefaces
| Role | Font | Source |
|---|---|---|
| Display / Headings | Cormorant Garamond | Google Fonts |
| Body / UI | DM Sans | Google Fonts |

### Type Scale
| Element | Size | Weight | Font | Notes |
|---|---|---|---|---|
| H1 hero | `clamp(52px, 6vw, 80px)` | 400 | Cormorant Garamond | Light, editorial |
| H1 italic line | `clamp(44px, 5.5vw, 70px)` | 400 italic | Cormorant Garamond | Second line of hero |
| H2 section | `clamp(36px, 4vw, 56px)` | 400 | Cormorant Garamond | |
| H3 card title | `20–22px` | 500 | DM Sans | |
| Body | `16–17px` | 400 | DM Sans | Line height 1.7 |
| Label / eyebrow | `11px` | 400 | DM Sans | Uppercase, letter-spacing 0.12em |
| Nav links | `13px` | 400 | DM Sans | Uppercase, letter-spacing 0.08em |
| CTA button | `11–12px` | 500 | DM Sans | Uppercase, letter-spacing 0.12em |

### Label Style (used across all sections)
```
text-transform: uppercase;
letter-spacing: 0.12em;
font-size: 11px;
color: var(--color-primary) or rgba(255,255,255,0.65) on dark
```
Every label has a **34px × 2px red line** below it (`::after` pseudo-element).

---

## 4. Spacing System — PHI / Fibonacci Scale

The entire layout uses a single spacing vocabulary derived from the Fibonacci sequence.

| Token | Value | Use |
|---|---|---|
| `--space-xs` | 13px | Tight inline gaps |
| `--space-sm` | 21px | Small internal padding |
| `--space-md` | 34px | Standard component gap |
| `--space-lg` | 55px | Section internal padding |
| `--space-xl` | 89px | Section vertical padding |
| `--space-xxl` | 144px | Large section padding |
| `--space-hero` | 233px | Hero padding |

**Navigation (mobile) — Fibonacci bands:**
| Band | Height |
|---|---|
| Logo row (dark teal) | 34px |
| Controls row (white) | 55px |

**Hero bottom bands (mobile):**
| Band | Height |
|---|---|
| Teal band | 55px |
| Footer dark band | 34px |

The palindrome reads: **34 / 55 / photo / 55 / 34** — top mirrors bottom.

---

## 5. Container & Layout

- **Max content width:** 1380px (widened from 1280px for breathing room on large screens)
- **Horizontal padding:** `var(--space-md)` (34px) on mobile, auto on desktop
- **Grid system:** CSS Grid, no framework
- **Section padding:** `var(--space-xl)` (89px) vertical by default; `var(--space-xxl)` (144px) for hero and major CTAs

---

## 6. Image Treatment

### Desktop Hero — Left-to-right gradient
- **Colour photo, no desaturation**
- Two overlay layers via `::before` (colour tint) and `::after` (gradient):
  - Left → right: `rgba(27,63,63,0.96)` at 0% → solid 20% → fades to transparent at 75%
  - Bottom: subtle gradient for text legibility
- Content sits in the solid left zone

### Mobile Hero — Top-to-bottom overlay
```
0–50%:  pure photo (transparent)
50–80%: gradient fading to 95% teal opacity
80%:    HARD CUT → solid main teal #1b3f3f
85%:    HARD CUT → solid footer dark #0f2626 (34px band)
```

### Pricing Teaser — Left-to-right gradient on image
- Left 15%: solid footer color `#0f2626` — hard vertical cut
- Then gradient: dark left → transparent right
- Keeps image visible on right 40%

### Blog Cards & Duotone sections
```css
img { mix-blend-mode: luminosity; filter: grayscale(60%) brightness(1.1); }
::before { background: linear-gradient(150deg, #2a6565, #1b3f3f); mix-blend-mode: color; opacity: 0.50; }
```

### Hard cut technique (CSS)
To create a perfectly sharp colour boundary with no feathering:
```css
/* Same percentage repeated = zero transition distance = hard cut */
rgba(27,63,63,1.00) 80%,
rgba(15,38,38,1.00) 80%
```

---

## 7. Navigation

### Desktop
- Transparent on hero, becomes `#1b3f3f` on scroll
- Logo: **PHI** (Cormorant Garamond, 24px) + FIDUCIAIRE (DM Sans, 11px, letter-spacing 0.2em)
- Links: uppercase, 13px, white 75% opacity
- CTA button: outlined white, right side
- Total height: 80px

### Mobile — Two-tone header
| Row | Color | Height | Content |
|---|---|---|---|
| Top | `#0f2626` (footer dark) | 34px | Logo centered |
| Bottom | `#ffffff` (white) | 55px | Hamburger left + CTA button right |

---

## 8. UI Components

### Buttons
| Type | Style |
|---|---|
| Primary (on light) | Outlined teal, uppercase, 11px, letter-spacing 0.12em, padding 16px 34px |
| Primary (on dark) | Outlined white — same specs |
| Ghost / Secondary | Transparent, white border 40% opacity |
| CTA hero | Solid white fill, teal text — only used for the main hero CTA |

Button border-radius: **0** (no rounding — Swiss precision aesthetic).

### Labels / Eyebrows
- Always uppercase, 11px, DM Sans
- Always followed by a `34px × 2px` red line (`::after { width: 34px; height: 2px; background: #ef3a24; display: block; margin-top: 6px; }`)
- On centered sections: add `margin: 6px auto 0` to center the red line

### Cards
- Border-top: `1px solid rgba(27,63,63,0.12)`
- Red top accent: `2px × 34px` red rule before title
- No box shadow, no border-radius
- Padding: `var(--space-md)` top, `var(--space-xl)` bottom

### FAQ Accordion
- `+` / `−` toggle (no circle, plain character, 22px, weight 300)
- Open item: `2px solid #ef3a24` left border
- Open question: `font-weight: 500`
- Max-height animation: `0 → 500px`

### Ghost φ Texture
Used on the Final CTA dark section:
```css
content: 'φ';
font-size: 560px;
font-family: Cormorant Garamond;
color: rgba(255,255,255,0.025);
position: absolute;
right: -1%;
bottom: -10%;
pointer-events: none;
```

---

## 9. Section-by-Section Visual Language

| Section | Background | Key technique |
|---|---|---|
| Hero | Full-bleed photo | Left gradient desktop / top gradient mobile |
| Accent bar | 3px solid `#ef3a24` | Separates hero from content |
| Services | `#f8f6f2` off-white | Ghost numbers (large Cormorant), card grid |
| Why PHI | White | 40/60 header grid, 3-col card grid, red top rules |
| Pricing Teaser | Full-bleed photo | Left dark hard cut + gradient, left-anchored content |
| Local SEO | White | 2-col: rich copy left, map card + NAP right |
| FAQ | `#f8f6f2` off-white | Accordion, red left border on open |
| Blog | `#f8f6f2` off-white | 3-col cards, teal duotone on images |
| Final CTA | Full-bleed photo (landscape) | Left gradient, ghost φ, single CTA button |
| Footer | `#0f2626` footer dark | 4-col grid, brand + services + NAP + legal |

**Rule:** No two adjacent sections use the same visual technique or background colour.

---

## 10. Photography Style

- **Preferred subjects:** Architecture (spiral stairs, stone buildings), Geneva waterscapes, professional office scenes
- **Colour treatment:** Either full colour with teal overlay gradient, OR partial duotone (teal)
- **Avoid:** Stock-looking posed handshakes, generic office photos, blue-tinted corporate imagery
- **PHI brand photo assets:** `phi-stairs*.jpeg/jpg`, `water.jpg`, `Fiduciare-69.jpg`, `bernd-dittrich-*.jpg`

---

## 11. Design Principles

1. **Swiss precision** — no unnecessary decoration, every element earns its place
2. **Controlled red** — max 2–3 red accents per viewport, never as fill
3. **Generous whitespace** — sections breathe; use `--space-xl` minimum vertical padding
4. **No repeated patterns** — each section has its own visual signature
5. **Golden ratio proportions** — spacing, band heights, and layouts derived from φ = 1.618
6. **Typography contrast** — Cormorant (editorial, human) paired with DM Sans (precise, functional)
7. **Image fidelity** — photos keep their colour; overlays are directional, not washing
8. **Hard cuts over gradients** for structural colour changes; gradients only for photo-to-colour transitions

---

## 12. Social & Marketing Assets — Application Rules

When creating carousels, GMB posts, or ads using this system:

- **Background options:** `#1b3f3f`, `#0f2626`, `#f8f6f2`, or photo with teal overlay
- **Never use red as background** — only as 2–3px line
- **Typography on dark:** White Cormorant Garamond headline + white DM Sans body
- **Typography on light:** `#1b3f3f` headline, `rgba(27,63,63,0.70)` body
- **Always include:** label eyebrow (uppercase, 11px) + red 34px underline
- **Image ratio for carousels:** 1:1 or 4:5, full bleed with left or bottom gradient
- **Minimum font sizes:** 11px label, 16px body, 28px+ headline
- **The φ symbol** can be used as a watermark/texture on dark backgrounds at very low opacity

---

*This document is a living brief. Update it as new sections, images, or design decisions are added to the PHI Fiduciaire project.*
