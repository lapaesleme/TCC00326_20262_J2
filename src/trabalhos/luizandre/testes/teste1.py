m1 = [[1, 2], [3, 4], [5, 6]]
m2 = [[2, 3], [4, 5], [6, 7]]
resultado = []

for i in range(len(m1)):
    linha = []
    for j in range(len(m1[0])):
        linha.append(m1[i][j] + m2[i][j])
    resultado.append(linha)

print(resultado)
