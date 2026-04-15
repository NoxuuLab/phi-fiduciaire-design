# PHI Fiduciaire — Design Mockup & WordPress Dev Handoff

**Client:** PHI Fiduciaire, Genève  
**Purpose:** Static HTML/CSS design reference for WordPress theme development  
**Domain:** phi-fiduciaire.ch  
**Address:** Rue de Malatrex 38, 1201 Genève

---

## Design Status (as of April 2026)

| Page | Status | Notes |
|------|--------|-------|
| `index.html` — Homepage | **Done & verified** | Small changes possible in coming days |
| `services/comptabilite-geneve.html` | **Done & verified** | Reference template for all other service pages |
| `services/fiscalite-tva-geneve.html` | Content placeholder | Structure complete, copy is lorem ipsum |
| `services/creation-societe-geneve.html` | Content placeholder | Structure complete, copy is lorem ipsum |
| `services/gestion-salaires-geneve.html` | Content placeholder | Structure complete, copy is lorem ipsum |
| `services/domiciliation-entreprise-geneve.html` | Content placeholder | Structure complete, copy is lorem ipsum |
| `services/mandat-administrateur-geneve.html` | Content placeholder | Structure complete, copy is lorem ipsum |
| Blog / article page | **Not yet designed** | Only 3 article cards visible on homepage |

### Components not yet finalised

- **Navigation (navbar)** — structure and styling are in place but the component is not fully finalised. Expect changes to spacing, mobile behaviour, and language selector placement before handoff is complete.
- **Footer** — current version is a working draft. Layout, link columns, and legal text are subject to change.

> **For the WordPress dev:** Do not start building the nav or footer components in WordPress until these are marked as finalised in this README. The homepage and comptabilité service page are safe to use as reference for all other sections (hero, service cards, FAQ, pricing, etc.).

---

## What this repository is

This is a **pixel-perfect static mockup** — not a WordPress theme. It exists so the WordPress developer has a complete, visual, and structurally sound reference before a single line of PHP is written. Every page here maps to a WordPress template. Every CSS file maps to a stylesheet that should be enqueued in the theme.

The dev team should:
1. Open the HTML files in a browser to see the target design
2. Use the CSS files as-is (or as a starting point) in the WordPress theme
3. Reproduce the HTML structure in WordPress templates / Elementor / ACF as required
4. Refer to this README for decisions already made (SEO, multilingual, schema)

---

## Project Structure

```
phi-fiduciaire-design/
├── index.html                          ← Homepage template
├── services/
│   ├── comptabilite-geneve.html        ← Service page template (fully designed)
│   ├── fiscalite-tva-geneve.html
│   ├── creation-societe-geneve.html
│   ├── gestion-salaires-geneve.html
│   ├── domiciliation-entreprise-geneve.html
│   └── mandat-administrateur-geneve.html
├── assets/
│   └── css/
│       ├── shared.css                  ← Global styles (all pages)
│       ├── home.css                    ← Homepage-only styles
│       └── service.css                 ← Service pages-only styles
├── img/
│   ├── escalier-spirale-phi-fiduciaire.jpg   ← Homepage hero image
│   ├── escalier-fiduciaire-service.jpg       ← Service pages hero image
│   ├── lac-leman-geneve.jpg
│   ├── paysage-alpin-suisse.jpg
│   ├── geneve-nuit-panorama.jpg
│   ├── article-sarl-sa-geneve.jpg            ← Blog card image 1
│   ├── article-tva-suisse.jpg                ← Blog card image 2
│   ├── article-comptabilite-geneve.jpg       ← Blog card image 3
│   └── logos/
│       ├── phi-white-logo-cut.svg
│       └── phi-horizontal-white.svg
└── robots.txt
```

---

## CSS Architecture

The CSS is split into **three files** that mirror WordPress theme architecture directly.

### `assets/css/shared.css` — Global stylesheet

Loaded on **every page** (homepage + all service pages).

