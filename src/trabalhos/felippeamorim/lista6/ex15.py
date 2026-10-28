def bordas_matriz(matriz):
    if not matriz or len(matriz) < 3 or len(matriz[0]) < 3:
        return "Erro: A matriz deve ter pelo menos 3 linhas e 3 colunas."

    linhas = len(matriz)
    colunas = len(matriz[0])
    elementos_borda = []
    soma_borda = 0

    for i in range(linhas):
        for j in range(colunas):
            # Elemento pertence à borda se estiver na primeira/última linha ou coluna
            if i == 0 or i == linhas - 1 or j == 0 or j == colunas - 1:
                elementos_borda.append(matriz[i][j])
                soma_borda += matriz[i][j]

    return {"elementos": elementos_borda, "soma": soma_borda}

# Exemplo
M = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12]]
print(bordas_matriz(M))