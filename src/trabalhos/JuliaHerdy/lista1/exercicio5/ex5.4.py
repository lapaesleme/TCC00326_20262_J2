saldo = 1000.00


def consultar_saldo():
    print(f"Saldo atual: R$ {saldo:.2f}")


def depositar(valor):
    global saldo
    saldo += valor
    print("Depósito realizado com sucesso!")


def sacar(valor):
    global saldo

    if valor <= saldo:
        saldo -= valor
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente!")


while True:
    print("\n=== CAIXA ELETRÔNICO ===")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        consultar_saldo()

    elif opcao == "2":
        valor = float(input("Digite o valor do depósito: "))
        depositar(valor)

    elif opcao == "3":
        valor = float(input("Digite o valor do saque: "))
        sacar(valor)

    elif opcao == "4":
        print("Obrigado por utilizar o caixa eletrônico!")
        break

    else:
        print("Opção inválida!")