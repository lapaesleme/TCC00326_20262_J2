def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
n = 10
print("primeiros", n, "termos de sequencia:")
for i in range(n):
    termo = fibonacci(i)
    print("termo", i, "=", termo)
print("termos pares:")
for i in range (n):
    termo = fibonacci(i)
    if termo % 2 == 0:
        print(termo)