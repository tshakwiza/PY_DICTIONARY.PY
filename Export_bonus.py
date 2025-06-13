import csv

FICHIER_TXT = "dictionnaire.txt"
FICHIER_CSV = "dictionnaire.csv"

def exporter_txt(dictionnaire):
    with open(FICHIER_TXT, "w", encoding="utf-8") as f:
        for mot, detais in dictionnaire.items():
            f.write(f"{mot}: {details['definition']}\n")

def exporter_csv(dictionnaire):
    with open(FICHIER_CSV, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["mot", "Définition"])
        for mot, details in dictionnaire.items():
            writer.writerow([mot, details['definition']])