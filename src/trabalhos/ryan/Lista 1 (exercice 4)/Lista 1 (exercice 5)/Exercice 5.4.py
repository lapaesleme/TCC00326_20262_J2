saldo = 2000,00
digito = 0

while digito != 4:
    print("1- Consultar saldo disponível ")
    print("2- Depositar Valor ")
    print("3 - Sacar Valor ")
    print("4 - Sair ")
    digito = int(input("Digite para iniciar o atendimento: "))

    if digito == 1:
        print ("Seu saldo é de: R$ " , saldo)


    elif digito == 2:

        valor = float(input("Qual valor gostaria de depositar ??? R$:   "))

        if valor > 0:
            saldo = saldo + valor

            print("Deposito efetuado com sucesso !!!.")

            print("Seu novo saldo atual é de: R$", saldo)
        else:
            print("valor do deposito invalido.")



    elif digito == 3:

        valor = float(input("Digite o valor do saque:"))

        if valor <= 0:

            print("O valor do saque invalido.")

        elif valor > saldo:

            print("Seu saldo é insuficiente.")

        else:

            saldo -= valor

            print("Saque realizado com sucesso !!!")

            print("Seu novo saldo é de R$:  ", saldo)

    elif digito == 4:
        print("Operação finalizada, volte sempre !!!")
    else:
        print("Código invalido !!!")