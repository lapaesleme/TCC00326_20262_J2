def media (a,b,c,nome):
    nota = (a + b + c)/3
    if nota >= 6:
        print(f"O aluno {nome} foi aprovado com média {nota}.")
    else:
        print(f"O aluno {nome} foi reprovado com média {nota}.")

n = input("Para ver a situação de um aluno digite suas notas e média:").split()

a = int(n[0])
b = int(n[1])
c = int(n[2])
nome = (n[3])

media(a,b,c,nome)