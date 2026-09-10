

#2.2
notas = [0,7,2,3,8,5,11,9,6,7,8,9,10]
i = 0
quantidade = 0
for nota in notas:
    if nota >= 0 and nota <= 10:
        i = i + nota
        quantidade = quantidade + 1
media = i / quantidade
print("media:", media)
if media > 7:
    print("bom")
elif media >= 5:
    print("ok")
else:
    print("baixo")

def soma_listas(lista):
    if lista == []:
        return 0
    else:
        return lista[0] + soma_listas(lista[1:])
numeros = [1,2,3,4,5,6,7,8,9,10]
print(soma_listas(numeros))