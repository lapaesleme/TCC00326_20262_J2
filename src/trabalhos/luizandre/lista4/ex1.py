def cofatora(a, l, c):
    cof = []
    for i in range(len(a)):
        if (i != l):
            linha = []
            for j in range(len(a[0])):
                if (j != c):
                    linha.append(a[i][j])
            cof.append(linha)
    return cof


def det(a):
    n1 = len(a)
    n2 = len(a[0])
    if n1 == n2 and n1 > 0:
        if n1 == 1:
            return a[0][0]
        else:
            l = 1
            soma = 0
            for c in range(n1):
                soma += a[l][c] * ((-1) ** (l + 1 + c + 1)) * det(cofatora(a, l, c))
            return soma
    else:
        return None


a = [[1, 2, 3], [4, 2, 6], [7, 8, 9]]
print(cofatora(a, 1, 1))
print(det(a))
