
ativos = [{ "nome": "ibov", "qtd": 10, "compra": 123.0, "preco": 134},
{ "nome": "itau", "qtd": 12, "compra": 12.0, "preco": 48}
]

def valor_investido(ativo):
    return ativo["qtd"]*ativo["compra"]

def valor_atual(ativo):
    return ativo["qtd"]*ativo["preco"]

def resultado(ativo):
    return valor_atual(ativo)-valor_investido(ativo)

def rentabilidade(ativo):
    return (valor_atual(ativo)/valor_investido(ativo)-1)*100

for ativo in ativos:
    print(ativo["nome"], "resultado", rentabilidade(ativo))