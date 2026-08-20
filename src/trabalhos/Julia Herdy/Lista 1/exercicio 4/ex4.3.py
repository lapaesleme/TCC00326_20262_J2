numero = int(input("Digite um numero:"))

def par_impar(numero):
    if numero % 2 == 0:
        print("O número", numero,"é par")
    else:
        print("O número", numero,"é ímpar")

par_impar(numero)