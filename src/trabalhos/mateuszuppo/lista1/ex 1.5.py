num_1 = int(input())
num_2 = int(input())
operador = str(input("Digite uma operação:"))
if operador == "*":
    resultado = num_1 * num_2
    print(resultado)
if operador == "+":
    resultado = num_1 + num_2
    print(resultado)
if operador == "-":
    resultado = num_1 - num_2
    print(resultado)
elif operador == "/":
    if num_2 ==0:
        print("Não existe")
    if num_1==0:
        print(0)
    if num_1 and num_2 ==0:
        print("Não existe")
    elif num_1 and num_2 !=0:
        resultado = num_1 / num_2
    print(resultado)