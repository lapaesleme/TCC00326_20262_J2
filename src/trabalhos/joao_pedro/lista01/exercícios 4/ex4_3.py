def verificar_paridade(numero: {int} ):
    if numero % 2 == 0:
        return "par"
    else:
        return ("ímpar")
numero = int(input("Digite um número:"))
resultado = verificar_paridade(numero)
print("O número é:", resultado)

