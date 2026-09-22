numeros = [2,4,5]

def quadrado (n ):
    return n*n

def processar_numeros (numeros, funcao):
    novaLista = []
    for n in numeros:
        novaLista.append(funcao(n))
    return novaLista

print (processar_numeros(numeros, quadrado))