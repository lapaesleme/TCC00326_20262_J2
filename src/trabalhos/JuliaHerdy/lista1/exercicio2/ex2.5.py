palavra = input("Digite uma palavra: ")

contador = 0
vogais = ["a", "e", "i", "o", "u"]

for letra in palavra:
    if letra in vogais:
        contador += 1
print(contador)
