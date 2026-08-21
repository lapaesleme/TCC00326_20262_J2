opçao = 0
while opçao != 3:
    print("\nMENU")
    print("1 - saudação")
    print("2 - mostrar data ficticia")
    print("3 - sair")
    opçao = int(input("escolha uma opção: "))

    if opçao == 1:
        print("Ola,seja bem-vindo")
    elif opçao == 2:
        print("hoje é 12/12/2012")
    elif opçao == 3:
        print("programa finalizado")
    else:
        print("comando invalido")