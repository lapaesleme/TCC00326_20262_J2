X = float(input('Digite sua nota:'))
Y = float(input('Digite sua nota:'))
media = (X + Y) / 2
print(media)
if media >= 6:
    print('Aprovado')
elif 5.9 >= media >= 4.0:
    print('Recuperação')
else:
    print('Reprovado')