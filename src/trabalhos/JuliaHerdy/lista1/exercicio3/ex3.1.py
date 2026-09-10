senha_correta = "1234"

while True:
    senha = input("Digite sua senha: ")
    if senha == senha_correta:
        print("Acesso liberado")
        break