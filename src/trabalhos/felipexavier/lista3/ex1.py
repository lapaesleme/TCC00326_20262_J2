vendas = [
{"produto":"teclado","categoria":"pc","preco":35,"quantidade vendida":8},
{"produto":"monitor","categoria":"pc","preco":200,"quantidade vendida":7},
{"produto":"mouse","categoria":"pc","preco":40,"quantidade vendida":11},
{"produto":"gabinete","categoria":"pc","preco":300,"quantidade vendida":6},
{"produto":"processador","categoria":"pc","preco":800,"quantidade vendida":4}
]
vtotal = 0

for x in vendas:
    preco = x["preco"]
    qtd = x["quantidade vendida"]
    valor_venda = preco * qtd
    vtotal += valor_venda

i=0
vtotal = 0
while i < len(vendas):
    x = vendas[i]
    preco = x["preco"]
    qtd = x["quantidade vendida"]
    valor_venda = preco * qtd
    vtotal += valor_venda
    i+=1

print (vtotal)





