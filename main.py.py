from dictionary_core import Dictionnaire  # Classe principale du dictionnaire
from data_storage import charger_dictionnaire, sauvegarder_dictionnaire  # Pour lire/sauvegarder les données
from advanced_features import recherche_par_mot_cle, statistiques_dictionnaire  # Fonctions avancées
from export_bonus import exporter_txt, exporter_csv  # Fonctions d'exportation

Fonction principale
def main():
    dictionnaire = Dictionnaire()  # Crée une instance du dictionnaire
    dictionnaire.donnees = charger_dictionnaire()  # Charge les données enregistrées

    while True:
        # Menu d'options
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

        choix = input("Choisissez une option: ").strip()  # Choix de l'utilisateur

        if choix == "1":
            # Ajouter un mot
            mot = input("Entrez le mot: ").strip()
            definition = input("Entrez la définition: ").strip()
            dictionnaire.ajouter_mot(mot, definition)
            sauvegarder_dictionnaire(dictionnaire.donnees)  # Sauvegarde

        elif choix == "2":
            # Modifier un mot existant
            mot = input("Entrez le mot à modifier: ").strip()
            nouvelle_definition = input("Entrez la nouvelle définition: ").strip()
            dictionnaire.modifier_mot(mot, nouvelle_definition)
            sauvegarder_dictionnaire(dictionnaire.donnees)

        elif choix == "3":
            # Supprimer un mot
            mot = input("Entrez le mot à supprimer: ").strip()
            dictionnaire.supprimer_mot(mot)
            sauvegarder_dictionnaire(dictionnaire.donnees)

        elif choix == "4":
            # Consulter un mot (affiche la définition)
            mot = input("Entrez le mot à consulter: ").strip()
            print(dictionnaire.consulter_mot(mot))

        elif choix == "5":
            # Liste les mots par ordre alphabétique
            print("\n".join(dictionnaire.lister_mots_par_ordre_alphabetique()))

        elif choix == "6":
            # Recherche dans les définitions
            mot_cle = input("Entrez le mot-clé: ").strip()
            print(recherche_par_mot_cle(dictionnaire.donnees, mot_cle))

        elif choix == "7":
            # Affiche des statistiques sur le dictionnaire
            stats = statistiques_dictionnaire(dictionnaire.donnees)
            for key, value in stats.items():
                print(f"{key}: {value}")

        elif choix == "8":
            # Exporter les données en fichier texte
            exporter_txt(dictionnaire.donnees)

        elif choix == "9":
            # Exporter les données en CSV
            exporter_csv(dictionnaire.donnees)

        elif choix == "10":
            # Quitte le programme
            print("Au revoir!")
            break

        else:
            # Erreur de saisie
            print("Option invalide, veuillez réessayer.")

Point d’entrée du programme
if name == "main":
    main()

