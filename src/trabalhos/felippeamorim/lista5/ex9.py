palavra = input("Digite uma palavra: ").lower()

contador = 0

with open("mensagem.txt", "r") as arquivo:
    texto = arquivo.read().lower()

palavras = texto.split()

for p in palavras:
    if p.strip(".,!?;:") == palavra:
        contador += 1

print("Quantidade:", contador)