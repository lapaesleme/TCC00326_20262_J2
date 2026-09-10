nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
if media >= 7:
    print ("O aluno está aprovado")
elif media >= 5:
    print("O aluno está de recuperação")
elif media < 5:
    print("O aluno está reprovado")