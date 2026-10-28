def contar_se(lista, criterio):
    contador = 0

    for elemento in lista:
        if criterio(elemento):
            contador += 1

    return contador


def maior_que_5(numero):
    return numero > 5


numeros = [2, 7, 4, 9, 10, 3]

resultado = contar_se(numeros, maior_que_5)

print(resultado)