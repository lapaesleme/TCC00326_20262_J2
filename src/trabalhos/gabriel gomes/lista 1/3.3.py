numero_secreto = 7

palpite = int(input("Tente adivinhar o número: "))

while palpite != numero_secreto:

    if palpite < numero_secreto:
        print("O número secreto é maior.")

    else:
        print("O número secreto é menor.")

    palpite = int(input("Tente novamente: "))

print("Parabéns! Você acertou!")