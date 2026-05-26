# File: generate_restant.py - Liste des mots encore en anglais (sans doublons) -> restant_{lang}.json
# Desc: Usage: python3 generate_restant.py --lang fr
#       Lit emoji_usa.json + emoji_fr_current.json, sort {"word": ""} pour chaque mot encore identique (à traduire).
# Version 1.0.0 | Copyright 2025 DNAvatar.org - Arnaud Maignan

import argparse
import json
import os

WIP = os.path.dirname(os.path.abspath(__file__))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="fr", help="Code langue (ex: fr)")
    args = ap.parse_args()
    lang = args.lang

    usa_path = os.path.join(WIP, "emoji_usa.json")
    current_path = os.path.join(WIP, "emoji_" + lang + "_current.json")
    out_path = os.path.join(WIP, "restant_" + lang + ".json")

    with open(usa_path, "r", encoding="utf-8") as f:
        usa = json.load(f)
    with open(current_path, "r", encoding="utf-8") as f:
        current = json.load(f)

    restants = {}
    for emoji, en_kws in usa.items():
        cur_kws = current.get(emoji) or []
        for i, w in enumerate(en_kws):
            if i < len(cur_kws) and cur_kws[i] == w:
                restants[w] = ""

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(restants, f, ensure_ascii=False, indent=2)
    print("restant_" + lang + ".json écrit:", len(restants), "mots à traduire.")


if __name__ == "__main__":
    main()
