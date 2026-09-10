numeros = [10,-3,4,4,2,0,7,8,9,-30]
positivos = 0
negativos = 0
zeros = 0
impares = 0
pares = 0
for i in range(0,len(numeros)):
    if numeros[i] > 0:
        positivos = positivos + 1
    elif numeros[i] < 0:
        negativos = negativos + 1
    else:
        zeros = zeros + 1
    if numeros[1] % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
print("positivos:", positivos)
print("negativos:", negativos)
print("zeros:", zeros)
print("pares:", pares)
print("impares:",impares)