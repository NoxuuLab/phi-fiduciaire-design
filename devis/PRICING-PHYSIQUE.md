# Grille tarifaire — Personne physique (devis/index.html)

Résumé des prix appliqués dans le parcours "Particulier" de l'outil de devis. Montants en CHF HT. Source : `priceDeclaration()` et `priceIndependant()` dans [devis/index.html](index.html).

## 1. Déclaration fiscale

Prix unique pour une déclaration (un exercice) : une base de 220, plus un supplément par élément déclaré. Aucun garde-fou : toujours une estimation.

### Situation personnelle

Canton d'imposition : Genève / Vaud / Autre canton suisse (si « Autre » : « Précisez le canton », texte libre optionnel). Même base tarifaire pour tous les cantons.

| Réponse | Prix |
|---|---|
| Base déclaration PP, quel que soit le canton | 220 |
| Célibataire / Séparé(e) / Divorcé(e) / Veuf / veuve | 0 |
| En couple, non marié(e) (concubins = dossiers distincts) | 0 |
| Marié(e) / partenariat enregistré — déclaration commune : Oui | +30 (total 250) |
| Marié(e) / partenariat enregistré — déclaration commune : Non | 0 |
| Enfants à charge — 1er et 2e | inclus |
| Enfants à charge — dès le 3e | +20 par enfant |

Une seule base par déclaration. La question « Déclaration commune ? » n'apparaît que pour Marié(e) / partenariat enregistré et elle est obligatoire.

### Situation internationale

| Réponse | Prix |
|---|---|
| Frontalier : Oui (tous les cantons, une seule fois) | +80 |
| Frontalier : Non (par défaut) | 0 |
| Revenus de source étrangère — par source (dès la 1re) | +30 |
| Activité professionnelle exercée à l'étranger | 0 |
| Rente ou pension étrangère | 0 |

Revenus de source étrangère : une seule question, « Combien de sources de revenus étrangères ? » (1+). Chaque source +30, y compris pour un frontalier (le +80 frontalier s'ajoute).

Le bien immobilier à l'étranger n'est plus dans cette étape : il sera traité à l'étape 4 (Patrimoine).

### Sources de revenus

| Source | Prix |
|---|---|
| Salaire — 0 à 2 certificats | 0 |
| Salaire — 3 certificats | +20 |
| Salaire — 4 certificats ou plus | +50 |
| Chômage / APG — 1re attestation | inclus |
| Chômage / APG — chaque attestation supplémentaire | +20 |
| Rente / Retraite — 1re attestation | inclus |
| Rente / Retraite — chaque attestation supplémentaire | +20 |
| Revenus locatifs (sans quantité) | 0 |
| Pension alimentaire | +20 par bénéficiaire |
| Activité indépendante | voir § 2 |

Un seul compteur par revenu pour toute la déclaration (aussi en déclaration commune), à 1 dès la sélection.

Chômage / APG et rente sont indépendants du salaire : la 1re attestation est incluse, chaque attestation en plus +20.

*Exemples : célibataire, 3 certificats → +20 ; couple en déclaration commune, 4 certificats → +50 ; retraité AVS + LPP → +20.*

### Patrimoine à déclarer

| Élément | Prix |
|---|---|
| Portefeuille de titres | 100 pour le 1er, +20 par suivant |
| Immobilier en Suisse | 80 pour le 1er bien, +20 par suivant |
| Immobilier à l'étranger (case, sans quantité) | +80 |
| 3e pilier — 1er contrat | inclus |
| 3e pilier — chaque contrat supplémentaire | +10 |
| Participation dans une société (> 10 %) | +40 par société |
| Cryptomonnaies | +100 |

### Éléments particuliers et documents

| Élément | Prix |
|---|---|
| Succession / héritage | +200 |
| Frais de formation | 0 |
| Documents prêts / Documents à compléter | 0 |
| Documents à organiser | +60 |

*Exemple : Genève · marié(e) · déclaration commune · 3 enfants → 220 + 30 + 20 = 270.*

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