Contains:
- **Design tokens** — all CSS custom properties (`--color-primary`, `--space-xl`, `--font-heading`, etc.)
- **Reset & base** — `*`, `html`, `body`, `img`, `a`, `ul`
- **Typography scale** — `h1`–`h3`, `.label`
- **Button variants** — `.btn`, `.btn--primary`, `.btn--secondary`, `.btn--ghost`, `.btn--outline`
- **`.container`** — max-width centering wrapper
- **Navigation** — full `.nav` with scroll behavior, mobile hamburger, all states and responsive overrides
- **Service cards** — `.service-card` (used on both homepage services grid and service page "related services" section)
- **FAQ accordion** — shared accordion component (used on homepage and service pages)
- **Footer** — full `.footer` with grid, logo, social links, map wrapper, legal bottom bar
- **Utilities** — `.sr-only`

### `assets/css/home.css` — Homepage stylesheet

Loaded **only on `index.html`**. Requires `shared.css` to be loaded first.

Contains:
- **Hero** — full-bleed cinematic hero with duotone overlay, headline, CTA buttons, proof bar
- **Trust bar** — client logos / trust signals strip
- **Services grid** — `.services__grid` section with cards
- **Testimonials** — dark teal background carousel/slider
- **Why PHI** — 3-column benefit cards (`.why-card`)
- **Pricing teaser** — forfait pricing preview section
- **Local SEO** — map + NAP block (includes Google Maps iframe)
- **Blog grid** — 3-column article cards
- **Final CTA** — full-width conversion section
- **Homepage responsive overrides** — all `@media` breakpoints for the above

### `assets/css/service.css` — Service page stylesheet

Loaded on **all `services/*.html` pages**. Requires `shared.css` to be loaded first.

Contains:
- **Hero** — `min-height: 92vh` with `escalier-fiduciaire-service.jpg` background
- **Breadcrumb bar** — `.breadcrumb-bar` navigation trail
- **Service summary** — intro block with meta tags (price, duration, location)
- **Description + component grid** — detail section with `.component-card` grid
- **Pourquoi section** — "Pourquoi choisir PHI" bloc
- **Tarifs** — pricing table
- **FAQ** — service-page FAQ variant (`.faq-service`)
- **Local/geo tags** — `.geo-tags` pill badges
- **Services liés** — "Related services" section (reuses `.service-card` from shared.css)
- **Final CTA** — conversion section
- **Service page responsive overrides** — all `@media` breakpoints for the above

### How CSS loads in each HTML file

```html
<!-- index.html -->
<link rel="stylesheet" href="assets/css/shared.css" />
<link rel="stylesheet" href="assets/css/home.css" />

<!-- services/*.html -->
<link rel="stylesheet" href="../assets/css/shared.css" />
<link rel="stylesheet" href="../assets/css/service.css" />
```

> **Note for WP dev:** In WordPress, enqueue these via `wp_enqueue_style()` in `functions.php`. Use `shared` as a dependency for both `home` and `service` stylesheets so WordPress loads them in the correct order.

---

## Page Templates

### 1. Homepage (`index.html`)

Maps to: `front-page.php` or homepage template in WordPress.

**Sections in order:**
1. Navigation (fixed, becomes opaque on scroll)
2. Hero — full-screen cinematic image, headline, 2 CTA buttons, proof bar (clients, years, rating)
3. Trust bar — partner/client logos
4. Services grid — 6 service cards linking to service pages
5. Testimonials — dark teal section, 3 client quotes
6. Why PHI — 3 value proposition cards
7. Pricing teaser — monthly forfait preview with CTA
8. Local SEO — Google Maps iframe + address/contact block
9. Blog / Articles — 3 latest article cards
10. Final CTA — full-width conversion strip
11. Footer

**Interaction note:** Service cards on the homepage use the **stretched link pattern** — the entire card is clickable, not just the "En savoir plus →" link. This is achieved with `.service-card__link::after { position: absolute; inset: 0; }` and `position: relative` on `.service-card`. Reproduce this in WordPress.

