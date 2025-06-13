
from dictionary_core import Dictionnaire
from data_storage import charger_dictionnaire, sauvegarder_dictionnaire 
from advanced_features import recherche_par_mot_cle, statistiques_dictionnaire
from export_bonus import exporter_txt, exporter_csv 

def main():
    dictionnaire = Dictionnaire()
    dictionnaire.donnees = charger_dictionnaire()

    while True:
        print("\nMenu:")
        print("1. Ajouter un mot")
        print("2. Modifier un mot")
        print("3. Supprimer un mot")
        print("4. Consulter un mot")
        print("5. Liste des mots alphabétiques")
        print("6. Recherche avancée")
        print("7. Afficher statistiques")
        print("8. Exporter en TXT")
        print("9. Exporter en CSV")
        print("10. Quitter")

        choix = input("Choisissez une option: ").strip()

        if choix == "1":
            mot = input("Entrez le mot: ").strip()
            definition = input("Entrez la définition: ").strip()
            dictionnaire.ajouter_mot(mot, definition)
            sauvegarder_dictionnaire(dictionnaire.donnees)

        elif choix == "2":
            mot = input("Entrez le mot à modifier: ").strip()
            nouvelle_definition = input("Entrez la nouvelle définition: ").strip()
            dictionnaire.modifier_mot(mot, nouvelle_definition)
            sauvegarder_dictionnaire(dictionnaire.donnees)

        elif choix == "3":
            mot = input("Entrez le mot à supprimer: ").strip()
            dictionnaire.supprimer_mot(mot)
            sauvegarder_dictionnaire(dictionnaire.donnees)

        elif choix == "4":
            mot = input("Entrez le mot à consulter: ").strip()
            print(dictionnaire.consulter_mot(mot))

        elif choix == "5":
            print("\n".join(dictionnaire.lister_mots_par_ordre_alphabetique()))

        elif choix == "6":
            mot_cle = input("Entrez le mot-clé: ").strip()
            print(recherche_par_mot_cle(dictionnaire.donnees, mot_cle))

        elif choix == "7":
            stats = statistiques_dictionnaire(dictionnaire.donnees)
            for key, value in stats.items():
                print(f"{key}: {value}")

        elif choix == "8":
            exporter_txt(dictionnaire.donnees)

        elif choix == "9":
            exporter_csv(dictionnaire.donnees)

        elif choix == "10":
            print("Au revoir!")
            break

        else:
            print("Option invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()