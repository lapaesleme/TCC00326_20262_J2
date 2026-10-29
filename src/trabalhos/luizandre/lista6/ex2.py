matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [7, 8, 9]
]


# colunas = len(matriz[0])
# linhas = len(matriz)


# m = [[0] * linhas] * colunas
# print(m)


def transposta(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    resultado = [[0 for j in range(linhas)] for i in range(colunas)]
    print(resultado)

    for i in range(0, linhas):
        for j in range(0, colunas):
            resultado[j][i] = matriz[i][j]
    return resultado


print(transposta(matriz))

print([[0 for j in range(4)] for i in range(2)])

m2 = []
for i in range(4):
    m2.append(0)
print(m2)
