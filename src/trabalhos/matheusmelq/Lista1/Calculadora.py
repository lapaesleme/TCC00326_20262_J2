#Programa de calculadora simples
num1=float(input("informe o primeiro número:"))
operador=input("informe qual operação deseja fazer (+,-,* ou /):")
num2=float(input("informe o segundo número da operação"))
if operador=="+":
    print("o resultado é:",num1+num2)
elif operador=="-":
    print("o resultado é:", num1-num2)
elif operador=="*":
    print("o resultado é:", num1*num2)
elif operador=="/":
    if num2!=0:
        print("o resultado é:",num1/num2)
    else:
        print("Erro: Não é possível dividir por 0!!!!!")
else:
    print("operador não válido")