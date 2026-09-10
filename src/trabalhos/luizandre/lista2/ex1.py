numeros = [1,43,-4, 6,2,10,8,78,100,56]

positivos = 0
negativos = 0
zeros = 0
pares = 0
impares = 0

for numero in numeros:
    if numero > 0:
        positivos = positivos + 1
    elif numero < 0:
        negativos = negativos + 1
    else:
        zeros = zeros + 1

    if numero % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

positivos = 0
negativos = 0
zeros = 0
pares = 0
impares = 0

for i in range(0,len(numeros)):
    if numeros[i] >0:
        positivos = positivos + 1
    elif numeros[i] < 0:
        negativos = negativos + 1
    else:
        zeros = zeros + 1
    if numeros[i] % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1


dict = {"pares": pares, "impares": impares, "zeros": zeros, "positivos": positivos, "negativos": negativos}

print (dict["pares"])
print(dict)
