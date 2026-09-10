nota1 = float(input("digite a primeira nota"))
nota2 = float(input("digite a segunda nota"))
media = (nota1 + nota2) / 2
if media >= 6:
    print("aprovado")
elif media >= 5:
    print("recuperação")
else:
    print("reprovado")