ativos = [
    {"nome": "aaaa", "qtd": 10, "compra": 123.0, "preco": 134},
    {"nome": "bbbb", "qtd": 12, "compra": 12.0, "preco": 12.6},
    {"nome": "cccc", "qtd": 15, "compra": 20.0, "preco": 25},
    {"nome": "dddd", "qtd": 17, "compra": 30, "preco": 12.6}
]


def valor_investido(ativo):
    return ativo["qtd"] * ativo["compra"]


def valor_atual(ativo):
    return ativo["qtd"] * ativo["preco"]


def resultado(ativo):
    return valor_atual(ativo) - valor_investido(ativo)


def rentabilidade(ativo):
    return (valor_atual(ativo) / valor_investido(ativo) - 1) * 100


def melhor_pior(ativos):
    maior = 0
    menor = 9999
    nomeMaior = None
    nomeMenor = None
    for ativo in ativos:
        percentual = rentabilidade(ativo)
        if percentual > maior:
            meior = percentual
            nomeMaior = ativo["nome"]
        if percentual < menor:
            menor = percentual
            nomeMenor = ativo["nome"]
    return {"melhor": nomeMaior, "pior": nomeMenor}


for ativo in ativos:
    print(ativo["nome"], "resultado", rentabilidade(ativo))

print(melhor_pior(ativos))
