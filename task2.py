from math import fabs



vowels = ("a", "e", "i", "o", "u")
firstChar = input("Digite uma letra: ")

if (firstChar.lower() in vowels):
    print("É uma vogal.")
else:
    print("Não é uma vogal.")
