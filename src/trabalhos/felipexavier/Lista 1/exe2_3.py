somar = (input("deseja realizar soma de 1 a 100? (s/n)"))
if somar == "s":
    soma = 0
    for numero in range(1, 101):
        soma += numero
    print(soma)
else:
    print("Tenha um bom dia!")