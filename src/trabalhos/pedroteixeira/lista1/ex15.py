numero1 = float(input("digite o primeiro valor"))
numero2 = float(input("digite o segundo valor"))
operacao = input("digite a operacao (+, -, * ou /):")
if operacao == "+":
    print("resultado:", numero1 + numero2)
elif operacao == "-":
    print("resultado:", numero1 - numero2)
elif operacao == "*":
    print("resultado,", numero1 * numero2)
elif operacao == "/":
    if numero2 == 0:
        print("erro: não é possivel dividir por zero")
    else:
        print("resultado:", numero1 / numero2)
else:
    print("operacao invalida")