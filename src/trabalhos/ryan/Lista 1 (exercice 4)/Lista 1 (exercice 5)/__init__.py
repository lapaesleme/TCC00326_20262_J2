def media(A,B,C):
   A + B + C / 3

A = int(input("Digite sua PRIMEIRA nota : "))
B = int(input("Digite sua SEGUNDA nota: "))
C = int(input(" Digit sua TERCEIRA nota: "))
nome = input("Qual o seu nome ??? : ")

if A + B + C / 3 > 6:
    print("Parabéns", nome, ", vc foi aprovado !!!")
elif A + B + C / 3 > 4:
    print("Vc ainda tem uma ultima prova", nome , "boa sorte !!! ")
else:
    print(nome, "infelizmente vc foi reprovado !!!")

