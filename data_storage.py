import json

FICHIER_JSON = "dictionnaire.json"

def charger_dictionnaire():
    try:
        with open(FICHIER_JSON, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def sauvegarder_dictionnaire(dictionnaire):
    with open(FICHIER_JSON, "w", encoding="utf-8") as f:
        json.dump(dictionnaire, f, indent=4, ensure_ascii=False)
