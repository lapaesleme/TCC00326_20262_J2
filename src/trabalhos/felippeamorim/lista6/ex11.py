def conta_ocorrencias(matriz, valor):
    if not matriz:
        return 0, []

    contagem = 0
    posicoes = []

    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                contagem += 1
                posicoes.append((i, j))

    return contagem, posicoes


# Exemplo
M = [[1, 2, 1], [3, 1, 4]]
cont, pos = conta_ocorrencias(M, 1)
print(f"Ocorrências: {cont}, Posições: {pos}")
# Saída: Ocorrências: 3, Posições: [(0, 0), (0, 2), (1, 1)]