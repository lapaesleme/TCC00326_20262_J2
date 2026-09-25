lista = [1, 4, 5, 8, 9, 0, 2]


def buscar(numero, vetor, indice):
    if 0 <= indice < len(vetor):
        if vetor[indice] == numero:
            return True
        else:
            return buscar(numero, vetor, indice + 1)
    else:
        return False


print(buscar(44, lista, 0))
