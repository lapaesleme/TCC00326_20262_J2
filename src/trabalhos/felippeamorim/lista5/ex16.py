import os

pasta = input("Digite o caminho da pasta: ")

arquivos = os.listdir(pasta)

for nome in arquivos:
    caminho = os.path.join(pasta, nome)

    if nome.endswith(".txt") and os.path.isfile(caminho):
        if not nome.startswith("processado_"):
            novo_nome = "processado_" + nome
            novo_caminho = os.path.join(pasta, novo_nome)

            if not os.path.exists(novo_caminho):
                os.rename(caminho, novo_caminho)
                print("Renomeado:", novo_nome)
