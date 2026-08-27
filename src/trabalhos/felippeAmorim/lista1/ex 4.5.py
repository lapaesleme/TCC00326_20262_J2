def calcular(a, b, operacao):
    if operacao == "+":
        return a + b
    elif operacao == "-":
        return a - b
    elif operacao == "*":
        return a * b
    elif operacao == "/":
        if b == 0:
            return "Não é possível dividir por zero"
        return a / b
    else:
        return "Operação inválida"


a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ")

print(calcular(a, b, operacao))