acesso = input("deseja acessar sua conta? (s/n)")
while acesso == "s":
    usuario = input("qual seu usuario: ")
    senha = input("qual sua sua senha: ")
    if usuario == "felipe" and senha == "eldenring":
        print("acesso liberado")
    else:
        print("acesso cancelado")
        acesso = input("acessar sua conta? (s/n)")