### 2. Service Pages (`services/*.html`)

Maps to: `single-service.php` or a custom post type template / page template in WordPress.

There are 6 service pages, all using the same template:

| File | Service | URL slug (FR) |
|------|---------|---------------|
| `comptabilite-geneve.html` | Comptabilité PME | `/fr/services/comptabilite-geneve/` |
| `fiscalite-tva-geneve.html` | Fiscalité & TVA | `/fr/services/fiscalite-tva-geneve/` |
| `creation-societe-geneve.html` | Création de société | `/fr/services/creation-societe-geneve/` |
| `gestion-salaires-geneve.html` | Gestion des salaires | `/fr/services/gestion-salaires-geneve/` |
| `domiciliation-entreprise-geneve.html` | Domiciliation | `/fr/services/domiciliation-entreprise-geneve/` |
| `mandat-administrateur-geneve.html` | Mandat administrateur | `/fr/services/mandat-administrateur-geneve/` |

**Sections in order:**
1. Navigation
2. Hero — 92vh with background image, breadcrumb overlay
3. Breadcrumb bar — e.g. Accueil > Services > Comptabilité PME
4. Service summary — short intro, meta chips (location, duration, price range)
5. Description — full service description
6. Component grid — what's included (e.g. "Saisie comptable", "Déclaration TVA")
7. Pourquoi PHI — specific reasons for this service
8. Tarifs — pricing table
9. FAQ — 7 Q&As specific to this service
10. Geo tags — Geneva neighborhoods / cantons served
11. Services liés — 3 related service cards
12. Final CTA
13. Footer

### 3. Blog / Article Pages (to be designed)

Maps to: `single.php` / `archive.php` in WordPress.

**Not yet designed in this mockup.** The homepage shows 3 article cards with images (`article-*.jpg`) linking to placeholder URLs. The dev team should request the blog article template design before building this template.

Planned sections:
- Article hero (title, date, category, author)
- Article body (long-form content)
- Related articles
- CTA block

---

## Heading Tag Structure (SEO vs. Visual Hierarchy)

> **Critical for WordPress dev:** The heading tag order is intentionally decoupled from visual size. Do not "fix" it — this is a deliberate SEO + design pattern.

### The inversion explained

On every page, the `h1` and `h2` in the hero are visually inverted compared to what you would expect:

| Tag | CSS class | Visual size | Purpose |
|-----|-----------|-------------|---------|
| `h1` | `.hero__overline` | **11px** — small uppercase eyebrow | Primary keyword for Google crawlers |
| `h2` | `.hero__title` | **62px** — large display headline | What humans read as the main title |

**Homepage example:**
```html
<h1 class="hero__overline">
  <span class="hero__overline-dash"></span>
  FIDUCIAIRE À GENÈVE                     ← Google's primary keyword anchor
</h1>

<h2 class="hero__title">
  Une fiscalité optimisée.<br>
  <em>Des comptes en ordre. L'esprit libre.</em>   ← What visitors actually read
</h2>
```

**Service page example:**
```html
<h1 class="hero__overline" id="hero-heading">
  COMPTABILITÉ PME À GENÈVE              ← Primary keyword, one per page
</h1>

<h2 class="hero__title">
  Vous gérez votre entreprise.<br>
  <em>On s'occupe de vos chiffres.</em>  ← Emotional headline for humans
</h2>
```

### Why this pattern

Google reads `h1` as the most important keyword on the page. By placing the short, dense keyword phrase ("COMPTABILITÉ PME À GENÈVE") in the `h1` and reserving the `h2` for the creative, human-facing headline, both goals are served without compromise:

- **SEO:** crawler sees a clean, unambiguous `h1` with the exact keyword the page targets
- **Design:** the 62px display headline stays beautiful and brand-consistent without stuffing keywords into it
- **User experience:** visitors read a compelling headline — not a keyword list

