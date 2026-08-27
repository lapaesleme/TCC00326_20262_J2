def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = 10

for i in range(n):
    numero = fibonacci(i)
    print(numero)

    if numero % 2 == 0:
        print("É par")