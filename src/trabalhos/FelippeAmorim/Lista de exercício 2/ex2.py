soma = 0
quantidade = 0

while True:
    nota = float(input("Digite uma nota: "))

    if nota == -1:
        break

    if nota < 0 or nota > 10:
        print("Nota inválida!")
        continue

    soma += nota
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade

    print("Média:", media)

    if media >= 7:
        print("Bom")
    elif media >= 5:
        print("Regular")
    else:
        print("Baixo")
else:
    print("Nenhuma nota válida foi digitada.")