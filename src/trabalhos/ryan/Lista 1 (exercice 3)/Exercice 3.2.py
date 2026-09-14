opçao = 0
while opçao != 3:
    print("\nMenu")
    print("1 - saudação")
    print("2 - mostrar data ficticia")
    print("3 - sair")
    opçao = int(input("escolha uma opção: "))

    if opçao == 1:
        print("Bem-vindo a J2 !!!")
    elif opçao == 2:
        print("hoje é 01/01/2100 !!!")
    elif opçao == 3:
        print("Fim do programa !!! ")
    else:
        print("comando errado !!!")