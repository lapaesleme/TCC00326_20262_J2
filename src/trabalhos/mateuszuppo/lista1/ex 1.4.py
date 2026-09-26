nota_1 = float(input())
nota_2 = float(input())
media = (nota_1 + nota_2) / 2
print(media)
if media>=6.0:
    print("Aprovado")
if 4.0 <= media <= 5.9:
    print("Recuperação")
elif media<4:
    print("Reprovado")