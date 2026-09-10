def calcular(A,B,op):
    if op == "+":
        return A + B
    elif op == "-":
        return A - B
    elif op == "*":
        return A * B
    elif op == "/":
        return A / B
    else:
        print("Operador não reconhecido")

num = input("Digite dois números e seu operador (A,B,op): ").split()
A = int(num[0])
B = int(num[1])
op = (num[2])
print(f"O resultado é {calcular(A,B,op)}")