def identidade(dimensao):
    resultado = [[0 for j in range(dimensao)] for i in range(dimensao)]
    for i in range(dimensao):
        resultado[i][i] = 1
    return resultado


def eh_identidade(m):
    for i in range(0, len(m)):
        for j in range(0, len(m)):
            if (i != j and m[i][j] != 0):
                return False
            elif (i == j and m[i][j] != 1):
                return False
    return True


print(identidade(5))
print(eh_identidade(identidade(5)))

# m = [[1, 2, 3]] * 3
# m[0][0] = 222
# print(m)
