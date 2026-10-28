def multiplica_matrizes(m1, m2):
    if not m1 or not m2:
        return "Erro: Matrizes não podem ser vazias."

    linhas_m1 = len(m1)
    colunas_m1 = len(m1[0])
    linhas_m2 = len(m2)
    colunas_m2 = len(m2[0])

    if colunas_m1 != linhas_m2:
         return f"Erro: Incompatível. Colunas M1 ({colunas_m1}) != Linhas M2 ({linhas_m2})."

    # Validação (opcional)
    for linha in m1:
        if len(linha) != colunas_m1: return "Erro: M1 irregular"
    for linha in m2:
        if len(linha) != colunas_m2: return "Erro: M2 irregular"

    # Inicializa a matriz resultado (linhas_m1 x colunas_m2) com zeros
    resultado = []
    for _ in range(linhas_m1):
        linha_zero = []
        for _ in range(colunas_m2):
            linha_zero.append(0)
        resultado.append(linha_zero)

    # Multiplicação
    for i in range(linhas_m1):
        for j in range(colunas_m2):
            for k in range(colunas_m1): # ou linhas_m2
                resultado[i][j] += m1[i][k] * m2[k][j]

    return resultado

# Exemplo
A = [[1, 2, 3], [4, 5, 6]] # 2x3
B = [[7, 8], [9, 10], [11, 12]] # 3x2
print(multiplica_matrizes(A, B)) # Saída: [[58, 64], [139, 154]]