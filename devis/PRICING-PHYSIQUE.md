# Grille tarifaire — Personne physique (devis/index.html)

Résumé des prix appliqués dans le parcours "Particulier" de l'outil de devis. Montants en CHF HT. Source : `priceDeclaration()` et `priceIndependant()` dans [devis/index.html](index.html).

## 1. Déclaration fiscale

Prix unique pour une déclaration (un exercice) : une base de 220, plus un supplément par élément déclaré. Aucun garde-fou : toujours une estimation.

### Situation personnelle

| Réponse | Prix |
|---|---|
| Base, quel que soit le canton | 220 |
| Célibataire / Divorcé(e) | 0 |
| Marié(e) / Couple | +30 |
| Enfant à charge | +20 par enfant |

### Situation internationale

Chaque case cochée ajoute 80 (cumulable, maximum 240) :

- Frontalier (masqué si canton = Genève ou Vaud)
- Revenus étrangers
- Bien immobilier à l'étranger

### Sources de revenus

| Source | Prix |
|---|---|
| Salaire — 0 ou 1 certificat | 0 |
| Salaire — 2 ou 3 certificats | +20 |
| Salaire — 4 certificats ou plus | +50 |
| Chômage / APG | +20 |
| Pension alimentaire | +20 par pension |
| Rente / Retraite, Revenus locatifs | 0 |
| Activité indépendante | voir § 2 |

### Patrimoine à déclarer

| Élément | Prix |
|---|---|
| Portefeuille de titres | 100 pour le 1er, +20 par suivant |
| Immobilier en Suisse | 80 pour le 1er bien, +20 par suivant |
| 3e pilier | +20 (+40 si marié(e)) |
| Participation dans une société (> 10 %) | +40 par société |
| Cryptomonnaies | +100 |

### Éléments particuliers et documents

| Élément | Prix |
|---|---|
| Succession / héritage | +200 |
| Frais de formation | 0 |
| Documents complets ou en cours de tri | 0 |
| Documents à organiser | +60 |

*Exemple : Genève · marié(e) · 2 enfants → 220 + 30 + 40 = 290.*

## 2. Activité indépendante

La comptabilité de l'activité s'ajoute à la déclaration fiscale dans une carte unique ("Estimation").

**CA < 100'000 — forfait** (0 à 3 employés ; dès 4 employés → devis personnalisé) :

| Transmission | Prix |
|---|---|
| Fichier Excel préparé | 1'250 + 260 = 1'510 |
| Documents à trier | 1'250 + 1'040 = 2'290 |

**CA ≥ 100'000 — matrice** : prix de base selon le CA × 1.10 par employé (grille identique aux sociétés).

| CA annuel | Base |
|---|---|
| ≤ 100'000 | 3'600 |
| 200'000 | 3'960 |
| 300'000 | 4'356 |
| 400'000 | 5'500 |
| 500'000 | 6'050 |
| 600'000 | 6'655 |
| 700'000 | 7'321 |
| 800'000 | 8'053 |

Interpolation linéaire entre deux paliers.

**Garde-fous** (CA ≥ 100'000) : ratio = comptabilité ÷ CA, déclaration exclue.

- CA > 800'000 ou plus de 20 employés → devis personnalisé
- Ratio < 1 % → estimation (palier bas)
- Ratio de 1 % à 5 % inclus → estimation
- Ratio > 5 % → devis personnalisé

*Exemple : CA 250'000 · 1 employé → 4'574 (ratio 1,83 %) + déclaration 220 = 4'794.*
