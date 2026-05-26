# WIP – Traductions (ne pas publier)

## Fichiers intermédiaires
- `emoji_usa.json` – export de utf8_search_usa.js (source EN)
- `emoji_fr_current.json` – snapshot actuel de utf8_search_fr.js (avant fusion)
- `restant_fr.json` – mots encore en anglais, `{"word": ""}` à remplir (ex. par Gemini)

## Workflow (compléter sans écraser)

1. **Exporter la source et l’état courant**
   ```bash
   node wip/export_usa_json.js
   node wip/export_current.js fr
   ```

2. **Générer la liste des mots restants (sans doublons)**
   ```bash
   python3 wip/generate_restant.py --lang fr
   ```
   → crée `wip/restant_fr.json` (ou utiliser `node wip/mots_restants.js fr`).

3. **Remplir** `wip/restant_fr.json` (Gemini / à la main).

4. **Fusionner et écrire** (ne pas écraser : fusion restant + état courant)
   ```bash
   python3 wip/build_lang.py --lang fr
   ```
   → met à jour `utf8_search_fr.js` en ne remplaçant que les mots traduits.

Pour une autre langue, remplacer `fr` par le code langue (ex. `it`) et adapter les noms de fichiers si besoin.
