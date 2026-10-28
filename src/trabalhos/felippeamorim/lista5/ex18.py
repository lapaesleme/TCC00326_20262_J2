import csv

with open("vendas.csv", "r", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)

    with open("resultado_vendas.csv", "w", newline="") as destino:
        campos = ["produto", "quantidade", "preço", "total"]

        escritor = csv.DictWriter(destino, fieldnames=campos)
        escritor.writeheader()

        for linha in leitor:
            quantidade = int(linha["quantidade"])
            preco = float(linha["preço"])

            total = quantidade * preco

            linha["total"] = total
            escritor.writerow(linha)

print("Arquivo criado!")