def verificar_paridade(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
numero = int(input("digite um numero"))
resultado = verificar_paridade(numero)
print("o numero é:", resultado)