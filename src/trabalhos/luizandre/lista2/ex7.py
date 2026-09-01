


def maior_5(n):
    return n > 5
def contar_se(lista,criterio):
    contador = 0
    for e in lista:
        if criterio(e):
            contador += 1
    return contador

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(contar_se(lista,maior_5))