def buscar(lista, valor):
    if len(lista) == 0:
        return False
    if lista[0] == valor:
        return True
    return buscar(lista[1:], valor)
numeros = [10,20,30,40,50]
valor = 50
resultado = buscar(numeros, valor)
print("lista:", numeros)
print("valor procurado:",valor)
print("encontrado", resultado)