### Full heading hierarchy on every page

```
h1  (.hero__overline)    → keyword eyebrow, 11px, visually small     [one per page]
h2  (.hero__title)       → main display headline, 62px                [one per page]
h2  (section headings)   → "Des services fiduciaires sur mesure…"    [one per section]
h3  (card/item titles)   → "Comptabilité", "Saisie mensuelle", etc.  [multiple]
```

### The `.label` / `h2.label` eyebrow pattern

Some sections also use a small uppercase eyebrow **above** their `h2` to name the section. This eyebrow is itself marked as an `h2` with the `.label` class (or as a `<p class="label">`):

```html
<!-- Section eyebrow — visually tiny, semantically h2 -->
<h2 class="label" id="services-lies-heading">Services associés</h2>

<!-- Then the real section h2 follows -->
<h2>Ce qui distingue PHI Fiduciaire</h2>
```

`.label` styling (defined in `shared.css`): 11px, `letter-spacing: 0.15em`, uppercase, `color: var(--color-text-light)`, with a 34px red underline via `::after`.

### Mobile note

On small screens (`≤ 768px`), `.hero__overline` is set to `display: none`. The `h1` is therefore **invisible on mobile** — only the `h2.hero__title` shows. This is intentional: Google indexes the full desktop DOM where the `h1` is visible. Do not remove this `display: none` rule thinking it is a bug.

### WordPress implementation

Preserve this exact tag structure in WordPress templates. If using Elementor or ACF:
- The `h1` eyebrow should be an editable text field typed as `h1` in the widget/block settings
- The `h2` display headline should be a separate field typed as `h2`
- Do not let Elementor or the theme auto-assign `h1` to the page title widget — the eyebrow element must carry the `h1`
- Yoast/Rank Math SEO analysis will flag the large `h2` as "not your main keyword heading" — **ignore this warning**, it is correct by design

---

## Design Tokens

All design decisions are encoded as CSS custom properties in `shared.css`:

```css
:root {
  /* Colors */
  --color-primary:    #1b3f3f;   /* Dark teal — brand primary */
  --color-accent:     #ef3a24;   /* Red — CTAs, highlights */
  --color-white:      #ffffff;
  --color-offwhite:   #f8f6f2;   /* Section backgrounds */
  --color-border:     #e8e6e2;
  --color-text:       #1a1a1a;
  --color-text-light: #6b6b6b;

  /* Fibonacci / Golden Ratio spacing scale */
  --space-xs:    13px;
  --space-sm:    21px;
  --space-md:    34px;
  --space-lg:    55px;
  --space-xl:    89px;
  --space-xxl:  144px;
  --space-hero: 233px;

  /* Typography */
  --font-display: 'Cormorant Garamond', 'Libre Caslon Display', Georgia, serif;
  --font-body:    'DM Sans', 'Nunito Sans', sans-serif;

  /* Layout */
  --max-width:  1380px;
  --nav-height: 80px;
}
```

The spacing scale follows the Fibonacci sequence (13, 21, 34, 55, 89, 144, 233) — this is intentional and part of the brand identity.

---

## SEO & Structured Data

### JSON-LD Schemas

Every page has **3 JSON-LD script blocks** in `<head>`:

1. **Service schema** (`AccountingService` or `ProfessionalService`) — describes the specific service with address, geo, hours, price range, aggregate rating
2. **FAQPage schema** — 7 Q&As for the service page (boosts FAQ rich results in Google)
3. **BreadcrumbList schema** — structured breadcrumb trail

These should be output dynamically in WordPress via a plugin (Rank Math or Yoast) or manually via `wp_head` hook / `functions.php`. The static HTML files show the exact structure to reproduce.

### Open Graph & Twitter Card

Homepage and service pages have full OG/Twitter meta tags. In WordPress, Rank Math or Yoast handles these. The static HTML shows the target values.

### `robots.txt`

A `robots.txt` file is present at the root that disallow all crawler for this mockup. Review before go-live.

