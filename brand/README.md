# Logo — Somfy RTS (RFXtrx)

Logo **original** de l'intégration. Aucune marque, logo ou mention « by Somfy » :
« Somfy RTS » est employé uniquement comme **nom du protocole** piloté (usage nominatif).
L'intégration n'est **pas** développée par Somfy.

## Concept

Volet roulant + ondes radio (le volet est piloté par radio : protocole RTS via un RFXtrx).

## Palette

| Rôle | Couleur |
|---|---|
| Fond badge (haut) | `#1B2A4A` |
| Fond badge (bas)  | `#0E1830` |
| Cyan principal    | `#22D3EE` |
| Cyan clair (accent) | `#67E8F9` |
| Mot-marque (texte)| `#1B2A4A` |
| Sous-titre        | `#0E9BB8` |

Police du mot-marque : Segoe UI / Arial Bold (sans-serif système).

## Fichiers

| Fichier | Dimensions | Usage |
|---|---|---|
| `icon.svg` / `icon.png` / `icon@2x.png` | 256² / 512² | Icône carrée (HA arrondit les coins) |
| `logo.svg` / `logo.png` / `logo@2x.png` | 512×160 / 1024×320 | Logo paysage (fond transparent) |

Les PNG sont régénérables depuis les SVG :

```powershell
magick -background none icon.svg icon@2x.png
magick -background none icon.svg -resize 256x256 icon.png
magick -background none -density 60  logo.svg logo.png
magick -background none -density 120 logo.svg -resize 1024x320 logo@2x.png
```

## Faire afficher le logo dans Home Assistant

HA ne lit pas le logo depuis ce dépôt : il le récupère depuis le dépôt
**`home-assistant/brands`**. Pour une intégration **custom**, déposer les images
sous `custom_integrations/somfy_rts/` :

1. Fork de `https://github.com/home-assistant/brands`.
2. Créer `custom_integrations/somfy_rts/icon.png` (+ `icon@2x.png`) et,
   optionnellement, `logo.png` (+ `logo@2x.png`).
3. Ouvrir une PR. Une fois mergée, HA affiche l'icône/logo pour le domaine
   `somfy_rts` (cache CDN : quelques heures).

Tant que la PR n'est pas mergée, HA montre l'icône puzzle générique — c'est normal.
