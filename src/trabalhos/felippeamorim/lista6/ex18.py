def calcular_caminhos(grade):
    if not grade: return 0

    linhas = len(grade)
    colunas = len(grade[0])

    # Se o ponto de partida ou de chegada for um obstáculo, não há caminho
    if grade[0][0] == 1 or grade[linhas - 1][colunas - 1] == 1:
        return 0

    # Matriz para armazenar o número de caminhos até cada célula
    dp = []
    for _ in range(linhas):
        dp.append([0] * colunas)

    dp[0][0] = 1

    # Preenche a primeira coluna
    for i in range(1, linhas):
        if grade[i][0] == 0:
            dp[i][0] = dp[i - 1][0]

    # Preenche a primeira linha
    for j in range(1, colunas):
        if grade[0][j] == 0:
            dp[0][j] = dp[0][j - 1]

    # Preenche o resto da matriz
    for i in range(1, linhas):
        for j in range(1, colunas):
            if grade[i][j] == 0:  # Posição livre
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[linhas - 1][colunas - 1]


# Exemplo (0 = livre, 1 = obstáculo)
grade = [[0, 0, 0],
         [0, 1, 0],
         [0, 0, 0]]
print("Caminhos possíveis:", calcular_caminhos(grade))