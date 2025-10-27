# Écrivez un programme Python pour convertir les températures vers et depuis Celsius et Fahrenheit.

temp = input("Entrez la température à convertir exemple (32F, 100C, etc ...): ")

def celsius(temp) : 
    return (temp - 32) * 5/9

def fahrenheit(temp) : 
    return (temp * 9/5) + 32

if temp[-1] in ['C', 'c'] :
    converted = fahrenheit(float(temp[:-1]))
    print(f"{temp[:-1]}C est égal à {converted}F")
elif temp[-1] in ['F', 'f'] :
    converted = celsius(float(temp[:-1]))
    print(f"{temp[:-1]}F est égal à {converted}C") 

#le terme "temp[:-1]" permet de prendre toute la chaîne de caractères sauf le dernier caractère qui est l'unité de température .