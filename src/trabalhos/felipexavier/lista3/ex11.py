vendas = [
{"produto":"teclado","categoria":"n_pc","preco":35,"quantidade vendida":8},
{"produto":"monitor","categoria":"n_pc","preco":200,"quantidade vendida":7},
{"produto":"mouse","categoria":"n_pc","preco":40,"quantidade vendida":11},
{"produto":"gabinete","categoria":"pc","preco":300,"quantidade vendida":6},
{"produto":"processador","categoria":"pc","preco":800,"quantidade vendida":4}
]

soma_quantidade = 0
maior = 0
produto = 0
vtotal = 0
vpctotal = 0
vnpctotal = 0
faturamento_cat = {}

for prod in vendas:
    val_prod = prod["preco"] * prod["quantidade vendida"]
    faturamento_cat[prod["produto"]] = faturamento_cat.get(prod["produto"], 0) + val_prod

for prod in faturamento_cat:
    if faturamento_cat[prod] > maior:
        maior = faturamento_cat[prod]
        produto = prod

for venda in vendas:
    faturamento = venda["preco"] * venda["quantidade vendida"]
    vtotal += faturamento
    if venda["categoria"] == "n_pc":
        faturamento = venda["preco"] * venda["quantidade vendida"]
        vnpctotal += faturamento
    elif venda["categoria"] == "pc":
        faturamento = venda["preco"] * venda["quantidade vendida"]
        vpctotal += faturamento
    else:
        pass

for quantidade in vendas:
    soma_quantidade += quantidade["quantidade vendida"]

media = soma_quantidade / len(vendas)


print(f"Faturamento total: {vtotal}, Média de produtos vendidos: {media}, faturamento de peças de pc: {vpctotal}, faturamento dos acessórios: {vnpctotal}")
print("--------------------------------------------------------------------------------------------------------------------------")
print(f"Faturamento por produto: {faturamento_cat}")
print("--------------------------------------------------------------------------------------------------------------------------")
print(f"Produto de maior faturamento: {produto}, total de {maior} reais.")
