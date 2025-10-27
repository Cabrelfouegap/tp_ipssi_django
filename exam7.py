#Écrire un programme Python pour compter le nombre de nombres pairs et impairs dans une série de nombres 

numbers = input("Entrez une série de nombres séparés par des virgules: ")
num_list = numbers.split(',')
nbre_pairs = 0
nbre_impairs = 0
for num in num_list:
    if int(num) % 2 == 0:
        nbre_pairs += 1
    else:
        nbre_impairs += 1
print(f"Nombre de nombres pairs: {nbre_pairs}")
print(f"Nombre de nombres impairs: {nbre_impairs}")