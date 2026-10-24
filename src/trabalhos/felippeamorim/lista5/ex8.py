with open("mensagem.txt", "r") as arquivo:
    texto = arquivo.read()

palavras = texto.split()

print("Total de palavras:", len(palavras))