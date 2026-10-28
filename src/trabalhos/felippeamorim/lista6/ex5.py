def is_simetrica(matriz):
    if not matriz:
        return False

    n = len(matriz)

    # Primeiro verifica se é quadrada
    for linha in matriz:
        if len(linha) != n:
            return False  # Não quadrada não pode ser simétrica

    # Compara a[i][j] com a[j][i]
    for i in range(n):
        for j in range(i + 1, n):  # Otimização: verifica só acima da diagonal
            if matriz[i][j] != matriz[j][i]:
                return False

    return True


# Exemplo
S1 = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
S2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(is_simetrica(S1))  # True
print(is_simetrica(S2))  # False