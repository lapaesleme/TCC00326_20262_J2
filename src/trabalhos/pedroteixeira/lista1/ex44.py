def maior_de_tres(a, b, c):
    maior = a
    if b > maior:
        maior = b
    if c > maior:
        maior = c
    return maior
n1 = float(input("digite o primeiro numero:"))
n2 = float(input("digite o segundo numero:"))
n3 = float(input("digite o terceiro numero:"))
resultado = maior_de_tres(n1, n2, n3)
print("O maior numero é:", resultado)