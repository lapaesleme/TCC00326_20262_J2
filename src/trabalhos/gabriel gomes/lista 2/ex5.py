def dobro(numero):
    return numero * 2
def aplicar_op(lista,funcao):
    resultado = []
    for numero in lista:
        resultado.append(funcao(numero))
    return resultado
numeros = [1,2,3,4,10,12,20]
print(aplicar_op(numeros,dobro))