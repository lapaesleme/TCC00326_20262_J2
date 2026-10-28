nomes = []

while True:
    x = input()
    if x.lower() == "sair":
        break
    nomes.append(x)

for elementos in nomes:
    print(elementos)