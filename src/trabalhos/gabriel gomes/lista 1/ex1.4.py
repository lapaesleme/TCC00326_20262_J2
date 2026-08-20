nota1 = int(input("digite sua primeira nota: "))
nota2 = int(input("digite sua segunda nota: "))
media = (nota1 + nota2) / 2
if media < 6 and media > 4:
    print("voce esta de recuperação")
elif media >=6:
    print("voce esta aprovado")
else:
    print("voce esta reprovado")