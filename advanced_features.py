import random

def rechercher_par_mot_cle(dictionnaire, mot_cle):
    return{ details["definition"] for mot, details in dictionnaire.items() if mot_cle.lower() in details["definition"].lower()}

def statistiques_dictionnaire(dictionnaire):
    total_mots= len(dictionnaire)
    mot_le_plus_long=max(dictionnaire.keys(), key=len, default="aucun")
    mot_le_plus_court= min(dictionnaire.keys(), keys=len, default="aucun")

    if dictionnaire:
        mot_aleatoire= random.choice(list(dictionnaire.keys()))
        definition_aleatoire=dictionnaire[mot_aleatoire]["definition"]
    else :
        mot_aleatoire, definition_aleatoire="aucun","aucune definition disponible"

    return {
    "total_mots": total_mots,
    "mot_le_plus_long": mot_le_plus_long ,
    "mot_le_plus_court": mot_le_plus_court,
    "mot_aleatoire": mot_aleatoire,
    "definition_aleatoire": definition_aleatoire
    }




