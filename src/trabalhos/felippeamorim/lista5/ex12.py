with open("mensagem.txt", "r") as arquivo:
    linhas = arquivo.readlines()

with open("sem_vazias.txt", "w") as arquivo:
    for linha in linhas:
        if linha.strip() != "":
            arquivo.write(linha)

print("Arquivo criado!")