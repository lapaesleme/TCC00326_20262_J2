def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3


nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = calcular_media(nota1, nota2, nota3)

print("Aluno:", nome)
print("Média:", media)

if media >= 6:
    print("Situação: Aprovado")
elif media <= 5.9:
    print("Situação: Recuperação")
else:
    print("Situação: Reprovado")