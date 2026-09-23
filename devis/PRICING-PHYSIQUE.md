# Grille tarifaire — Personne physique (devis/index.html)

Résumé de tous les prix appliqués dans le parcours "Particulier" de l'outil de devis. Les montants sont HT. Source : `personalDeclarationPricing()` et `calcPrice()` / `getBasePrice()` dans [devis/index.html](index.html).

## 1. Déclaration fiscale de base

Base selon le canton de résidence, puis multipliée selon l'état civil (résultat arrondi).

| Canton | Base |
|---|---|
| Genève | CHF 350 |
| Vaud | CHF 280 |
| Autre | CHF 260 |

| État civil | Multiplicateur |
|---|---|
| Célibataire | ×1 |
| Divorcé(e) | ×1.05 |
| Marié(e) / Couple | ×1.15 |

*Exemple : Genève + Marié(e) → 350 × 1.15 = CHF 403. Dans le résumé, ce montant est affiché en deux lignes : "Base déclaration fiscale — CHF 350" puis "Marié(e) / Couple — +CHF 53".*

## 2. Sources de revenus

### Salaire → Certificats de revenus
Champ nesté sous "Salaire" ; l'utilisateur saisit le nombre exact de certificats.

| Nombre de certificats | Supplément |
|---|---|
| 1 | Inclus dans le tarif de base |
| 2 – 3 | +CHF 20 |
| 4 ou plus | +CHF 50 |

### Activité indépendante
Champ nesté sous "Activité indépendante" (nombre d'employés + CA annuel). La comptabilité de l'activité indépendante est calculée séparément puis **ajoutée** au total de la déclaration personnelle dans une carte unique ("Estimation").

**CA < CHF 100'000** — forfait fixe, avec choix de transmission des documents :

| Mode de transmission | Prix |
|---|---|
| Fichier Excel préparé | CHF 1 250 |
| Documents à trier | CHF 1 250 + CHF 150 = CHF 1 400 |

**CA ≥ CHF 100'000** — matrice CA + employés (identique à la grille Personne morale, voir § 5).

### Autres sources (aucun impact sur le prix)
- Chômage / APG
- Rente / Retraite
- Pension alimentaire

### Revenus locatifs
+CHF 60 si coché.

## 3. Situation internationale

Forfait unique de **+CHF 80** dès qu'au moins une case est cochée parmi :

- Frontalier (masqué si canton de résidence = Genève ou Vaud)
- Revenus étrangers
- Bien immobilier à l'étranger

*(Pas de cumul — une seule case ou les trois cochées = même supplément de CHF 80.)*

## 4. Patrimoine à déclarer

+CHF 40 par case cochée (cumulatif) :

- Portefeuille titres
- Immobilier en Suisse
- Immobilier à l'étranger
- 3e pilier
- Participation dans une société (>10% SA/Sàrl/société étrangère)
- Cryptomonnaies

## 5. Matrice CA + employés (Activité indépendante, CA ≥ 100k)

Identique au calcul utilisé pour les personnes morales (`calcPrice()`).

**Base selon le CA** (interpolation linéaire entre paliers) :

| CA annuel | Base |
|---|---|
| ≤ 100 000 | CHF 3 600 |
| 200 000 | CHF 3 960 |
| 300 000 | CHF 4 356 |
| 400 000 | CHF 5 500 |
| 500 000 | CHF 6 050 |
| 600 000 | CHF 6 655 |
| 700 000 | CHF 7 321 |
| 800 000 | CHF 8 053 |
| > 800 000 | Sur devis |

**Ajustement employés** : `base × 1.10^(nombre d'employés)`, arrondi.

**Garde-fous :**

- CA > 800 000 ou employés > 20 → sur devis
- Résultat < 1.5% du CA (avec ≥1 employé) → hors grille, devis manuel
- Résultat > 3% du CA (sauf 0 employé et CA ≤ 200 000) → sur devis

## 6. Éléments particuliers (aucun impact sur le prix)

Ces cases sont informatives uniquement, sans supplément automatique :

- Plusieurs immeubles
- Succession / héritage
- Frais de formation

## Récapitulatif des montants

| Élément | Montant |
|---|---|
| Base déclaration (canton) | CHF 260 / 280 / 350 |
| Multiplicateur état civil | ×1 / ×1.05 / ×1.15 |
| Certificats de revenus (2–3) | +CHF 20 |
| Certificats de revenus (4+) | +CHF 50 |
| Revenus locatifs | +CHF 60 |
| Situation internationale (≥1 case) | +CHF 80 |
| Patrimoine (par case) | +CHF 40 |
| Indépendant, CA < 100k — Excel préparé | CHF 1 250 |
| Indépendant, CA < 100k — Documents à trier | CHF 1 400 |
| Indépendant, CA ≥ 100k | Matrice CA + employés (§5) |
