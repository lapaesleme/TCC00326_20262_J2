matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def soma_diagonais(matriz):
    soma_principal = 0
    soma_secundaria = 0
    linhas = len(matriz)
    for i in range(0, len(matriz)):
        soma_principal += matriz[i][i]
    for i in range(len(matriz) - 1, -1, -1):
        soma_secundaria += matriz[i][linhas - i - 1]
    return {"principal": soma_principal, "secundaria": soma_secundaria}


print(soma_diagonais(matriz))

print(list(range(len(matriz) - 1, 0, -1)))
