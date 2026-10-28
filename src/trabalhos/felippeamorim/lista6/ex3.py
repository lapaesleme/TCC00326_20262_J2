def soma_diagonais(matriz):
    if not matriz:
        return "Erro: Matriz vazia."

    n = len(matriz)
    # Verifica se é quadrada
    for linha in matriz:
        if len(linha) != n:
            return "Erro: A matriz não é quadrada."

    soma_principal = 0
    soma_secundaria = 0

    for i in range(n):
        soma_principal += matriz[i][i]
        soma_secundaria += matriz[i][n - 1 - i]

    diferenca = abs(soma_principal - soma_secundaria)

    return {
        "soma_principal": soma_principal,
        "soma_secundaria": soma_secundaria,
        "diferenca_absoluta": diferenca
    }


# Exemplo
Quad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(soma_diagonais(Quad))
# Saída: {'soma_principal': 15, 'soma_secundaria': 15, 'diferenca_absoluta': 0}