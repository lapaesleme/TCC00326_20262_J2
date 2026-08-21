import random
num = random.randint(1, 100)
chute = int(input("digite um chute: "))
while chute != num:
    if chute > num:
        print("chute mais baixo")
        chute = int(input("digite um chute: "))
    elif chute < num:
        print("chute mais alto")
        chute = int(input("digite um chute: "))
print("voce acertou!")
