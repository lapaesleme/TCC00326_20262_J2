palavra = input("Digite uma palavra: ")

contador = 0
for letra in palavra:
    if letra in "aeiou":
        contador = contador + 1

print(" A palavra possui ", contador, "vogais ")
