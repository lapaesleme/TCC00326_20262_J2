def paridade(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
numero = int(input("digite um numero:"))
resultado = paridade(numero)
print("o resultado é", resultado)