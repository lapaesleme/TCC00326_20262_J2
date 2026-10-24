antiga = input("Palavra antiga: ")
nova = input("Palavra nova: ")

with open("mensagem.txt", "r") as arquivo:
    texto = arquivo.read()

texto = texto.replace(antiga, nova)

with open("novo.txt", "w") as arquivo:
    arquivo.write(texto)

print("Substituição realizada!")