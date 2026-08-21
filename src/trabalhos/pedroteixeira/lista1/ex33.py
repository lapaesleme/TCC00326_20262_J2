numero_secreto = 10
palpite = int(input("digite o seu palpite"))
while palpite != numero_secreto:
    print("voce errou")
    palpite = int(input("tente novamente"))
    print("voce acertou")