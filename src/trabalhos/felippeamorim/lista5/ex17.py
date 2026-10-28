import os

pasta = input("Digite o caminho da pasta: ")

arquivos = os.listdir(pasta)

lista = []

for nome in arquivos:
    caminho = os.path.join(pasta, nome)

    if nome.endswith(".txt") and nome != "completo.txt":
        if os.path.isfile(caminho):
            lista.append(nome)

lista.sort()

destino = os.path.join(pasta, "completo.txt")

with open(destino, "w") as completo:
    for nome in lista:
        caminho = os.path.join(pasta, nome)

        with open(caminho, "r") as arquivo:
            texto = arquivo.read()

        completo.write("Arquivo: " + nome + "\n")
        completo.write(texto + "\n\n")

print("Arquivo completo criado!")