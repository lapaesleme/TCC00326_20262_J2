numeros = [8,9,6,5,5,4,8,9,7,8]

pos = 0
neg = 0
par = 0
imp = 0
zero = 0

for i in numeros:
    if i < 0:
        neg += 1
    elif i == 0:
        zero += 1
    else:
        pos += 1

    if i % 2 == 0:
        par += 1
    else:
        imp += 1

print(f"Número de valores par: {par}, impar: {imp}, positivos: {pos}, negativos: {neg}, zeros: {zero}")