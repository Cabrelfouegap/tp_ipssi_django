# On vous donne une chaîne s. Le score d'une chaîne est défini comme la somme de la différence absolue entre les valeurs ASCII des caractères adjacents.

s = input("Entrez une chaîne de caractères: ")

def score_chaine(s):
    score = 0
    for i in range(len(s) - 1):
        score += abs(ord(s[i]) - ord(s[i + 1]))
    return score

print("Le score de la chaîne est:", score_chaine(s))

# la fonction ord () permet de récupérer la valeur ASCII d'un caractère.