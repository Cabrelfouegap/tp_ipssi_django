# Vous recevez un grand entier représenté sous la forme d'un tableau d'entiers digits, où chacun digits[i]est le chiffre de l'entier. Les chiffres sont classés du plus significatif au moins significatif, de gauche à droite. Le grand entier ne contient aucun signe non significatif

# Incrémentez le grand entier de un et renvoyez le tableau de chiffres résultant .

tab = input("entrer un les elements de votre tableau exp: 1, 2, 3 : ").split(',')
tab = [int(i) for i in tab]  
def incrementation (tab):
    # Convertir le tableau de chiffres en un entier
    nombre = int("".join(map(str, tab)))
    # Incrémenter l'entier de un
    nombre += 1
    # Convertir l'entier incrémenté en un tableau de chiffres
    return [int(i) for i in str(nombre)]
print(incrementation(tab))