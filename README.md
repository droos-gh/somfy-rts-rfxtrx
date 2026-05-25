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

## Licence

[MIT](LICENSE)
