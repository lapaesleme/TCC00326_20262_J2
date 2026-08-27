x = str(input('Digite uma palavra: '))
soma = 0
for letra in x:
    if letra in 'aeiouAEIOU':
        soma +=1
print("Quantidade de vogais:", soma)