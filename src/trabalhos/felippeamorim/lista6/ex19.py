def filtro_vizinhanca(matriz):
    if not matriz or len(matriz) < 3 or len(matriz[0]) < 3:
        return "Erro: Matriz pequena demais para aplicar o filtro."

    linhas = len(matriz)
    colunas = len(matriz[0])

    # Cria uma nova matriz copiando os valores originais
    nova_matriz = [linha[:] for linha in matriz]

    for i in range(1, linhas - 1):
        for j in range(1, colunas - 1):
            soma = (matriz[i - 1][j - 1] + matriz[i - 1][j] + matriz[i - 1][j + 1] +
                    matriz[i][j - 1] + matriz[i][j] + matriz[i][j + 1] +
                    matriz[i + 1][j - 1] + matriz[i + 1][j] + matriz[i + 1][j + 1])
            nova_matriz[i][j] = round(soma / 9, 2)  # Calcula a média e arredonda

    return nova_matriz


# Exemplo
M = [[1, 1, 1, 1],
     [1, 9, 9, 1],
     [1, 9, 9, 1],
     [1, 1, 1, 1]]
res = filtro_vizinhanca(M)
for l in res: print(l)