def filtrar_palavras(lista, tamanho_minimo):
    nova_lista = []
    for palavra in lista:
        if len(palavra) >= tamanho_minimo:
            nova_lista.append(palavra)
    return nova_lista
palavras = ["casa", "computador", "sol", "python"]
resultado = filtrar_palavras(palavras,5)
print(resultado)