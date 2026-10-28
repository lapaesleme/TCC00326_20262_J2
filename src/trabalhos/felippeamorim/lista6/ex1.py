def soma_matrizes(m1, m2):
    if not m1 or not m2:
        return "Erro: Matrizes não podem ser vazias."

    linhas_m1 = len(m1)
    colunas_m1 = len(m1[0])
    linhas_m2 = len(m2)
    colunas_m2 = len(m2[0])

    if linhas_m1 != linhas_m2 or colunas_m1 != colunas_m2:
        return "Erro: Matrizes com dimensões incompatíveis para soma."

    # Verifica se todas as linhas têm o mesmo tamanho
    for linha in m1:
        if len(linha) != colunas_m1:
            return "Erro: A primeira matriz não é regular."
    for linha in m2:
        if len(linha) != colunas_m2:
            return "Erro: A segunda matriz não é regular."

    m3 = []
    for i in range(linhas_m1):
        linha_soma = []
        for j in range(colunas_m1):
            linha_soma.append(m1[i][j] + m2[i][j])
        m3.append(linha_soma)
    return m3


# Exemplo de uso
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = [[1, 2, 3], [4, 5, 6]]

print(soma_matrizes(A, B))  # Saída: [[6, 8], [10, 12]]
print(soma_matrizes(A, C))  # Saída: Erro: Matrizes com dimensões incompatíveis para soma.