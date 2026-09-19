def eh_par(numero):
    return numero % 2 == 0
def contar_se(lista, criterio):
    contador = 0
    for elemento in lista:
        if criterio(elemento):
            contador += 1
    return  contador
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
quantidade_pares = contar_se(lista_numeros, eh_par)
print("lista", lista_numeros)
print("quantidade de numeros pares", quantidade_pares)