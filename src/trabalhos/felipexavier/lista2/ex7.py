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



palavra = input("digite uma palavra: ")
contador = 0
for letra in palavra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador += 1
print(f"palavra possui {contador} vogais")