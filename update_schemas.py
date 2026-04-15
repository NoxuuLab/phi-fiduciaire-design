#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Replace the 3 JSON-LD schema blocks (Service, FAQPage, BreadcrumbList)
for the 5 non-comptabilite service pages.
"""
import re

BASE = r"c:\Users\ledbu\Documents\CLIENTS\PHI FIDUCIAIRE\phi-fiduciaire-design\services"

COMMON = {
    "telephone": "+41774303693",
    "email": "admin@phi-fiduciaire.ch",
    "address": {
        "streetAddress": "Rue de Malatrex 38",
        "addressLocality": "Genève",
        "postalCode": "1201",
        "addressRegion": "Genève",
        "addressCountry": "CH"
    },
    "geo": {"latitude": 46.20727210, "longitude": 6.13809100},
    "hours": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "08:30",
    "closes": "17:30",
    "rating": {"ratingValue": "4.9", "reviewCount": "31", "bestRating": "5"},
    "sameAs": "https://www.google.com/maps?cid=3062222191625880894"
}

PAGES = {
    "fiscalite-tva-geneve.html": {
        "type": "AccountingService",
        "slug": "fiscalite-tva-geneve",
        "name": "PHI Fiduciaire — Fiscalité & TVA Genève",
        "description": "Cabinet fiduciaire genevois spécialisé en optimisation fiscale ICC/IFD, déclarations fiscales et décomptes TVA pour PME, Sàrl et SA à Genève.",
        "serviceType": "Fiscalité et TVA PME",
        "breadcrumbName": "Fiscalité & TVA Genève",
        "faqs": [
            {
                "q": "Quelle est la différence entre l'ICC et l'IFD ?",
                "a": "L'ICC (impôt cantonal et communal) est perçu par le canton de Genève et la commune de domicile de la société. L'IFD (impôt fédéral direct) est perçu par la Confédération. Les taux et les bases imposables diffèrent. PHI Fiduciaire optimise votre charge fiscale sur ces deux niveaux, en tirant parti des déductions légales disponibles."
            },
            {
                "q": "À partir de quel chiffre d'affaires faut-il s'assujettir à la TVA en Suisse ?",
                "a": "L'assujettissement à la TVA est obligatoire dès que le chiffre d'affaires annuel dépasse 100 000 CHF. En dessous de ce seuil, l'inscription volontaire reste possible et peut être avantageuse. PHI Fiduciaire gère vos décomptes TVA trimestriels ou semestriels et vous conseille sur le taux le plus favorable pour votre activité."
            },
            {
                "q": "Quels sont les taux de TVA applicables en Suisse ?",
                "a": "En 2024, la TVA suisse comporte trois taux : le taux normal de 8,1 %, le taux réduit de 2,6 % (denrées alimentaires, médicaments, livres) et le taux spécial de 3,8 % pour les prestations d'hébergement. PHI Fiduciaire vérifie que vos décomptes appliquent les taux corrects selon la nature de vos prestations."
            },
            {
                "q": "Comment PHI Fiduciaire peut-il réduire ma charge fiscale légalement ?",
                "a": "Plusieurs leviers sont disponibles : optimisation de la rémunération du dirigeant, gestion du timing de comptabilisation des produits et charges, planification des amortissements, déductions liées à la prévoyance professionnelle, et choix de la méthode de décompte TVA. PHI Fiduciaire analyse votre situation et met en œuvre les stratégies adaptées dans le respect strict du droit fiscal suisse."
            },
            {
                "q": "Que se passe-t-il en cas de contrôle fiscal à Genève ?",
                "a": "En cas de contrôle de l'Administration fiscale cantonale (AFC GE) ou de l'AFC fédérale, PHI Fiduciaire vous représente et prépare tous les documents requis. Notre connaissance des pratiques locales de l'AFC GE permet de traiter les demandes de manière efficace et d'éviter des redressements injustifiés."
            },
            {
                "q": "Quand dois-je déposer ma déclaration fiscale à Genève ?",
                "a": "Pour les personnes morales (Sàrl, SA) à Genève, la déclaration d'impôt doit être déposée dans les six mois suivant la clôture de l'exercice. Des délais supplémentaires sont accordés sur demande motivée. PHI Fiduciaire gère le calendrier fiscal de votre société et s'assure du respect de toutes les échéances."
            },
            {
                "q": "Combien coûte un mandat de fiscalité avec PHI Fiduciaire ?",
                "a": "Nos honoraires dépendent de la complexité de votre structure, du volume de transactions et des services inclus. Un forfait annuel est établi après une consultation initiale gratuite. La majorité de nos clients PME bénéficient d'un accompagnement fiscal complet entre 500 et 2 000 CHF par an selon la situation."
            }
        ]
    },
    "creation-societe-geneve.html": {
        "type": "ProfessionalService",
        "slug": "creation-societe-geneve",
        "name": "PHI Fiduciaire — Création de société Genève",
        "description": "Cabinet fiduciaire genevois accompagnant la création de Sàrl et SA à Genève : rédaction des statuts, inscription au Registre du Commerce, libération du capital et affiliations sociales.",
        "serviceType": "Création de société Sàrl SA",
        "breadcrumbName": "Création de société Genève",
        "faqs": [
            {
                "q": "Quelle est la différence entre une Sàrl et une SA en Suisse ?",
                "a": "La Sàrl (Société à responsabilité limitée) nécessite un capital minimum de 20 000 CHF et convient aux PME avec peu d'associés. La SA (Société anonyme) exige un capital minimum de 100 000 CHF (dont 50 000 libérés) et offre plus de flexibilité pour l'actionnariat et les levées de fonds. PHI Fiduciaire vous guide dans le choix de la forme juridique adaptée à votre projet."
            },
            {
                "q": "Combien de temps faut-il pour créer une Sàrl à Genève ?",
                "a": "Avec PHI Fiduciaire, la création d'une Sàrl à Genève prend en moyenne 2 à 3 semaines ouvrables, depuis la signature de l'acte constitutif devant notaire jusqu'à l'inscription définitive au Registre du Commerce genevois. Ce délai inclut la libération du capital, la rédaction des statuts et toutes les démarches administratives."
            },
            {
                "q": "Quel capital minimum faut-il pour créer une Sàrl ?",
                "a": "Le capital social minimum d'une Sàrl en Suisse est de 20 000 CHF, entièrement libéré lors de la constitution. Ce capital doit être déposé sur un compte bancaire de consignation avant la signature de l'acte constitutif. PHI Fiduciaire coordonne l'ouverture du compte de consignation avec votre banque."
            },
            {
                "q": "Faut-il obligatoirement un notaire pour créer une société à Genève ?",
                "a": "Oui, la constitution d'une Sàrl ou d'une SA en Suisse requiert un acte authentique rédigé par un notaire. Le notaire certifie les statuts et l'acte de constitution. PHI Fiduciaire travaille avec des notaires genevois partenaires et coordonne l'ensemble des démarches pour vous éviter tout déplacement inutile."
            },
            {
                "q": "Quelles affiliations sociales sont obligatoires à la création ?",
                "a": "Toute société employant du personnel est tenue de s'affilier à une caisse AVS/AI/APG, à une caisse d'assurance-accidents (LAA) et à une institution de prévoyance LPP pour les salariés. PHI Fiduciaire gère toutes ces affiliations dès la création de votre société, afin que vous soyez opérationnel immédiatement."
            },
            {
                "q": "Est-il possible de créer une société en Suisse sans être résident ?",
                "a": "Oui, un non-résident peut constituer une Sàrl ou une SA en Suisse. Toutefois, le CO exige qu'au moins un gérant ou administrateur domicilié en Suisse soit inscrit au Registre du Commerce. PHI Fiduciaire propose un mandat d'administrateur domicilié pour répondre à cette exigence légale."
            },
            {
                "q": "Combien coûte la création d'une Sàrl avec PHI Fiduciaire ?",
                "a": "Le coût total inclut nos honoraires de conseil, les frais notariaux (environ 800 à 1 500 CHF), l'émolument du Registre du Commerce (environ 600 CHF) et les éventuels frais d'annonce officielle. PHI Fiduciaire vous remet un devis détaillé et transparent lors de la consultation initiale gratuite."
            }
        ]
    },
    "gestion-salaires-geneve.html": {
        "type": "AccountingService",
        "slug": "gestion-salaires-geneve",
        "name": "PHI Fiduciaire — Gestion des salaires Genève",
        "description": "Cabinet fiduciaire genevois assurant la gestion complète des salaires pour PME à Genève : fiches de salaire, déclarations AVS/LPP/LAA, impôt à la source et charges sociales.",
        "serviceType": "Gestion des salaires PME",
        "breadcrumbName": "Gestion des salaires Genève",
        "faqs": [
            {
                "q": "Que comprend la gestion externalisée des salaires ?",
                "a": "La gestion externalisée des salaires comprend : l'établissement mensuel des fiches de salaire, le calcul et le paiement des charges sociales (AVS/AI/APG, AC, LAA, IJM, LPP), la déclaration et le versement de l'impôt à la source pour les employés concernés, et la production des attestations de salaire annuelles. PHI Fiduciaire prend en charge l'intégralité de ces obligations."
            },
            {
                "q": "Qui est soumis à l'impôt à la source en Suisse ?",
                "a": "Sont soumis à l'impôt à la source les salariés étrangers sans permis C résidant en Suisse, ainsi que les frontaliers selon les conventions fiscales bilatérales. À Genève, les employeurs sont tenus de retenir et de reverser l'impôt à la source mensuellement à l'Administration fiscale cantonale. PHI Fiduciaire gère ces décomptes pour l'ensemble de vos collaborateurs concernés."
            },
            {
                "q": "Quelles sont les charges sociales obligatoires en Suisse ?",
                "a": "Les charges sociales obligatoires comprennent : AVS/AI/APG (10,6 % partagés entre employeur et salarié), assurance-chômage (2,2 % partagés), LAA (accidents professionnels à la charge de l'employeur, accidents non professionnels à celle du salarié), LPP (prévoyance professionnelle, taux variable selon l'âge) et, selon les cantons, des allocations familiales."
            },
            {
                "q": "Comment fonctionne la LPP pour une PME ?",
                "a": "Toute PME employant des salariés dont le salaire annuel dépasse 22 050 CHF (seuil 2024) est tenue de les affilier à une institution de prévoyance LPP. Les cotisations sont partagées entre l'employeur et le salarié, avec un minimum légal fixé par le CO. PHI Fiduciaire vous aide à choisir l'institution de prévoyance adaptée et gère les décomptes mensuels."
            },
            {
                "q": "Quand les salaires doivent-ils être payés à Genève ?",
                "a": "Le Code des obligations suisse (art. 323 CO) impose le paiement du salaire à la fin du mois, sauf convention contraire dans le contrat de travail ou la CCT applicable. PHI Fiduciaire prépare les ordres de virement en temps voulu pour que vos collaborateurs soient payés à la date prévue, sans interruption."
            },
            {
                "q": "PHI Fiduciaire peut-il gérer les salaires pour une entreprise avec des frontaliers ?",
                "a": "Oui, Genève étant une zone de forte concentration de travailleurs frontaliers, PHI Fiduciaire maîtrise les spécificités applicables : impôt à la source selon l'accord bilatéral franco-suisse, déclaration aux autorités françaises, traitement des permis G. Nous gérons le traitement de paie des frontaliers en conformité avec la législation des deux pays."
            },
            {
                "q": "Combien coûte l'externalisation de la paie chez PHI Fiduciaire ?",
                "a": "Nos forfaits paie sont calculés par employé et par mois, avec un tarif dégressif selon l'effectif. Pour une PME de 5 à 20 employés, le coût se situe généralement entre 30 et 80 CHF par fiche de salaire mensuelle. Un devis personnalisé est transmis dans les 48 heures sur demande."
            }
        ]
    },
    "domiciliation-entreprise-geneve.html": {
        "type": "ProfessionalService",
        "slug": "domiciliation-entreprise-geneve",
        "name": "PHI Fiduciaire — Domiciliation d'entreprise Genève",
        "description": "Adresse commerciale professionnelle au cœur de Genève pour Sàrl et SA. Gestion du courrier incluse — tout ce qu'exige le Registre du Commerce, sans bureau physique.",
        "serviceType": "Domiciliation d'entreprise",
        "breadcrumbName": "Domiciliation d'entreprise Genève",
        "faqs": [
            {
                "q": "Qu'est-ce qu'une adresse de domiciliation pour une société en Suisse ?",
                "a": "Une adresse de domiciliation est une adresse commerciale officielle inscrite au Registre du Commerce, distincte du lieu de résidence des associés ou gérants. En Suisse, toute Sàrl ou SA doit disposer d'une adresse fixe en Suisse pour son siège social. PHI Fiduciaire met à disposition son adresse genevoise à cet effet."
            },
            {
                "q": "La domiciliation suffit-elle pour s'inscrire au Registre du Commerce ?",
                "a": "Oui, une adresse de domiciliation professionnelle est reconnue comme siège social valide par le Registre du Commerce genevois, à condition que la société puisse y être effectivement contactée. PHI Fiduciaire fournit une attestation de domiciliation que le notaire intégrera à l'acte constitutif ou à la modification de siège."
            },
            {
                "q": "Que comprend la gestion du courrier dans votre offre de domiciliation ?",
                "a": "Notre service de gestion du courrier comprend : la réception de tout courrier adressé à votre société, le scan et la transmission électronique dans les 24 heures ouvrables, la possibilité de retrait physique sur rendez-vous, et l'archivage structuré des documents reçus. Les colis et envois en recommandé sont également gérés."
            },
            {
                "q": "Peut-on domicilier plusieurs sociétés à la même adresse ?",
                "a": "Oui, il est légalement possible et courant de domicilier plusieurs entités légales à la même adresse. PHI Fiduciaire gère la domiciliation de plusieurs sociétés appartenant à un même groupe ou à des clients différents, avec une gestion du courrier individualisée par entité."
            },
            {
                "q": "La domiciliation est-elle possible pour une société étrangère souhaitant s'implanter à Genève ?",
                "a": "Oui, PHI Fiduciaire accompagne régulièrement des groupes internationaux souhaitant établir une filiale ou une succursale à Genève. La domiciliation s'accompagne alors d'un mandat d'administrateur domicilié — exigé par le CO pour les SA et Sàrl — afin de satisfaire pleinement aux conditions d'inscription au Registre du Commerce."
            },
            {
                "q": "Quelle est la durée minimale d'un contrat de domiciliation ?",
                "a": "Nos contrats de domiciliation sont conclus pour une durée minimale d'un an, renouvelable par tacite reconduction avec un préavis de résiliation de 3 mois. Des formules à l'essai sur 6 mois sont disponibles pour les sociétés en phase de démarrage. Contactez-nous pour connaître les conditions actuelles."
            },
            {
                "q": "Combien coûte la domiciliation d'une société à Genève chez PHI Fiduciaire ?",
                "a": "Nos tarifs de domiciliation comprennent l'adresse de siège social et la gestion du courrier, pour un forfait mensuel tout compris. Le tarif varie selon le volume de courrier estimé et les services additionnels souhaités. Un devis personnalisé vous est remis gratuitement lors de la consultation initiale."
            }
        ]
    },
    "mandat-administrateur-geneve.html": {
        "type": "ProfessionalService",
        "slug": "mandat-administrateur-geneve",
        "name": "PHI Fiduciaire — Mandat d'administrateur Genève",
        "description": "Administrateur domicilié indépendant pour SA et Sàrl à Genève. Implantez-vous en Suisse sans contrainte de résidence — conformément aux art. 718 et 814 CO.",
        "serviceType": "Mandat d'administrateur indépendant",
        "breadcrumbName": "Mandat d'administrateur Genève",
        "faqs": [
            {
                "q": "Pourquoi une SA ou Sàrl doit-elle avoir un administrateur domicilié en Suisse ?",
                "a": "Le Code des obligations suisse (art. 718 CO pour les SA, art. 814 CO pour les Sàrl) exige qu'au moins un représentant habilité à signer pour la société soit domicilié en Suisse. Cette exigence vise à garantir qu'une personne physiquement présente en Suisse puisse représenter la société auprès des autorités suisses. PHI Fiduciaire assure ce mandat de représentation."
            },
            {
                "q": "Quelles sont les responsabilités d'un administrateur indépendant ?",
                "a": "L'administrateur indépendant fourni par PHI Fiduciaire agit comme représentant domicilié au sens du CO. Son rôle se limite à la représentation légale de la société : signature de documents officiels, réception de communications des autorités, et représentation formelle au Registre du Commerce. Il n'intervient pas dans la gestion opérationnelle de la société."
            },
            {
                "q": "Un administrateur indépendant peut-il engager la responsabilité de la société ?",
                "a": "Un administrateur indépendant dispose uniquement des pouvoirs expressément définis dans les statuts et le contrat de mandat. PHI Fiduciaire encadre strictement ce mandat : les pouvoirs de signature sont limités, et tout acte engageant la société au-delà du mandat de représentation requiert l'accord préalable des actionnaires ou associés."
            },
            {
                "q": "Le mandat d'administrateur est-il compatible avec une direction opérationnelle étrangère ?",
                "a": "Oui, c'est précisément l'utilité principale de ce service. Les dirigeants résidant à l'étranger conservent la pleine direction opérationnelle de leur société suisse. L'administrateur domicilié de PHI Fiduciaire répond uniquement à l'exigence légale de présence en Suisse, sans interférer avec la gouvernance de l'entreprise."
            },
            {
                "q": "Faut-il un administrateur domicilié pour une succursale en Suisse ?",
                "a": "Pour une succursale d'une société étrangère inscrite au Registre du Commerce suisse, la loi exige également un représentant domicilié en Suisse habilité à la représenter. PHI Fiduciaire assure ce mandat pour les succursales genevоises de sociétés étrangères, en coordination avec la maison-mère."
            },
            {
                "q": "Quelle est la différence entre un administrateur et un gérant dans une Sàrl ?",
                "a": "Dans une Sàrl suisse, les associés-gérants exercent la gestion de la société. L'administrateur domicilié fourni par PHI Fiduciaire remplit uniquement la condition légale de domicile suisse prévue à l'art. 814 CO. Il est inscrit au Registre du Commerce comme gérant avec pouvoir de signature individuelle limité, mais n'interfère pas dans les décisions de gestion."
            },
            {
                "q": "Quel est le coût d'un mandat d'administrateur avec PHI Fiduciaire ?",
                "a": "Le mandat d'administrateur est facturé sur une base annuelle forfaitaire. Le tarif dépend de la complexité de la structure, du volume de documents à signer et des éventuels services complémentaires (domiciliation, comptabilité). Contactez-nous pour obtenir une proposition tarifaire personnalisée."
            }
        ]
    }
}


def build_service_schema(p, slug, common):
    return f'''{{
  "@context": "https://schema.org",
  "@type": "{p['type']}",
  "@id": "https://phi-fiduciaire.ch/services/{slug}",
  "name": "{p['name']}",
  "url": "https://phi-fiduciaire.ch/services/{slug}",
  "description": "{p['description']}",
  "telephone": "{common['telephone']}",
  "email": "{common['email']}",
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "{common['address']['streetAddress']}",
    "addressLocality": "{common['address']['addressLocality']}",
    "postalCode": "{common['address']['postalCode']}",
    "addressRegion": "{common['address']['addressRegion']}",
    "addressCountry": "{common['address']['addressCountry']}"
  }},
  "geo": {{
    "@type": "GeoCoordinates",
    "latitude": {common['geo']['latitude']},
    "longitude": {common['geo']['longitude']}
  }},
  "openingHoursSpecification": [
    {{
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
      "opens": "{common['opens']}",
      "closes": "{common['closes']}"
    }}
  ],
  "priceRange": "CHF",
  "currenciesAccepted": "CHF",
  "areaServed": {{
    "@type": "State",
    "name": "Canton de Genève"
  }},
  "serviceType": "{p['serviceType']}",
  "aggregateRating": {{
    "@type": "AggregateRating",
    "ratingValue": "{common['rating']['ratingValue']}",
    "reviewCount": "{common['rating']['reviewCount']}",
    "bestRating": "{common['rating']['bestRating']}"
  }},
  "sameAs": [
    "{common['sameAs']}"
  ]
}}'''


def build_faq_schema(faqs):
    entities = []
    for faq in faqs:
        entities.append(f'''    {{
      "@type": "Question",
      "name": "{faq['q']}",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "{faq['a']}"
      }}
    }}''')
    joined = ",\n".join(entities)
    return f'''{{\n  "@context": "https://schema.org",\n  "@type": "FAQPage",\n  "mainEntity": [\n{joined}\n  ]\n}}'''


def build_breadcrumb_schema(p, slug):
    return f'''{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{
      "@type": "ListItem",
      "position": 1,
      "name": "Accueil",
      "item": "https://phi-fiduciaire.ch/"
    }},
    {{
      "@type": "ListItem",
      "position": 2,
      "name": "Services",
      "item": "https://phi-fiduciaire.ch/services/"
    }},
    {{
      "@type": "ListItem",
      "position": 3,
      "name": "{p['breadcrumbName']}",
      "item": "https://phi-fiduciaire.ch/services/{slug}"
    }}
  ]
}}'''


SCRIPT_RE = re.compile(
    r'<script type="application/ld\+json">\s*(.*?)\s*</script>',
    re.DOTALL
)


def process_file(filename, page_data):
    filepath = BASE + "\\" + filename
    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    slug = page_data["slug"]
    schemas = [
        build_service_schema(page_data, slug, COMMON),
        build_faq_schema(page_data["faqs"]),
        build_breadcrumb_schema(page_data, slug),
    ]

    idx = 0
    def replacer(m):
        nonlocal idx
        if idx < len(schemas):
            result = f'<script type="application/ld+json">\n{schemas[idx]}\n  </script>'
            idx += 1
            return result
        return m.group(0)

    content = SCRIPT_RE.sub(replacer, content)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated: {filename} ({idx} schemas replaced)")


for filename, page_data in PAGES.items():
    process_file(filename, page_data)

print("Done.")
