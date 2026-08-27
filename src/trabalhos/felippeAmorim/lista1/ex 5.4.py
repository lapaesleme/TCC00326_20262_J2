saldo = 1000


def consultar_saldo():
    print("Saldo atual: R$", saldo)


def depositar(valor):
    return saldo + valor


def sacar(valor):
    return saldo - valor


while True:
    print("\n--- MENU ---")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        consultar_saldo()

    elif opcao == "2":
        valor = float(input("Digite o valor do depósito: "))
        saldo = depositar(valor)
        print("Depósito realizado!")

    elif opcao == "3":
        valor = float(input("Digite o valor do saque: "))

        if valor <= saldo:
            saldo = sacar(valor)
            print("Saque realizado!")
        else:
            print("Saldo insuficiente!")

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")