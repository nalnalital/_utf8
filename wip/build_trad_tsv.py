# File: build_trad_tsv.py - Génère trad_en_fr.tsv depuis restant_fr.json (EN -> FR)
# Desc: Lit les clés dans l'ordre, traduit via deep_translator, écrit key\tvalue.
# Version 1.0.0
# Copyright 2025 DNAvatar.org - Arnaud Maignan
# Licensed under Apache License 2.0 with Commons Clause.
# Date: 2025-03-06
# Logs:
# - Initial: read restant_fr.json, translate non-numeric keys, output TSV.

import json
import re
import time
import os

from deep_translator import GoogleTranslator

WIP = os.path.dirname(os.path.abspath(__file__))
RESTANT_PATH = os.path.join(WIP, "restant_fr.json")
OUT_TSV_PATH = os.path.join(WIP, "trad_en_fr.tsv")

# Nombres et formats à garder tels quels (pas de traduction)
NUMERIC_RE = re.compile(r"^\d+$")
TIME_RE = re.compile(r"^\d{1,2}:\d{2}$")
# Lettres seules ou termes très techniques / noms propres identiques
KEEP_AS_IS = frozenset({
    "v", "w", "e", "o", "i", "lgbt", "atm", "dna", "pc", "tv", "vhs", "abc",
    "nba", "nfl", "uae", "uk", "naruto", "hanafuda", "tanabata", "om", "tao",
    "yin", "yang", "dharma", "torii", "onsen", "bento", "onigiri", "ramen",
    "sake", "dango", "oden", "tempura", "hocho", "kaaba", "mecca", "hanukkah",
    "hygieia", "khanda", "nazar", "petri", "covid", "playstation", "deutschland",
    "nippon", "rosette", "formee", "touchtone", "tada", "matsuri",
})


def should_keep_as_is(key: str) -> bool:
    if NUMERIC_RE.match(key) or TIME_RE.match(key):
        return True
    if key.lower() in KEEP_AS_IS:
        return True
    return False


def main():
    with open(RESTANT_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    keys_ordered = list(data.keys())
    translator = GoogleTranslator(source="en", target="fr")
    n = len(keys_ordered)
    with open(OUT_TSV_PATH, "w", encoding="utf-8") as out_f:
        for i, key in enumerate(keys_ordered):
            if should_keep_as_is(key):
                value = key
            else:
                try:
                    value = translator.translate(key)
                    if value is None or not str(value).strip():
                        value = key
                except Exception:
                    value = key
                time.sleep(0.12)
            out_f.write(f"{key}\t{value}\n")
            out_f.flush()
            if (i + 1) % 200 == 0:
                print(f"  {i + 1}/{n}")

    print(f"Written {n} lines to {OUT_TSV_PATH}")


if __name__ == "__main__":
    main()
