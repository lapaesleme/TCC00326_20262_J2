soma = 0
conta = 0
nota = 0

while nota != -1:
    nota = float(input("Digite a nota: "))

    if nota >= 0 and nota <= 10:
        soma = soma + nota
        conta = conta + 1

if conta > 0:
    media = soma / conta

    print("Media:", media)

    if media >= 7:
        print("Bom")
    elif media >= 5:
        print("Regular")
    else:
        print("Baixo")
else:
    print("Nenhuma nota valida")

#2.1
quantidade = int(input("Quantos números você quer digitar? "))

pos = neg = zero = par = imp = 0

for i in range(quantidade):
    n = int(input("Digite um número: "))

    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
    else:
        zero += 1

    if n % 2 == 0:
        par += 1
    else:
        imp += 1

print("Positivos:", pos)
print("Negativos:", neg)
print("Zeros:", zero)
print("Pares:", par)
print("Ímpares:", imp)

#2.3

def ehprimo (numero):
    if numero % 2 == 0:
        return False
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

for numero in range(inicio, fim + 1):
    if ehprimo (numero):
        print(numero)


#2.8
textos = ["a","b"]

def maiusculas(texto):
    return texto.upper()

def processar(texto):
    novalista = []
    for i in texto:
        maiusculas(i)
        novalista.append(maiusculas(i))
    return novalista

print (textos,maiusculas())

#2.8
def soma_lista(lista):

    if not lista:
        return 0


    return lista[0] + soma_lista(lista[1:])


numeros = [5, 2, 8, 3]
resultado = soma_lista(numeros)
print("A soma da lista é:", resultado)
