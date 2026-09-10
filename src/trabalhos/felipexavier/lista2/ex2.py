numeros = [8,9,6,5,5,4,8,9,7,8]
media = 0

for i in range(0,len(numeros)):
    if numeros[i] > 0 and numeros[i] < 10:
        media = media + numeros[i] / len(numeros)


if media >= 7:
    print(f"Desempenho: Bom e média: {media}")
elif media < 7 and media >= 5:
    print(f"Desempenho: Médio e média: {media}")
elif media < 5:
    print(f"Desempenho: Baixo e média: {media}")


