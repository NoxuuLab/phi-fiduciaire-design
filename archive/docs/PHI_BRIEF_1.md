# PHI Fiduciaire — Claude Design Brief
> Paste this at the start of every Claude session this weekend.

---

## 1. MISSION

Build a high-fidelity HTML/CSS prototype of the PHI Fiduciaire website.
Single HTML file per page. No framework. Pure HTML + CSS + vanilla JS.
Target: elegant, airy, premium Swiss fiduciaire. Designed for transposition into WordPress/Elementor.

---

## 2. BRAND IDENTITY

**Company:** PHI Fiduciaire
**Location:** Route de Malatrex 38, CH-1201 Genève
**Phone:** +41 77 430 36 93
**Email:** admin@phi-fiduciaire.ch
**Website:** phi-fiduciaire.ch
**Hours:** Lundi–Vendredi 8:30–17:30

**Positioning:** High-end fiduciary in Geneva. Premium, prestigious, trustworthy.
**Tone:** Elegant, structured, reassuring, expert. Swiss precision with human warmth.
**Brand archetypes:** The Servant + The Sage.

---

## 3. COLORS

| Token | HEX | Usage |
|-------|-----|-------|
| `--color-primary` | `#1b3f3f` | Headers, nav, dark sections, buttons |
| `--color-accent` | `#ef3a24` | Accent ONLY — thin lines, CTA hover, dividers (max 2–3× per page) |
| `--color-white` | `#ffffff` | Main background |
| `--color-offwhite` | `#f8f6f2` | Section backgrounds |
| `--color-border` | `#e8e6e2` | Subtle dividers |
| `--color-text` | `#1a1a1a` | Body text |
| `--color-text-light` | `#6b6b6b` | Captions, labels |

---

## 4. TYPOGRAPHY

**Display / Headings:** Adobe Caslon Pro → Web fallback: `"IM Fell English", "Libre Caslon Display", Georgia, serif`
**Body / UI:** Avenir LT Pro → Web fallback: `"DM Sans", "Nunito Sans", sans-serif`

**Google Fonts to import:**
```html
<link href="https://fonts.googleapis.com/css2?family=IM+Fell+English:ital@0;1&family=DM+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
```

**Type scale:**
| Level | Size | Font | Weight | Notes |
|-------|------|------|--------|-------|
| H1 | 60–72px | IM Fell English | 400 | Generous tracking, light feel |
| H2 | 38–44px | IM Fell English | 400 | |
| H3 | 20–24px | DM Sans | 500 | |
| Body | 17px | DM Sans | 300 | Line-height: 1.75 |
| Label | 11px | DM Sans | 500 | Uppercase, 0.15em tracking |
| CTA | 14px | DM Sans | 500 | Uppercase, 0.1em tracking |

---

## 5. THE PHI / GOLDEN RATIO PRINCIPLE ⚡

The company is named PHI (φ = 1.618). This must be felt in the design — not rigidly, but as a guiding harmony.

**Fibonacci spacing scale (use exclusively):**
```css
--space-xs:   13px;
--space-sm:   21px;
--space-md:   34px;
--space-lg:   55px;
--space-xl:   89px;
--space-xxl: 144px;
--space-hero:233px;
```

**Apply golden ratio to:**
- Hero split: 61.8% / 38.2% (image vs content, or inverse)
- Content column vs margin: 61.8% / 38.2%
- Card proportions: width:height = 1:1.618
- Typography rhythm: H1 to H2 ratio ≈ 1.618

---

## 6. DESIGN PRINCIPLES

**Feel:** Premium Swiss fiduciaire. Confident. Airy. Structured. Like a very good private bank — but approachable.

**Key visual rules:**
- Large typographic moments — H1 must command the page
- The PHI red accent line (1–2px horizontal) is a signature element — use as section dividers, card accents, decorative moments
- Generous negative space is a luxury signal — do not fill every area
- Geometric blocks (teal rectangles) create visual identity alongside photography
- Light backgrounds dominant — the dark teal appears in hero, footer, CTA sections

