arquivo = open("nomes.txt", "r")

numero = 1

for linha in arquivo:
    print(numero, "-", linha.strip())
    numero += 1

arquivo.close()