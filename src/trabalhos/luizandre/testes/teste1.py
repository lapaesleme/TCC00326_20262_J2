m1 = [[1, 2], [3, 4]]
m2 = [[2, 3], [4, 5]]
resultado = []

soma = 0
for l in range(len(m1)):
    linha = []
    for c in range(len(m2[0])):
        soma = 0
        for k in range(len(m1[0])):
            soma += m1[l][k] * m2[k][c]
        linha.append(soma)
    resultado.append(linha)

print(resultado)
