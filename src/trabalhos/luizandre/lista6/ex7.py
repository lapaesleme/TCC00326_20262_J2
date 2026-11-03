m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]


def rotacao(A):
    linhas = len(A)
    colunas = len(A[0])
    resultado = [[0 for j in range(linhas)] for i in range(colunas)]
    for i in range(0, linhas):
        for j in range(0, colunas):
            resultado[j][linhas - i - 1] = A[i][j]
    return resultado


print(rotacao(m1))
