import random # pour faire un choix au hasard

# fonction pour chercher les mots dans la definition contient le mot-cle
def rechercher_par_mot_cle(dictionnaire, mot_cle):
     # retourne un ensemble des définitions contenant le mot-clé (en ignorant la casse)
    return{ details["definition"] for mot, details in dictionnaire.items() if mot_cle.lower() in details["definition"].lower()}

# fonction pour donner des infos sur le dictionnaire 
def statistiques_dictionnaire(dictionnaire):
    total_mots= len(dictionnaire) # compte tout les mots
    mot_le_plus_long=max(dictionnaire.keys(), key=len, default="aucun") # le mot le plus long
    mot_le_plus_court= min(dictionnaire.keys(), key=len, default="aucun") # le mot le plus court

    if dictionnaire:  # si le dictionnaire n'est pas vide

        mot_aleatoire= random.choice(list(dictionnaire.keys())) # prend un mot au hasard
        definition_aleatoire=dictionnaire[mot_aleatoire]["definition"]  # récupère sa définition

    else :
        mot_aleatoire, definition_aleatoire="aucun","aucune definition disponible" # valeurs par défaut


    # retourne les infos sous forme de dictionnaire ou renvoie les statistiques
    return {
    "total_mots": total_mots,
    "mot_le_plus_long": mot_le_plus_long ,
    "mot_le_plus_court": mot_le_plus_court,
    "mot_aleatoire": mot_aleatoire,
    "definition_aleatoire": definition_aleatoire
    }




