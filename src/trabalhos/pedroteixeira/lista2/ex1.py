numeros = (0,43,354,1,-64,0,-52,6,8,-43)
positivos = 0
negativos = 0
zeros = 0
impares = 0
pares = 0
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
dict = {"pares": pares, "impares": impares, "zeros": zeros, "positivos": positivos, "negativos": negativos}
print (dict["pares"])
print(dict)