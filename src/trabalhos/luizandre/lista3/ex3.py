produtos = [
    {"nome": "sorvete", "quantidade_atual": 10, "quantidade_minima":5, "preco": 20},
    {"nome": "telefone", "quantidade_atual": 100, "quantidade_minima":20, "preco": 200},
    {"nome": "camisa", "quantidade_atual": 80, "quantidade_minima":20, "preco": 100},
    {"nome": "calca", "quantidade_atual": 70, "quantidade_minima":80, "preco": 40},
    {"nome": "meia", "quantidade_atual": 60, "quantidade_minima":280, "preco": 40}
]


def produtos_abaixo_minimo(produtos):
    selecionados=[]
    for produto in produtos:
        if produto["quantidade_atual"] < produto["quantidade_minima"]:
            selecionados.append(produto)
    return selecionados

def valor_estoque(produtos):
    soma=0
    for produto in produtos:
        soma += produto["quantidade_atual"]*produto["preco"]
    return soma

def produtos_reposicao(produtos):
    selecionados=produtos_abaixo_minimo(produtos)
    menor = 1000
    comprar = ""
    for produto in selecionados:
        percentual = produto["quantidade_atual"]/produto["quantidade_minima"]*100
        if percentual < menor:
            menor = percentual
            comprar = produto["nome"]
    return comprar



print (produtos_abaixo_minimo(produtos))
print (valor_estoque(produtos))
print (produtos_reposicao(produtos))