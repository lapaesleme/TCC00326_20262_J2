def filtrar_palavras(palavras, tamanho_minimo):
    resultado = []

    for palavra in palavras:
        if len(palavra) >= tamanho_minimo:
            resultado.append(palavra)

    return resultado


palavras = ["casa", "computador", "sol", "python", "oi"]

tamanho = int(input("Digite o tamanho mínimo: "))

resultado = filtrar_palavras(palavras, tamanho)

print(resultado)