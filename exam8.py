# Écrivez un programme Python qui itère les entiers de 1 à 50. Pour les multiples de trois, imprimez « Fizz » au lieu du nombre et pour les multiples de cinq, imprimez « Buzz ». Pour les nombres multiples de trois et cinq, imprimez « FizzBuzz ».

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)