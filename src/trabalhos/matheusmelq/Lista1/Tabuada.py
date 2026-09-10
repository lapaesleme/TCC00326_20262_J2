#programa para informar a tabuada de um número digitado pelo teclado
numero=int(input("informe um número inteiro <=10 e saiba sua tabuada de 1 a 10:"))
for i in range (1,11):
    print(numero,"*",i,"=",numero*i)