a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
operacao = input("Digite a operação matemática que deseja realizar (soma, subtração, divisão ou multiplicação):")

def calcular(a, b, operacao):
    if operacao == "soma":
        print ("A soma do número", a, "com o número", b, "é igual a", a + b)
    elif operacao == "subtração":
        print("A subtração do número", a, "com o número", b, "é igual a", a - b)
    elif operacao == "divisão":
        print("A divisão do número", a, "com o número", b, "é igual a", a/b)
    elif operacao == "multiplicação":
        print("A multiplicação do número", a, "com o número", b, "é igual a", a*b)

calcular(a, b, operacao)