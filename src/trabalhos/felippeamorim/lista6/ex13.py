def troca_linhas(matriz, l1, l2):
    if not matriz: return "Matriz vazia"
    linhas = len(matriz)
    if l1 < 0 or l1 >= linhas or l2 < 0 or l2 >= linhas:
        return "Erro: Índice de linha inválido."

    nova_matriz = [linha[:] for linha in matriz]  # Copia profunda
    nova_matriz[l1], nova_matriz[l2] = nova_matriz[l2], nova_matriz[l1]
    return nova_matriz


def troca_colunas(matriz, c1, c2):
    if not matriz: return "Matriz vazia"
    linhas = len(matriz)
    colunas = len(matriz[0])
    if c1 < 0 or c1 >= colunas or c2 < 0 or c2 >= colunas:
        return "Erro: Índice de coluna inválido."

    nova_matriz = [linha[:] for linha in matriz]
    for i in range(linhas):
        nova_matriz[i][c1], nova_matriz[i][c2] = nova_matriz[i][c2], nova_matriz[i][c1]
    return nova_matriz


# Exemplo
M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Troca Linhas (0 e 2):", troca_linhas(M, 0, 2))
print("Troca Colunas (0 e 1):", troca_colunas(M, 0, 1))