palavra = input("Digite uma palavra: ").lower()

with open("mensagem.txt", "r") as arquivo:
    linhas = arquivo.readlines()

with open("resultado.txt", "w") as arquivo:
    for linha in linhas:
        if palavra in linha.lower():
            arquivo.write(linha)

print("Arquivo criado!")