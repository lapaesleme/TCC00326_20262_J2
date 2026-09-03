vendas = [
{"produto":"teclado","categoria":"n_pc","preco":35,"quantidade vendida":8},
{"produto":"monitor","categoria":"n_pc","preco":200,"quantidade vendida":7},
{"produto":"mouse","categoria":"n_pc","preco":40,"quantidade vendida":11},
{"produto":"gabinete","categoria":"pc","preco":300,"quantidade vendida":6},
{"produto":"processador","categoria":"pc","preco":800,"quantidade vendida":4}
]
vtotal = 0
vpctotal = 0
vnpctotal = 0
for x in vendas:
    faturamento = x["preco"] * x["quantidade vendida"]
    vtotal += faturamento
    media = vtotal/len(vendas)
    if x["categoria"] == "n_pc":
        faturamento = x["preco"] * x["quantidade vendida"]
        vnpctotal += faturamento
    elif x["categoria"] == "pc":
        faturamento = x["preco"] * x["quantidade vendida"]
        vpctotal += faturamento
    else:
        pass

print(f"Faturamento total: {vtotal}, Média do valor total: {media}, faturamento de peças de pc: {vpctotal}, faturamento dos acessórios: {vnpctotal}")

