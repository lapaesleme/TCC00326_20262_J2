palavra = str(input("Digite uma palavra: "))
qntd_vogais = 0
for letra in palavra:
    if letra in "aeiou":
        qntd_vogais += 1
    else:
        qntd_vogais += 0
print(qntd_vogais)