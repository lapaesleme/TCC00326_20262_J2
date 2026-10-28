saldo_inicial = 16785.80

def consultar():
    return print(saldo_inicial)

def depositar():
    global saldo_inicial
    b = int(input("Quanto você deseja depositar: "))
    saldo_inicial = saldo_inicial + b
    return print(saldo_inicial)

def sacar():
    global saldo_inicial
    a = int(input("Quanto você deseja sacar: "))
    saldo_inicial = saldo_inicial - a
    return print(saldo_inicial)

def sair():
    return print("Você saiu")

print("1- consultar")
print("2- depositar")
print("3- sacar")
print("4- sair")
print("")
x = int(input("O que você deseja fazer: "))
print("")
if x == 1:
    consultar()
if x ==2:
    depositar()
if x==3:
    sacar()
if x==4:
    sair()

while x != 4:
    print("")
    print("1- consultar")
    print("2- depositar")
    print("3- sacar")
    print("4- sair")
    print("")
    x = int(input("O que você deseja fazer: "))
    if x == 1:
        consultar()
    if x ==2:
        depositar()
    if x==3:
        sacar()
    if x==4:
        sair()