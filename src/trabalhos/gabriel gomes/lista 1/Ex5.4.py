saldo = 1000.0
opcao = 0

while opcao != 4:
    print("\n=== CAIXA ELETRONICO ===")
    print("1 - consultar saldo")
    print("2 - depositar ")
    print("3 - sacar")
    print("4 - sair")
    opcao = int(input("escolha uma opção:"))
    if opcao == 1:

        print("saldo atual: ", saldo)

    elif opcao == 2:

        valor = float(input("digite o valor de deposito:"))

        if valor > 0:

            saldo = saldo + valor
            print("deposito efetuado.")
            print("novo saldo atual: R$", saldo)
        else:
            print("valor do deposito invalido.")
    elif opcao == 3:
        valor = float(input("digite o valor do saque:"))
        if valor <= 0:
            print("valor do saque invalido.")
        elif valor > saldo:
            print("saldo insuficiente.")
        else:
            saldo -= valor
            print("saque realizado com sucesso.")
            print("novo saldo: R$",saldo)
    elif opcao == 4:

        print("operação finalizada.")
    else:

        print("operação invalida")
