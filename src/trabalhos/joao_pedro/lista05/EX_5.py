nome = input("Digite o nome do arquivo: ")

try:
    with open(nome, "r", encoding="utf-8") as arquivo:
        linhas = arquivo.readlines()

    print("Quantidade de linhas:", len(linhas))

except FileNotFoundError:
    print("Erro: arquivo não encontrado.")

except PermissionError:
    print("Erro: você não tem permissão para ler esse arquivo.")
