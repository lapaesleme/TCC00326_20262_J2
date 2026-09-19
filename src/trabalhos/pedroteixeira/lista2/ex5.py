from trabalhos.felippeamorim.lista2.ex5 import resultado


def aplicar_operacao(lista, funcao):
    nova_lista = []
    for numero in lista:
        nova_lista.append(funcao(numero))
    return nova_lista
def dobrar(x):
    return x * 2
lista = [1,2,3,4]
resultado = aplicar_operacao(lista, dobrar)
print(resultado)