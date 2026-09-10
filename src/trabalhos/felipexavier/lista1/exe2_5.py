palavra = input("digite uma palavra: ")
contador = 0
for letra in palavra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador += 1
print(f"palavra possui {contador} vogais")