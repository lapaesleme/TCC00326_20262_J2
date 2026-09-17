def aplicar_operacao(lista, funcao):
    resultado = []

    for numero in lista:
        resultado.append(funcao(numero))

    return resultado


def dobro(numero):
    return numero * 2


numeros = [1, 2, 3, 4, 5]

resultado = aplicar_operacao(numeros, dobro)

print(resultado)