import difflib

class Dictionnaire:
    def __init__(self):
        self.donnees = {}

    def ajouter_mot(self, mot, definition):
        self.donnees[mot] = {"definition": definition, "consultations": 0}

    def modifier_mot(self, mot, nouvelle_definition):
        if mot in self.donnees:
            self.donnees[mot]["definition"] = nouvelle_definition
        else:
            print(f"Le mot '{mot}' n'existe pas.")

    def supprimer_mot(self, mot):
        if mot in self.donnees:
            del self.donnees[mot]
        else:
            print(f"Le mot '{mot}' n'existe pas.")

    def consulter_mot(self, mot):
        if mot in self.donnees:
            self.donnees[mot]["consultations"] += 1
            return self.donnees[mot]["definition"]
        else:
            suggestions = difflib.get_close_matches(mot, self.donnees.keys(), n=3)
            return f"Le mot '{mot}' n'existe pas. Suggestions : {', '.join(suggestions)}"

    def lister_mots_par_ordre_alphabetique(self):
        return sorted(self.donnees.keys())