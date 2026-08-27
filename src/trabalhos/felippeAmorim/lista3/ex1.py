vendas = [
    {"produto": "Arroz", "categoria": "Alimentos", "preco": 25, "quantidade": 10},
    {"produto": "Feijão", "categoria": "Alimentos", "preco": 10, "quantidade": 15},
    {"produto": "Sabão", "categoria": "Limpeza", "preco": 8, "quantidade": 20},
    {"produto": "Shampoo", "categoria": "Higiene", "preco": 15, "quantidade": 12}
]


# Faturamento total
total = 0

for venda in vendas:
    total += venda["preco"] * venda["quantidade"]

print("Faturamento total:", total)


# Produto com maior faturamento
maior = vendas[0]

for venda in vendas:
    faturamento = venda["preco"] * venda["quantidade"]
    faturamento_maior = maior["preco"] * maior["quantidade"]

    if faturamento > faturamento_maior:
        maior = venda

print("Produto com maior faturamento:", maior["produto"])


# Faturamento por categoria
categorias = {}

for venda in vendas:
    categoria = venda["categoria"]
    faturamento = venda["preco"] * venda["quantidade"]

    if categoria not in categorias:
        categorias[categoria] = 0

    categorias[categoria] += faturamento

print("Faturamento por categoria:", categorias)


# Média de unidades vendidas
soma = 0

for venda in vendas:
    soma += venda["quantidade"]

media = soma / len(vendas)

print("Média de unidades vendidas:", media)