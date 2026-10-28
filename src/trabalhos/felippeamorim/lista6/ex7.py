def rotaciona_90(matriz):
    if not matriz:
        return []

    linhas = len(matriz)
    colunas = len(matriz[0])

    # A matriz resultante terá dimensões (colunas x linhas)
    rotacionada = []
    for j in range(colunas):
        nova_linha = []
        for i in range(linhas - 1, -1, -1):  # Lê de baixo para cima
            nova_linha.append(matriz[i][j])
        rotacionada.append(nova_linha)

    return rotacionada


# Exemplo
M = [[1, 2, 3], [4, 5, 6]]
print(rotaciona_90(M))  # Saída: [[4, 1], [5, 2], [6, 3]]