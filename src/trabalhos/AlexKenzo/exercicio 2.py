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
