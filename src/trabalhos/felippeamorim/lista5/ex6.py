origem = open("origem.txt", "r")
copia = open("copia.txt", "w")

for linha in origem:
    copia.write(linha)

origem.close()
copia.close()