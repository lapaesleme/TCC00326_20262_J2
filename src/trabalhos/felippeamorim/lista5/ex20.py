import os
import shutil

pasta = input("Digite o caminho da pasta: ")

arquivos = os.listdir(pasta)

log = os.path.join(pasta, "log.txt")

with open(log, "a") as registro:

    for nome in arquivos:
        origem = os.path.join(pasta, nome)

        if os.path.isfile(origem) and nome != "log.txt":

            partes = os.path.splitext(nome)
            extensao = partes[1].replace(".", "").lower()

            if extensao == "":
                extensao = "sem_extensao"

            nova_pasta = os.path.join(pasta, extensao)

            os.makedirs(nova_pasta, exist_ok=True)

            destino = os.path.join(nova_pasta, nome)

            contador = 1

            while os.path.exists(destino):
                novo_nome = partes[0] + "_" + str(contador) + partes[1]
                destino = os.path.join(nova_pasta, novo_nome)
                contador += 1

            shutil.move(origem, destino)

            registro.write(nome + " movido para " + destino + "\n")

            print(nome, "organizado!")

print("Organização concluída!")