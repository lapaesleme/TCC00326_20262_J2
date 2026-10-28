def buscar(lista, valor):
    if len(lista) == 0:
        return False

    if lista[0] == valor:
        return True

    return buscar(lista[1:], valor)


numeros = [2, 5, 8, 10, 15]

print(buscar(numeros, 8))
print(buscar(numeros, 7))