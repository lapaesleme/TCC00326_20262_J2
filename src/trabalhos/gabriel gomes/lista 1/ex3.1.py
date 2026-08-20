senha_correta = "1234"
senha = input("digite a senha:")
while senha != senha_correta:
    print("senha incorreta")
    senha = input("digite a senha novamente:")
print("acesso liberado.")