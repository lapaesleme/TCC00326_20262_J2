i = int(input("digite a idade:"))
while i <0 or i>120:
    print("idade invalida")
    i = int(input("digite uma idade valida:"))
print("idade valida", i)