#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update h2 titles and replace paragraph content with lorem ipsum
for the 5 non-comptabilite service pages.
"""
import re

BASE = r"c:\Users\ledbu\Documents\CLIENTS\PHI FIDUCIAIRE\phi-fiduciaire-design\services"

LOREM_S  = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
LOREM_M  = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
LOREM_L  = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
            "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
            "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris "
            "nisi ut aliquip ex ea commodo consequat.")

PAGES = {
    "fiscalite-tva-geneve.html": {
        "description-heading": "Notre service de fiscalité &amp; TVA à Genève",
        "pourquoi-heading":    "Ce qui distingue PHI en conseil fiscal",
        "tarifs-heading":      "Tarifs fiscalité &amp; TVA à Genève",
        "faq-heading":         "Questions fréquentes sur la fiscalité à Genève",
        "local-heading":       "Conseil fiscal pour entreprises à Genève et dans le canton",
        "cta-heading":         "Besoin d'un conseil fiscal à Genève ?",
    },
    "creation-societe-geneve.html": {
        "description-heading": "Notre service de création de société à Genève",
        "pourquoi-heading":    "Ce qui distingue PHI en création de société",
        "tarifs-heading":      "Tarifs création de société à Genève",
        "faq-heading":         "Questions fréquentes sur la création de société à Genève",
        "local-heading":       "Création de société à Genève et dans le canton",
        "cta-heading":         "Prêt à créer votre société à Genève ?",
    },
    "gestion-salaires-geneve.html": {
        "description-heading": "Notre service de gestion des salaires à Genève",
        "pourquoi-heading":    "Ce qui distingue PHI en gestion des salaires",
        "tarifs-heading":      "Tarifs gestion des salaires à Genève",
        "faq-heading":         "Questions fréquentes sur la gestion des salaires à Genève",
        "local-heading":       "Gestion des salaires pour entreprises à Genève",
        "cta-heading":         "Besoin d'un gestionnaire de salaires à Genève ?",
    },
    "domiciliation-entreprise-geneve.html": {
        "description-heading": "Notre service de domiciliation d'entreprise à Genève",
        "pourquoi-heading":    "Ce qui distingue PHI en domiciliation",
        "tarifs-heading":      "Tarifs domiciliation à Genève",
        "faq-heading":         "Questions fréquentes sur la domiciliation à Genève",
        "local-heading":       "Domiciliation d'entreprise à Genève et dans le canton",
        "cta-heading":         "Besoin d'une adresse professionnelle à Genève ?",
    },
    "mandat-administrateur-geneve.html": {
        "description-heading": "Notre service de mandat d'administrateur à Genève",
        "pourquoi-heading":    "Ce qui distingue PHI comme administrateur indépendant",
        "tarifs-heading":      "Tarifs mandat d'administrateur à Genève",
        "faq-heading":         "Questions fréquentes sur le mandat d'administrateur",
        "local-heading":       "Mandat d'administrateur pour sociétés à Genève",
        "cta-heading":         "Besoin d'un administrateur indépendant à Genève ?",
    },
}


def replace_h2_by_id(content, heading_id, new_title):
    """Replace the text inside <h2 id="...">...</h2>."""
    pattern = r'(<h2[^>]*id="%s"[^>]*>)[^<]*(</h2>)' % re.escape(heading_id)
    return re.sub(pattern, r'\g<1>' + new_title + r'\g<2>', content)


def replace_p_content(content, class_name, new_text):
    """Replace content of <p class="...">...</p> (single or multiline)."""
    pattern = r'(<p class="%s">)\s*.*?\s*(</p>)' % re.escape(class_name)
    replacement = r'\g<1>\n        ' + new_text + r'\n      \g<2>'
    return re.sub(pattern, replacement, content, flags=re.DOTALL)


def replace_component_card_p(content):
    """Replace <p> inside .component-card divs (plain <p>, no class)."""
    # Match <p> directly inside component-card that has no class
    pattern = r'(<div class="component-card"[^>]*>.*?<h3>[^<]*</h3>\s*)<p>[^<]*</p>'
    replacement = r'\g<1><p>' + LOREM_M + r'</p>'
    return re.sub(pattern, replacement, content, flags=re.DOTALL)


def replace_pourquoi_bloc_p(content):
    """Replace <p> inside .pourquoi-bloc divs."""
    pattern = r'(<div class="pourquoi-bloc">\s*<h3>[^<]*</h3>\s*)<p>[^<]*</p>'
    replacement = r'\g<1><p>' + LOREM_M + r'</p>'
    return re.sub(pattern, replacement, content, flags=re.DOTALL)


def replace_faq_answer_p(content):
    """Replace <p> inside .faq-item__answer divs."""
    pattern = r'(<div class="faq-item__answer">\s*)<p>[^<]*</p>'
    replacement = r'\g<1><p>' + LOREM_M + r'</p>'
    return re.sub(pattern, replacement, content, flags=re.DOTALL)


def replace_local_body_p(content):
    """Replace <p> inside .local__body."""
    pattern = r'(<div class="local__body">\s*)<p>[^<]*</p>'
    replacement = r'\g<1><p>' + LOREM_L + r'</p>'
    return re.sub(pattern, replacement, content, flags=re.DOTALL)


def process_file(filename, h2_map):
    filepath = BASE + "\\" + filename
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    # 1. Replace h2 titles
    for heading_id, new_title in h2_map.items():
        content = replace_h2_by_id(content, heading_id, new_title)

    # 2. Replace named-class paragraphs
    content = replace_p_content(content, "description__intro", LOREM_L)
    content = replace_p_content(content, "tarifs__subline", LOREM_M)
    content = replace_p_content(content, "faq__left-tagline", LOREM_S)
    content = replace_p_content(content, "services-lies__intro", LOREM_S)
    content = replace_p_content(content, "service-card__desc", LOREM_S)
    content = replace_p_content(content, "cta-final__text", LOREM_M)

    # 3. Replace testimonial-slide__text
    content = replace_p_content(content, "testimonial-slide__text", LOREM_S)

    # 4. Replace plain <p> inside component-cards
    content = replace_component_card_p(content)

    # 5. Replace plain <p> inside pourquoi-blocs
    content = replace_pourquoi_bloc_p(content)

    # 6. Replace FAQ answer paragraphs
    content = replace_faq_answer_p(content)

    # 7. Replace local body paragraph
    content = replace_local_body_p(content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Updated: {filename}")


for filename, h2_map in PAGES.items():
    process_file(filename, h2_map)

print("Done.")
