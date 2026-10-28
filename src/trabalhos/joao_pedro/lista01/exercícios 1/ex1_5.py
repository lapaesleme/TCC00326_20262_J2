n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
operação = input("Digite a operação matemática que deseja realizar (+,-,* ou /: ")

if operação == "+":
    print ("A soma do número", n1, "com o número", n2, "é igual a", n1 + n2)
if operação == "-":
    print("A subtração do número", n1, "com o número", n2, "é igual a", n1 - n2)
if operação == "*":
    print("A multiplicação do número", n1, "com o número", n2, "é igual a", n1*n2)
if operação == "/":
    print("A divisão do número", n1, "com o número", n2, "é igual a", n1 / n2)