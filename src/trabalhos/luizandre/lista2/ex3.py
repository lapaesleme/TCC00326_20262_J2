import math


def eh_primo(n):
    if n % 2 == 0:
        return False
    else:
        for div in range(3, int(math.sqrt(n)) + 1, 2):
            if n % div == 0:
                return False
        return True

n1 = 23
n2 = 115
primos = []

for numero in range(n1, n2 + 1):
    if eh_primo(numero):
        primos.append(numero)
print(primos)