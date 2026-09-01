
def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 12
lista = []
for i in range(n):
    lista.append(fibonacci(i))
print(lista)

lista2 = []
for e in lista:
    if e % 2 == 0:
        lista2.append(True)
    else:
        lista2.append(False)
print(lista2)