A = int(input("digite o primeiro valor: "))
B = int(input("digite o segundo valor: "))
calc = input("qual operação deseja fazer? (+, -, * ou /)")

if calc == "+":
    print(f"{A} + {B} = {A + B}")
elif calc == "-":
    print(f"{A} - {B} = {A - B}")
elif calc == "*":
    print(f"{A} * {B} = {A * B}")
elif calc == "/":
    if B == 0:
        print("resultado não definido")
    else:
        print(f"{A} / {B} = {A / B}")
else:
    print("sinal desconhecido")