soma = 0
num = int(input("deseja fazer somas? (digite zero para sair): "))
while num != 0:
    soma = soma + num
    num = int(input("Continue somando (zero para sair): "))
print(soma)