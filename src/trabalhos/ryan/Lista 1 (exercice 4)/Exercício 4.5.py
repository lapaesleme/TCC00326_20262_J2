def calculadora(A,B,operacao):
    if operacao =="+":
        return A + B
    elif operacao  =="-":
        return A - B
    elif operacao  =="*":
        return A * B
    else:
        return A / B

A = int(input("Selecione uma variável: "))
B = int(input("Seelecione a segunda variável: "))
operacao  = input("Selecione a Operacao: ",)

resultado = calculadora(A,B,operacao)
print("O resultado é: ", resultado)

print()

