positivos = 0
negativos = 0
pares = 0
impares = 0
zeros = 0

for i in range(10):
    numero = int(input("Digite um número: "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    else:
        zeros += 1

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Positivos:", positivos)
print("Negativos:", negativos)
print("Pares:", pares)
print("Ímpares:", impares)
print("Zeros:", zeros)