# Merge trad_en_fr.tsv into restant_fr.json (fill values), then run build_lang.
import json
import os
import subprocess

WIP = os.path.dirname(os.path.abspath(__file__))
restant_path = os.path.join(WIP, "restant_fr.json")
tsv_path = os.path.join(WIP, "trad_en_fr.tsv")

with open(restant_path, "r", encoding="utf-8") as f:
    restant = json.load(f)
with open(tsv_path, "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\n")
        if "\t" not in line:
            continue
        key, val = line.split("\t", 1)
        if key in restant:
            restant[key] = val.strip()

with open(restant_path, "w", encoding="utf-8") as f:
    json.dump(restant, f, ensure_ascii=False, indent=2)
print("restant_fr.json rempli depuis trad_en_fr.tsv.")

subprocess.run(["python3", os.path.join(WIP, "build_lang.py"), "--lang", "fr"], check=True)
