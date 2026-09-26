def filtrar_itens(lista, criterio):
    resultado = []

    for item in lista:
        if criterio(item):
            resultado.append(item)

    return resultado


# Critério 1: números pares
def eh_par(numero):
    return numero % 2 == 0


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Números pares:")
print(filtrar_itens(numeros, eh_par))


# Critério 2: valores acima da média
def acima_da_media(numero):
    media = sum(numeros) / len(numeros)
    return numero > media


print("Valores acima da média:")
print(filtrar_itens(numeros, acima_da_media))


# Critério 3: palavras com mais de 7 letras
def mais_de_sete_letras(palavra):
    return len(palavra) > 7


palavras = [
    "computador",
    "casa",
    "programação",
    "python",
    "faculdade",
    "exercicio"
]

print("Palavras com mais de 7 letras:")
print(filtrar_itens(palavras, mais_de_sete_letras))
