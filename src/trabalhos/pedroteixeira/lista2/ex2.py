notas = [8,7,7,56,76,9,0,8,9,10,-1]
soma = 0
quantidade = 0
for nota in notas:
    if nota == -1:
        break
    if nota >= 0 and nota <= 10:
        soma += nota
        quantidade += 1
    else:
        print("nota invalida:", nota)
if quantidade > 0:
    media = soma / quantidade
    print("media:", media)
    if media >= 7:
        print("desempenho bom")
    elif media >= 5:
        print("desempenho regular")
    else:
        print("desempenho baixo")