X = float(input('Digite um número:'))
Y = float(input('Digite um número:'))
operacao = input("Digite a operação (+, -, *, /):")
if operacao == "+":
    print(X+Y)
if operacao == "-":
    print(X-Y)
if operacao == "*":
    print(X*Y)
elif operacao == "/":
    if Y==0 or X==0 :
        print("não pode ser dividido")
    if X and Y!=0:
        print(X/Y)