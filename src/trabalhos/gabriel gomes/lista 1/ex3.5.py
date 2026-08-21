idade = int(input("digite a idade:"))
while idade <0 or idade>120:
    print("idade invalida")
    idade = int(input("digite uma idade valida:"))
print("idade valida", idade)