with open("nomes.txt", "w") as arquivo:
    arquivo.write("Galeria\n")
    arquivo.write("Trabalhos\n")
    arquivo.write("Ferias\n")
    arquivo.write("Familia\n")
    arquivo.write("Boletim\n")
with open("nomes.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())