def eh_par(y):
    if y % 2 == 0:
        int(input("par"))
    else:
        int(input("impar"))

y = input("Digite um numero:")
valor = eh_par(y)
print("o resultado é", valor)

# função recursiva é uma função que chama a sí