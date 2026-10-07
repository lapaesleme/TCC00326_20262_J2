matriz1= [[1,2], [3,4]]
matriz2 = [[2,3], [4,5]]
resultado = []

soma = 0

for l in range(len(matriz1)):
    linha = []
    for c in range(len(matriz2[0])):
        soma = 0
        for k in range(len(matriz1[0])):
            soma += matriz1[l][k] * matriz2[k][c]
        linha.append(soma)
    resultado.append(linha)
print(resultado)