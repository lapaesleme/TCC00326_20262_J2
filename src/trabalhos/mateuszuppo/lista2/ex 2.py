nota = [ 10, 2, 1, 2, 5, 4, 3, 4, 6, 9]
soma = 0
for elementos in nota:
    soma += elementos
media = soma/10
if media >= 7:
    print(media, "regular")
if 5 < media <= 6.9:
    print(media, "bom")
else:
    print(media, "ruim")