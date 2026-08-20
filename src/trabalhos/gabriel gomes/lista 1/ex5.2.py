nomes = []
nome = input("digite um nome('sair' para terminar): ")
while nome.lower()!="sair":
    nomes.append(nome)
    nome = input("digite outro nome('sair' para terminar): ")

print("\n--- NOMES CADASTRADOS ---")
for nome in nomes:
    print(nome)