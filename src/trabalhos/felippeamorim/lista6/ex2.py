def matriz_transposta(matriz):
    if not matriz:
        return []

    linhas = len(matriz)
    colunas = len(matriz[0])

    # Validação (opcional, dependendo do rigor)
    for linha in matriz:
        if len(linha) != colunas:
            return "Erro: A matriz não é regular."

    transposta = []
    for j in range(colunas):
        nova_linha = []
        for i in range(linhas):
            nova_linha.append(matriz[i][j])
        transposta.append(nova_linha)

    return transposta


# Exemplo
M = [[1, 2, 3], [4, 5, 6]]
print(matriz_transposta(M))  # Saída: [[1, 4], [2, 5], [3, 6]]