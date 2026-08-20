def calcular(a,b,operaçao):
    if operaçao =="+":
        return a+b
    elif operaçao =="-":
        return a-b
    elif operaçao =="*":
        return a*b
    elif operaçao =="/":
        if b != 0:
             return a/b
        else:
          return "nao é possivel dividir por zero"
    else:
        return "operação invalida"

num1 = int(input("digite um numero:"))
num2 = int(input("digite um numero:"))
operaçao = input("digite a operação(+,/,*,-):")

resultado = calcular(num1,num2,operaçao)
print("resultado:", resultado)