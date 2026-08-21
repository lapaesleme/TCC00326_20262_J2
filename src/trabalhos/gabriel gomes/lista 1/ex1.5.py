operação = input("informe a operação desejada: multiplicação(*),divisão(/),subtração(-),adição(+):")
num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))
if operação == "*":
    print("o resultado é:", num1 * num2)
elif operação == "+":
    print("o resultado é:", num1 + num2)
elif operação == "-":
    print("o resultado é:", num1 - num2)
else:
    print("o resultado é", num1/num2)