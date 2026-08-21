opcao = 0

while opcao != 3:

    print("1 - saudação")
    print("2 - mostrar data fictícia")
    print("3 - sair")

    opcao = int(input("escolha uma opcao"))

    if opcao == 1:
        print("ola! seja bem - vindo")

    elif opcao == 2:
        print("a data é 15/07/2026")

    elif opcao == 3:
        print("programa encerrado")

    else:
        print("opcao invalida")
