import os

nome = input("Digite o nome do arquivo: ")

if os.path.isfile(nome):
    with open(nome, "r") as arquivo:
        texto = arquivo.read()

    print(texto)
else:
    print("Arquivo não encontrado!")