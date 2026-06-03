<p align="center">
  <img src="brand/logo.png" alt="Somfy RTS (RFXtrx)" width="420">
</p>

# Somfy RTS (RFXtrx) — intégration Home Assistant

Intégration personnalisée pour piloter des volets / stores **Somfy RTS** depuis Home Assistant via un transmetteur **RFXtrx**.

Cette intégration s'appuie sur l'intégration officielle [`rfxtrx`](https://www.home-assistant.io/integrations/rfxtrx/) pour envoyer les trames RFY au protocole Somfy RTS, et expose pour chaque volet :

- une entité `cover` (commandes **Open / Close / Stop**),
- un bouton **Programme** (appairage de la télécommande virtuelle au moteur),
- un bouton **My** (position favorite Somfy).

## Pré-requis

- Home Assistant **2024.1** ou plus récent.
- Un transmetteur **RFXtrx** (USB ou Ethernet) configuré et fonctionnel dans Home Assistant via l'intégration officielle `rfxtrx`.
- L'intégration `rfxtrx` doit exposer le service `rfxtrx.send` (comportement par défaut).

## Installation

### Via HACS (recommandé)

1. Ouvrir HACS → **Intégrations** → menu ⋯ → **Custom repositories**.
2. Ajouter l'URL `https://github.com/droos-gh/somfy-rts-rfxtrx` avec la catégorie **Integration**.
3. Installer **Somfy RTS (RFXtrx)**, puis redémarrer Home Assistant.

### Manuelle

Copier le dossier `custom_components/somfy_rts/` dans le dossier `config/custom_components/` de votre installation Home Assistant, puis redémarrer.

## Configuration

1. **Paramètres** → **Appareils et services** → **Ajouter une intégration** → rechercher **Somfy RTS**.
2. Donner un nom au volet (ex. *Volet salon*).
3. Un identifiant RFX unique (`device_id` sur 24 bits) est généré automatiquement.
4. Sur le moteur Somfy, lancer le mode d'appairage (appui long sur la touche **PROG** d'une télécommande déjà mémorisée — voir la doc Somfy de votre moteur).
5. Dans Home Assistant, appuyer sur le bouton **Programme** de l'entité créée : le moteur doit confirmer (court va-et-vient).

Le volet répond ensuite aux commandes **Open / Close / Stop** et au bouton **My**.

## Notes

- Le protocole RTS est **unidirectionnel** : Home Assistant ne reçoit aucun retour d'état du moteur. L'état des entités `cover` est donc toujours *inconnu* (`assumed_state`).
- Chaque entrée de configuration = un canal Somfy RTS distinct (`unit` fixé à `01`, `device_id` aléatoire et unique parmi les entrées existantes).

## Logo / Marque

Les visuels de l'intégration se trouvent dans [`brand/`](brand/) (sources SVG +
PNG, voir [`brand/README.md`](brand/README.md)) :

| Asset | Dimensions | Usage |
|---|---|---|
| `brand/icon.png` / `icon@2x.png` | 256² / 512² | Icône carrée |
| `brand/logo.png` / `logo@2x.png` | 512×160 / 1024×320 | Logo paysage |

Concept : volet roulant + ondes radio (pilotage par radio), palette bleu nuit
`#1B2A4A` / cyan `#22D3EE`.

Pour que Home Assistant affiche réellement l'icône/logo, déposer les PNG dans le
dépôt [`home-assistant/brands`](https://github.com/home-assistant/brands) sous
`custom_integrations/somfy_rts/` (via une PR). Sans cela, HA montre l'icône
puzzle générique.

> **Non-affiliation.** Cette intégration est un projet indépendant. Elle n'est ni
> développée, ni soutenue, ni approuvée par Somfy. « Somfy » et « RTS » sont des
> marques de leurs détenteurs respectifs ; elles ne sont utilisées ici qu'à titre
> descriptif pour désigner le protocole radio piloté.

## Licence

[MIT](LICENSE)
