nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

def media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3

media = media(nota1, nota2, nota3)

if media >= 7:
    situacao = "O aluno está aprovado"
elif media >= 5:
    situacao = "O aluno está de recuperação"
else:
    situacao = "O aluno está reprovado"

print("\n--- BOLETIM ---")
print("Aluno:", nome)
print("Média:", media)
print("Situação:", situacao)
