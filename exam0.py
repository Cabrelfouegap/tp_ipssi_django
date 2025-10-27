#Étant donné une chaîne s composée de mots et d’espaces, renvoie la longueur du dernier mot de la chaîne.
#Un mot est une sous-chaîne composé uniquement de caractères autres que des espaces.

s = input("Entrez une chaîne de caractères: ")
def longueur_mot(s):
    s = s.strip()  # Supprime les espaces au début et à la fin de la chaîne
    mots = s.split(' ')  # Divise la chaîne en mots
    if mots:
        return len(mots[-1])  # Retourne la longueur du dernier mot
    return 0  # Si la chaîne est vide, retourne 0

print(longueur_mot(s))