---

## Multilingual Strategy

PHI Fiduciaire will serve clients in **three languages**:

| Language | URL structure | hreflang code |
|----------|--------------|---------------|
| Français (default) | `phi-fiduciaire.ch/fr/` | `fr-CH` |
| English | `phi-fiduciaire.ch/en/` | `en-CH` |
| Polski | `phi-fiduciaire.ch/pl/` | `pl` |

### Why subdirectories (not subdomains)

`phi-fiduciaire.ch/fr/` vs `fr.phi-fiduciaire.ch/` — subdirectories keep all SEO authority under one root domain. All backlinks, domain age, and trust signals benefit all language versions. Subdomains split authority and are treated as separate sites by Google.

### WordPress Plugin

The site launches in French only (Phase 1). English and Polish are added in later phases. Whether to install Polylang or WPML from day one is a decision for the dev team — it is easier to set up the URL structure correctly from the start than to migrate later. If the dev team is building a plain custom theme and is comfortable managing language URLs manually, it can be deferred. If using a page builder or standard theme, install Polylang at the start.

**Recommended: [Polylang](https://polylang.pro/)** (free tier covers basic needs; Pro adds WooCommerce and nav switcher widget).

Alternative: **WPML** (paid, more mature, but expensive for a small site). Use WPML only if the dev team already has a license or is more comfortable with it.

Either plugin will:
- Create the `/fr/`, `/en/`, `/pl/` URL structure
- Handle all `hreflang` tag output automatically (replacing the static tags in the HTML)
- Provide translated versions of each page/post
- Add a language switcher widget/block for the navbar

### hreflang Tags

Already implemented in all static HTML pages. Example from `comptabilite-geneve.html`:

```html
<link rel="alternate" hreflang="fr-CH" href="https://phi.ch/fr/services/comptabilite-geneve/"/>
<link rel="alternate" hreflang="en-CH" href="https://phi.ch/en/services/accounting-geneva/"/>
<link rel="alternate" hreflang="pl"    href="https://phi.ch/pl/services/ksiegowosc-genewa/"/>
<link rel="alternate" hreflang="x-default" href="https://phi.ch/fr/services/comptabilite-geneve/"/>
```

In WordPress with Polylang/WPML, these are **generated automatically** — do not hardcode them. The static HTML values serve as the canonical reference for the expected URL slugs in each language.

### Language Selector in Navigation

The navbar must include a language switcher. This is a WordPress-specific integration:

**With Polylang:**
- Use the "Language Switcher" widget in a custom menu location
- Or use `pll_the_languages()` template tag in the nav template
- Style to match the existing nav design (small flag icons or `FR | EN | PL` text links)

**With WPML:**
- Use the WPML Language Switcher block or `icl_get_languages()` template function
- Same styling requirement

**Design requirement:** The language selector should appear in the top-right of the navigation bar, visually separated from the main nav links. On mobile, it appears in the hamburger menu. The static HTML mockup shows the nav structure — add the language selector as a sibling element to `.nav__links`.

### Translation Approach

**Do NOT use automatic machine translation for page content.** The translation workflow is:

1. Write all content in French first (live in production)
2. Translate each page manually using AI-assisted translation + human review
3. Verify with a native speaker before publishing each language version
4. Only automatic translation that may be acceptable: navigation labels and UI strings (buttons, form labels) — these can use Polylang's string translation interface

**Exception:** Navigation labels, button text, footer links, and form placeholders can be managed via Polylang's string translations panel (no human review needed for these short strings).

---

## Launch Strategy

### Phase 1 — French only (launch)

- Deploy WordPress with Polylang installed
- Publish all 6 service pages + homepage in French
- English and Polish language variants exist in Polylang but are set to **draft/hidden**
- All `hreflang` tags point only to French URLs (Polylang handles this automatically when EN/PL are not published)

### Phase 2 — English version

- Translate all 6 service pages + homepage to English (AI-assisted, human-reviewed)
- Translate all JSON-LD schema content (service descriptions, FAQ Q&As)
- Update English URL slugs (e.g. `/en/services/accounting-geneva/`)
- Publish and verify hreflang is correctly generated

### Phase 3 — Polish version

- Same process as Phase 2 but for Polish
- Polish URL slugs to be defined (e.g. `/pl/services/ksiegowosc-genewa/`)

### Blog / Articles

- Not live at launch
- 3 article cards on homepage link to `#` placeholder during Phase 1
- Design the blog article template and archive page before Phase 2

---

## WordPress Theme Development Notes

### Enqueuing Stylesheets

In `functions.php`:

```php
function phi_enqueue_styles() {
    wp_enqueue_style(
        'phi-shared',
        get_template_directory_uri() . '/assets/css/shared.css',
        [],
        '1.0.0'
    );

    if ( is_front_page() ) {
        wp_enqueue_style(
            'phi-home',
            get_template_directory_uri() . '/assets/css/home.css',
            ['phi-shared'],
            '1.0.0'
        );
    }

    if ( is_page_template('template-service.php') || is_singular('service') ) {
        wp_enqueue_style(
            'phi-service',
            get_template_directory_uri() . '/assets/css/service.css',
            ['phi-shared'],
            '1.0.0'
        );
    }
}
add_action( 'wp_enqueue_scripts', 'phi_enqueue_styles' );
```

### Google Fonts

Google Fonts are loaded via `<link>` in each HTML `<head>`. In WordPress, enqueue via:

```php
wp_enqueue_style(
    'phi-fonts',
    'https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=Inter:wght@300;400;500;600&display=swap',
    [],
    null
);
```

### JavaScript

The only JS in this mockup is:
- Nav scroll behavior (adds `.scrolled` class to `.nav` on scroll)
- Mobile hamburger toggle
- FAQ accordion toggle

These are inline `<script>` tags at the bottom of each HTML file. Extract them into `assets/js/main.js` and enqueue via `wp_enqueue_script()`.

### Contact Form

The "Devis gratuit" CTA buttons link to `#contact` (a contact section not yet designed in this mockup). In WordPress, use **Contact Form 7** or **WPForms** for the contact/devis form. Style the form fields to match the existing button and input styles in `shared.css`.

---

## Image Inventory

| File | Usage | Alt text |
|------|-------|----------|
| `escalier-spirale-phi-fiduciaire.jpg` | Homepage hero background | Escalier en spirale dorée — architecture Genève |
| `escalier-fiduciaire-service.jpg` | Service pages hero background | Escalier fiduciaire PHI — bureau Genève |
| `lac-leman-geneve.jpg` | Section background / testimonials | Vue sur le lac Léman depuis Genève |
| `paysage-alpin-suisse.jpg` | Section background | Paysage alpin suisse — fiduciaire internationale |
| `geneve-nuit-panorama.jpg` | Section background | Panorama de Genève la nuit |
| `article-sarl-sa-geneve.jpg` | Blog card 1 | Création Sàrl ou SA à Genève — guide pratique |
| `article-tva-suisse.jpg` | Blog card 2 | TVA en Suisse — déclaration et obligations |
| `article-comptabilite-geneve.jpg` | Blog card 3 | Comptabilité PME Genève — bonnes pratiques |
| `logos/phi-white-logo-cut.svg` | Navbar logo | PHI Fiduciaire |
| `logos/phi-horizontal-white.svg` | Footer logo | PHI Fiduciaire |

---

## Contact & Business Info

These values appear in JSON-LD schemas and the footer. Use them as the canonical source.

```
Name:       PHI Fiduciaire
Address:    Rue de Malatrex 38, 1201 Genève, Suisse
Phone:      +41 77 430 36 93
Email:      admin@phi-fiduciaire.ch
Hours:      Mon–Fri 08:30–17:30
Google CID: 3062222191625880894
Coordinates: 46.20727210, 6.13809100
```
