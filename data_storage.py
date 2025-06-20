import json  # On importe le module json, qui permet de lire et d'écrire des fichiers au format JSON

FICHIER_JSON = "dictionnaire.json"  # Nom du fichier JSON qui contiendra notre dictionnaire

# Fonction pour charger les données du dictionnaire depuis le fichier JSON
def charger_dictionnaire():
    try:
        # On essaie d'ouvrir le fichier en mode lecture avec l'encodage UTF-8
        with open(FICHIER_JSON, "r", encoding="utf-8") as f:
            return json.load(f)  # Si le fichier existe, on le lit et on retourne le contenu sous forme de dictionnaire
    except FileNotFoundError:
        return {}  # Si le fichier n'existe pas, on retourne un dictionnaire vide

# Fonction pour sauvegarder un dictionnaire dans le fichier JSON
def sauvegarder_dictionnaire(dictionnaire):
    # On ouvre le fichier en mode écriture (ce qui écrasera l'ancien contenu s'il existe)
    with open(FICHIER_JSON, "w", encoding="utf-8") as f:
        # On écrit le dictionnaire dans le fichier en format JSON, avec une indentation pour la lisibilité
        json.dump(dictionnaire, f, indent=4, ensure_ascii=False)
