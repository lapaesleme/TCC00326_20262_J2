def soma_lista(lista):

    soma = 0

    for elemento in lista:

        if isinstance(elemento, list):
            soma += soma_lista(elemento)

        else:
            soma += elemento

    return soma


numeros = [1, [2, 3], [4, [5, 6]]]

resultado = soma_lista(numeros)

print("Soma:", resultado)