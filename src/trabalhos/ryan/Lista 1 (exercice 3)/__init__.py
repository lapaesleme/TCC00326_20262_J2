senha = input("Digite a senha correta: ")
senha_correta = "0265"

while senha != senha_correta:
    senha = int(input("Acesso negado !!!"))
    senha_correta = 0
print("Acesso liberado !!!")