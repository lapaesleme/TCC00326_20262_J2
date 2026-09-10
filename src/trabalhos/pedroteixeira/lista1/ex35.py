idade = int(input("digite sua idade"))
while idade < 0 or idade > 120:
    print("idade invalida")
    idade = int(input("digite sua idade novamente"))
print("idade valida:", idade)5