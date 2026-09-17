idade = int(input("Digite uma idade: "))

while idade > 120 or idade < 0:
    print("Idade inválida!")
    idade = int(input("Digite uma idade: "))

print("Idade válida!")