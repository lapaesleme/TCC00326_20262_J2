def soma_maxima_2x2(matriz):
    if not matriz or len(matriz) < 2 or len(matriz[0]) < 2:
        return "Erro: Matriz deve ter pelo menos 2 linhas e 2 colunas."

    linhas = len(matriz)
    colunas = len(matriz[0])

    # Inicializa com a primeira submatriz possível
    max_soma = float('-inf')
    melhor_posicao = (0, 0)
    melhores_elementos = []

    for i in range(linhas - 1):
        for j in range(colunas - 1):
            elem1 = matriz[i][j]
            elem2 = matriz[i][j + 1]
            elem3 = matriz[i + 1][j]
            elem4 = matriz[i + 1][j + 1]

            soma_atual = elem1 + elem2 + elem3 + elem4

            if soma_atual > max_soma:
                max_soma = soma_atual
                melhor_posicao = (i, j)
                melhores_elementos = [[elem1, elem2], [elem3, elem4]]

    return {
        "soma": max_soma,
        "elementos": melhores_elementos,
        "posicao_inicial": melhor_posicao
    }


# Exemplo
M = [[1, 2, 3], [4, 5, -6], [-7, 8, 9]]
print(soma_maxima_2x2(M))
# Saída: {'soma': 16, 'elementos': [[5, -6], [8, 9]], 'posicao_inicial': (1, 1)}