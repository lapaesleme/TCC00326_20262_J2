def cofatora(a, i, j):
    cof = []
    for r in range(len(a)):
        if r != i:
            linha = []
            for c in range(len(a[0])):
                if c != j:
                    linha.append(a[r][c])
            cof.append(linha)
    return cof


def det(A):
    n = len(A)
    n2 = len(A[0])
    if n == n2 and n > 0:
        if n == 1:
            return A[0][0]
        else:
            i = 0
            soma = 0
            for j in range(n):
                soma += (
                    A[i][j]
                    * ((-1) ** ((i + 1) + (j + 1)))
                    * det(cofatora(A, i, j))
                )
            return soma
    else:
        return None

def resolver_cramer(A, B):
    n = len(A)
    det_principal = det(A)

    if det_principal == 0:
        return ("O sistema não possui solução única (determinante é zero).")

    solucoes = []
    for j in range(n):
# Cria uma cópia da matriz A para não alterar a original
        A_j = [linha[:] for linha in A]

# Substitui a coluna j pelos valores do vetor B
        for i in range(n):
            A_j[i][j] = B[i]


        det_atual = det(A_j)
        solucoes.append(det_atual / det_principal)

    return solucoes
    
