coringa = []

def list_comp (n,j):
    for i in n:
        if len(i) <= j:
            coringa.append(i)
        else:
            pass

palavras = input("Quais palavras deseja verificar? ").split()
k = int(input("Qual o tamanho mínimo de cada palavra a ser separada? "))
list_comp (palavras,k)
print(coringa)