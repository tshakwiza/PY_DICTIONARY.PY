
            import csv  # Importe le module csv pour pouvoir écrire dans un fichier CSV

# Constantes pour les noms de fichiers
FICHIER_TXT = "dictionnaire.txt"  # Nom du fichier texte dans lequel on va écrire
FICHIER_CSV = "dictionnaire.csv"  # Nom du fichier CSV dans lequel on va écrire

# Fonction pour exporter le dictionnaire dans un fichier texte
def exporter_txt(dictionnaire):
    with open(FICHIER_TXT, "w", encoding="utf-8") as f:  # Ouvre le fichier en écriture avec encodage UTF-8
        for mot, details in dictionnaire.items():  # Parcourt chaque mot et sa définition
            f.write(f"{mot}: {details['definition']}\n")  # Écrit le mot et sa définition sur une ligne

# Fonction pour exporter le dictionnaire dans un fichier CSV
def exporter_csv(dictionnaire):
    with open(FICHIER_CSV, "w", encoding="utf-8", newline="") as f:  # Ouvre le fichier CSV avec UTF-8 et sans saut de ligne supplémentaire
        writer = csv.writer(f)  # Crée un objet writer pour écrire dans le fichier CSV
        writer.writerow(["mot", "Définition"])  # Écrit l’en-tête du fichier CSV
        for mot, details in dictionnaire.items():  # Parcourt chaque mot et sa définition
            writer.writerow([mot, details['definition']])  # Écrit chaque mot et sa définition dans une ligne du CSV
