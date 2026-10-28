nome = input("Digite o nome do arquivo: ")

arquivo = open(nome, "r")

contador = 0

for linha in arquivo:
    contador += 1

print("Quantidade de linhas:", contador)

arquivo.close()