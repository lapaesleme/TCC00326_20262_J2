def calcular_media():
    nome = str(input())
    notas = []
    soma = 0
    for _ in range(3):
        inserir = float(input())
        notas.append(inserir)
        soma += inserir
    media = soma / 3
    if media >=6.0:
        return (f"{media} Aprovado ")
    if 4.0 <= media <= 5.9:
        return (f"{media} Recuperação")
    elif media<4:
        return (f"{media} Reprovado")


print(calcular_media())