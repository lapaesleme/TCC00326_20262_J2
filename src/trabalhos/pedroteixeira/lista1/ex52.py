nomes = []
while True:
    nome = input("digite um nome ou 'sair' para finalizar: ")
    if nome.lower() == "sair":
        break
    nomes.append(nome)
    print("nomes cadastrados: ")
    for nome in nomes:
        print(nomes)