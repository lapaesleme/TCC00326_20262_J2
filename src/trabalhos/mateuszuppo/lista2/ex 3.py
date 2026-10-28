def eh_primo(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o segundo número: "))

for numero in range(inicio, fim + 1):
    if eh_primo(numero):
        print(numero)