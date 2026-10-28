estoque = {
    "Arroz": {
        "quantidade_atual": 10,
        "quantidade_minima": 20,
        "preco": 25.00
    },
    "Feijão": {
        "quantidade_atual": 30,
        "quantidade_minima": 15,
        "preco": 8.50
    },
    "Macarrão": {
        "quantidade_atual": 5,
        "quantidade_minima": 10,
        "preco": 4.00
    },
    "Açúcar": {
        "quantidade_atual": 8,
        "quantidade_minima": 12,
        "preco": 5.50
    }
}


def calcular_valor_estoque(estoque):
    total = 0

    for produto, dados in estoque.items():
        total += dados["quantidade_atual"] * dados["preco"]

    return total


def verificar_reposicao(estoque):
    produtos_repor = []

    for produto, dados in estoque.items():
        if dados["quantidade_atual"] < dados["quantidade_minima"]:
            falta = dados["quantidade_minima"] - dados["quantidade_atual"]
            produtos_repor.append((produto, falta))

    return produtos_repor


def item_mais_urgente(estoque):
    urgente = None
    maior_falta = 0

    for produto, dados in estoque.items():
        falta = dados["quantidade_minima"] - dados["quantidade_atual"]

        if falta > maior_falta:
            maior_falta = falta
            urgente = produto

    return urgente


# Calculando o valor total
total = calcular_valor_estoque(estoque)

# Verificando produtos que precisam de reposição
reposicao = verificar_reposicao(estoque)

# Encontrando o item mais urgente
urgente = item_mais_urgente(estoque)


print(f"Valor total do estoque: R$ {total:.2f}")

print("\nProdutos que precisam de reposição:")

for produto, falta in reposicao:
    print(f"- {produto}: faltam {falta} unidades")

print(f"\nItem que exige reposição mais urgente: {urgente}")