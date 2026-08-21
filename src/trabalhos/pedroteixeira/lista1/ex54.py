def consultar_saldo(saldo):
    print("Saldo atual: R$", saldo)

def depositar(saldo):
    valor = float(input("Digite o valor do depósito: "))
    if valor > 0:
        saldo += valor
        print("Depósito realizado!")
    else:
        print("Valor inválido.")
    return saldo
def sacar(saldo):
    valor = float(input("Digite o valor do saque: "))
    if valor <= 0:
        print("Valor inválido.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        saldo -= valor
        print("Saque realizado!")
    return saldo

saldo = 1000
while True:
    print("n=== CAIXA ELETRÔNICO ===")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        consultar_saldo(saldo)
    elif opcao == "2":
        saldo = depositar(saldo)
    elif opcao == "3":
        saldo = sacar(saldo)
    elif opcao == "4":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")