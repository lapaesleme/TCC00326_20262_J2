lista = []
lista.append(int(input()))
for _ in range(9):
    lista.append(int(input()))
negativos = 0
positivos = 0
pares = 0
impares = 0
zeros = 0
for elementos in lista:
    if elementos ==0:
        zeros+=1
    if elementos > 0:
        positivos +=1
    if elementos <0:
        negativos +=1
    if elementos %2 ==0:
        pares +=1
    elif elementos %2!=0:
        impares +=1
print("negativos", negativos)
print("positivos", positivos)
print("pares", pares)
print("impares", impares)
print("zeros", zeros)