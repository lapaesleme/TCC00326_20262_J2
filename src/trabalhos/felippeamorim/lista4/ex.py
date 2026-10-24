def determinante(A):
    n = len(A)

    # Caso base: matriz 1x1
    if n == 1:
        return A[0][0]

    # Caso base: matriz 2x2
    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    det = 0

    # Expansão pela primeira linha
    for j in range(n):

        # Cria a submatriz Aij, retirando
        # a primeira linha e a coluna j
        submatriz = [
            [A[i][k] for k in range(n) if k != j]
            for i in range(1, n)
        ]

        # Cofator: (-1)^(i+j)
        # Como estamos usando a primeira linha, i = 0
        cofator = (-1) ** j

        # Regra de Laplace
        det += A[0][j] * cofator * determinante(submatriz)

    return det
A = [
    [1, 9, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Determinante =", determinante(A))