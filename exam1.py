# Étant donné une chaîne s, renvoie la plus longue sous-chaîne palindromique dans s

s = input("Entrez une chaîne de caractères: ")

def palyndrome (s):
    max = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j+1] == s[i:j+1][::-1] and len(s[i:j+1]) > len(max):
                max = s[i:j+1]
    return max
print(palyndrome(s))