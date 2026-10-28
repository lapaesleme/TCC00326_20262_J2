def calcular(a, b):
    operador = str(input("Digite uma operação:"))
    if operador == "*":
        resultado = a * b
        print(resultado)
    if operador == "+":
        resultado = a + b
        print(resultado)
    if operador == "-":
        resultado = a - b
        print(resultado)
    elif operador == "/":
        if b ==0:
            print("Não existe")
        if a==0:
            print(0)
        if a and b ==0:
            print("Não existe")
        elif a and b !=0:
            resultado = a / b
        print(resultado)

print(calcular(1, 1))