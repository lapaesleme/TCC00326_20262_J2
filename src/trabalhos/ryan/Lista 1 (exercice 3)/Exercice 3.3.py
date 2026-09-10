n = 2008

i = int(input("Tente adivinhar o número: "))

while i!= n:

    if i < n:
        print("O número secreto é maior.")

    else:
        print("O número secreto é menor.")

    i = int(input("Tente novamente: "))

print("Parabéns! Você acertou!")