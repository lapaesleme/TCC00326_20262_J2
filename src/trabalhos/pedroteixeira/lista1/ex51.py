def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3
nome = input("digite o nome do aluno: ")
n1 = float(input("digite a primeira nota: "))
n2 = float(input("digite a segunda nota: "))
n3 = float(input("digite a terceira nota: "))
media = calcular_media(n1, n2, n3)
print("aluno:", nome)
print("media:", media)
if media >= 6:
    print("situação: aprovado")
elif media >= 5:
    print("situação: recuperação")
else:
    print("situação: reprovado")