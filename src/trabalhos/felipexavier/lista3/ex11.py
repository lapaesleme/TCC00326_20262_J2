vendas = [
{"produto":"teclado","categoria":"n_pc","preco":35,"quantidade vendida":8},
{"produto":"monitor","categoria":"n_pc","preco":200,"quantidade vendida":7},
{"produto":"mouse","categoria":"n_pc","preco":40,"quantidade vendida":11},
{"produto":"gabinete","categoria":"pc","preco":300,"quantidade vendida":6},
{"produto":"gabinete","categoria":"pc","preco":280,"quantidade vendida":2},
{"produto":"processador","categoria":"pc","preco":800,"quantidade vendida":4}
]
vtotal = 0
vpctotal = 0
vnpctotal = 0
faturamentos={}
for venda in vendas:
    total_venda = venda["preco"] * venda["quantidade vendida"]
    faturamentos[venda["produto"]]=faturamentos.get(venda["produto"],0)+total_venda
print (faturamentos)

faturamentos_cat={}
for venda in vendas:
    total_venda = venda["preco"] * venda["quantidade vendida"]
    faturamentos_cat[venda["categoria"]]=faturamentos_cat.get(venda["categoria"],0)+total_venda
print (faturamentos_cat)

maior = 0
produto = None
for faturamento in faturamentos:
    #print (faturamento)
    if faturamentos[faturamento] > maior:
        maior = faturamentos[faturamento]
        produto = faturamento
print((maior, produto))





#print(faturamento)


