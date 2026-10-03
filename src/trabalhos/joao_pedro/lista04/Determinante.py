def submatriz(A, i, j):

    return [
        [A[x][y] for y in range(len(A)) if y != j]
        for x in range(len(A)) if x != i
    ]


def determinante(A):

    n = len(A)

    if n == 1:
        return A[0][0]

    if n == 2:
        return A[0][0] * A[1][1] - A[0][1] * A[1][0]

    det = 0

    for j in range(n):
        cofator = (-1) ** j
        sub = submatriz(A, 0, j)

        det += A[0][j] * cofator * determinante(sub)

    return det


A = [
    [1, 3, 8],
    [5, 1, 2],
    [2, 5, 3]
]

print("Determinante =", determinante(A))