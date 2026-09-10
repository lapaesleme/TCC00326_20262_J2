inv = input("deseja lista invertida? (s/n)")
if inv == "s":
    #             (inicio, fim, passo)
    for numero in range(10, 0, -1):
        print(numero)
    print("Fim!")
else:
    print("Tenha um bom dia!")