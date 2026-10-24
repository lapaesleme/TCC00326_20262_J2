import os

pasta = input("Digite o caminho da pasta: ")

arquivos = os.listdir(pasta)

lista = []

for nome in arquivos:
    caminho = os.path.join(pasta, nome)

    if nome.endswith(".txt") and os.path.isfile(caminho):
        lista.append(nome)

lista.sort()

for nome in lista:
    print(nome)