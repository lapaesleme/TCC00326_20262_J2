#programa para informar se um número é positivo, negativo ou zero
numero=int(input("Insira um número inteiro:"))
if numero>0:
    print(numero,"é positivo!")
elif numero<0:
    print(numero,"é menor que zero!")
else:
    print("Zero não é positivo nem negativo, é zero!")
