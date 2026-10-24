numeros = []

with open("numeros.txt", "r") as arquivo:
    for linha in arquivo:
        if linha.strip() != "":
            numero = float(linha)
            numeros.append(numero)

if len(numeros) > 0:
    quantidade = len(numeros)
    soma = sum(numeros)
    media = soma / quantidade

    print("Quantidade:", quantidade)
    print("Soma:", soma)
    print("Média:", media)
    print("Menor:", min(numeros))
    print("Maior:", max(numeros))
else:
    print("Nenhum número encontrado.")