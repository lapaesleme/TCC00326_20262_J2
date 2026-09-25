numeros = [1, 43, -4, 6, 2, 10, 8, 0, 78, 100, 56]


def estatisticas(numeros):
    positivos = 0
    negativos = 0
    zeros = 0
    pares = 0
    impares = 0

    for numero in numeros:
        if numero > 0:
            positivos = positivos + 1
        elif numero < 0:
            negativos = negativos + 1
        else:
            zeros = zeros + 1

        if numero % 2 == 0:
            pares = pares + 1
        else:
            impares = impares + 1

    estatisticas = {"pares": pares, "impares": impares, "zeros": zeros, "positivos": positivos, "negativos": negativos}
    return estatisticas


print(estatisticas(numeros))
