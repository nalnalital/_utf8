# File: build_lang.py - Complète le JS langue sans écraser (fusion restant_{lang}.json + état courant)
# Desc: Usage: python3 build_lang.py --lang fr
#       Lit emoji_usa.json, emoji_fr_current.json, restant_fr.json (rempli); fusionne et écrit utf8_search_fr.js.
# Version 1.0.0 | Copyright 2025 DNAvatar.org - Arnaud Maignan

import argparse
import json
import os

WIP = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(WIP)


def escape_js(s):
    return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "\\r") + '"'


FOOTER = """
// Fonction helper pour obtenir les mots-clés d'un emoji
function getEmojiKeywords(emoji) {
    return emojiKeywords[emoji] || [];
}

// Fonction helper pour rechercher des emojis par mot-clé
function searchEmojisByKeyword(keyword) {
    const results = [];
    const lowerKeyword = keyword.toLowerCase();
    for (const [emoji, keywords] of Object.entries(emojiKeywords)) {
        if (keywords.some(k => k.toLowerCase().includes(lowerKeyword))) {
            results.push(emoji);
        }
    }
    return results;
}

if (typeof module !== 'undefined' && module.exports) {
    module.exports = { emojiKeywords, getEmojiKeywords, searchEmojisByKeyword };
}
if (typeof window !== 'undefined') {
    window.emojiKeywords = emojiKeywords;
    window.getEmojiKeywords = getEmojiKeywords;
    window.searchEmojisByKeyword = searchEmojisByKeyword;
}
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="fr", help="Code langue (ex: fr)")
    args = ap.parse_args()
    lang = args.lang

    usa_path = os.path.join(WIP, "emoji_usa.json")
    current_path = os.path.join(WIP, "emoji_" + lang + "_current.json")
    restant_path = os.path.join(WIP, "restant_" + lang + ".json")
    out_js = os.path.join(ROOT, "utf8_search_" + lang + ".js")

    with open(usa_path, "r", encoding="utf-8") as f:
        usa = json.load(f)
    with open(current_path, "r", encoding="utf-8") as f:
        current = json.load(f)
    with open(restant_path, "r", encoding="utf-8") as f:
        trad = json.load(f)

    merged = {}
    for emoji, en_kws in usa.items():
        cur_kws = current.get(emoji) or en_kws
        fr_kws = []
        for i, en_w in enumerate(en_kws):
            cur_val = cur_kws[i] if i < len(cur_kws) else en_w
            if en_w in trad and trad[en_w] and str(trad[en_w]).strip():
                fr_kws.append(str(trad[en_w]).strip())
            else:
                fr_kws.append(cur_val)
        merged[emoji] = fr_kws

    lines = [
        "// File: utf8_search_" + lang + ".js - Mots-clés emoji",
        "// Desc: Généré par wip/build_lang.py --lang " + lang + " (fusion, pas d’écrasement).",
        "// Version 1.0.0 | Copyright 2025 DNAvatar.org - Arnaud Maignan",
        "",
        "var emojiKeywords = {",
    ]
    entries = list(merged.items())
    for i, (emoji, kws) in enumerate(entries):
        part = "    " + json.dumps(emoji, ensure_ascii=False) + ": [" + ", ".join(escape_js(k) for k in kws) + "]"
        lines.append(part + ("," if i < len(entries) - 1 else ""))
    lines.append("};")
    lines.append(FOOTER)

    with open(out_js, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print("Écrit:", out_js, "(" + str(len(entries)) + " emojis, fusionné).")


if __name__ == "__main__":
    main()