**Layout approach:**
- Asymmetric grids inspired by the golden ratio
- Left-aligned text as a rule (not centered)
- Thin decorative red lines under section labels
- Clear visual anchors — every section has one dominant element

**What NOT to do:**
- No purple gradients
- No generic sans-serif (no Inter, no Roboto, no system fonts)
- No dark mode
- No cluttered layouts
- No overuse of red — max 2–3 instances per page visible at once
- No centered hero text on white background (generic)
- No stock handshake photos

---

## 7. IMAGERY RULES

**YES:** Professional people, well-lit, business context. Hands working. Laptops. Confident portraits. Teal/neutral backgrounds.
**NO:** Too casual. Too dark. Too many colors. Empty offices. No people at all.
**Placeholder images:** Use Unsplash with these search terms: `business geneva`, `professional portrait`, `office switzerland`, `hands laptop`.
**Format:** `https://images.unsplash.com/photo-[ID]?w=1200&q=80`

---

## 8. INSPIRATION REFERENCES

| Site | What to extract |
|------|----------------|
| https://mirabaud-compass.com/ | Elegance, confidence, serif headlines, generous white space, structured layout, high-end feel |
| https://www.findea.ch/fr | Swiss fiduciaire flow, clean section transitions, spacing rhythm, professional credibility |

---

## 9. TECHNICAL REQUIREMENTS

- Single HTML file per page (`index.html`, `services.html`)
- All CSS in one `<style>` block at the top (or linked `tokens.css`)
- No external JS frameworks — vanilla JS only
- Google Fonts via CDN (link in `<head>`)
- Responsive: mobile-first, breakpoints at `768px` and `1200px`
- Add WordPress dev comments on every section:
  `<!-- SECTION: Hero — Elementor full-width section, background image -->`
- Language: `lang="fr"` on `<html>` tag

---

## 10. LOCAL SEO REQUIREMENTS

- `<h1>` must contain: **"fiduciaire Genève"** or close variant
- NAP block in footer AND in contact/local section (consistent format):
  ```
  PHI Fiduciaire · Route de Malatrex 38 · 1201 Genève
  +41 77 430 36 93 · admin@phi-fiduciaire.ch
  ```
- Each service = its own `<section>` with a keyword-rich `<h2>` or `<h3>`
- Schema markup comment hint at top of file:
  `<!-- SCHEMA: LocalBusiness — name, address, telephone, openingHours -->`
- Meta title format: `Fiduciaire Genève | PHI Fiduciaire — Comptabilité, Fiscalité, Création de Société`
- Meta description: `PHI Fiduciaire à Genève. Expert-comptable, fiscalité, création Sàrl/SA, domiciliation. 15 ans d'expérience. Réponse sous 24h. +41 77 430 36 93`

---

## 11. PAGE SECTIONS — HOMEPAGE (in order)

1. **Nav** — Logo left, links right, phone visible, thin bottom border
2. **Hero** — Big H1, 1-line subline, 2 CTAs, golden ratio split (image + teal block)
3. **Trust bar** — 3 items: `15 ans d'expérience` · `4.9/5 sur Google` · `FR · EN · DE · PL`
4. **Services** — 6 cards, 1-line each, `En savoir plus →` link
5. **Testimonials** — 3 short quotes, minimal styling
6. **Why PHI** — 3 pillars, 1 sentence each, red accent line motif
7. **Pricing calculator teaser** — Short, CTA to calculator
8. **Local SEO block** — 3 sentences + NAP + map placeholder
9. **FAQ** — 4 questions, 2-sentence answers
10. **Final CTA** — Dark teal background, 2 buttons
11. **Footer** — Full NAP + services links + legal

---

## 12. HOMEPAGE COPY FILE

> See `PHI_HOMEPAGE_COPY.md` for all section texts ready to paste.
