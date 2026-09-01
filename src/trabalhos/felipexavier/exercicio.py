def acessar ():

    senhas = {"felipe": "malenia","giulia":"marika","elden":"ring"}

    entrar = input("Deseja acessar sistema? (s/n) ")

    while entrar == "s":

        login = input("Qual o usuário? ")

        senha = input("Qual a senha? ")

        if login in senhas:

            if senhas[login] == senha:

                print("Acesso liberado.")

                break

            else:

                print("Senha errada.")

                entrar = input("Deseja acessar sistema? (s/n) ")

        else:

            print("Acesso Negado")

            entrar = input("Deseja acessar sistema? (s/n) ")

acessar()
