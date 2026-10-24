def busca_matriz_ordenada(matriz, alvo):
    if not matriz:
        return "Matriz vazia."

    linhas = len(matriz)
    colunas = len(matriz[0])

    i = 0
    j = colunas - 1  # Começa no canto superior direito

    while i < linhas and j >= 0:
        if matriz[i][j] == alvo:
            return (i, j)
        elif matriz[i][j] > alvo:
            j -= 1  # Move para a esquerda
        else:
            i += 1  # Move para baixo

    return "Elemento não existe na matriz."


# Exemplo
M = [[1, 4, 7, 11],
     [2, 5, 8, 12],
     [3, 6, 9, 16],
     [10, 13, 14, 17]]
print("Posição de 5:", busca_matriz_ordenada(M, 5))
print("Posição de 20:", busca_matriz_ordenada(M, 20))