
pedidos = [
    {"cliente": "João", "regiao": "Sudeste", "valor": 500},
    {"cliente": "Maria", "regiao": "Sul", "valor": 300},
    {"cliente": "João", "regiao": "Sudeste", "valor": 200},
    {"cliente": "Pedro", "regiao": "Nordeste", "valor": 700},
    {"cliente": "Maria", "regiao": "Sul", "valor": 400}
]


total_cliente = {}
total_regiao = {}

soma_total = 0
maior_pedido = pedidos[0]


for pedido in pedidos:

    cliente = pedido["cliente"]
    regiao = pedido["regiao"]
    valor = pedido["valor"]

    # Total por cliente
    if cliente in total_cliente:
        total_cliente[cliente] += valor
    else:
        total_cliente[cliente] = valor

    # Total por região
    if regiao in total_regiao:
        total_regiao[regiao] += valor
    else:
        total_regiao[regiao] = valor

    # Soma de todos os pedidos
    soma_total += valor

    # Maior pedido
    if valor > maior_pedido["valor"]:
        maior_pedido = pedido


ticket_medio = soma_total / len(pedidos)


print("TOTAL POR CLIENTE")

for cliente in total_cliente:
    print(cliente, ":", total_cliente[cliente])


print("\nTOTAL POR REGIÃO")

for regiao in total_regiao:
    print(regiao, ":", total_regiao[regiao])


print("\nTicket médio:", ticket_medio)

print("\nMaior pedido:")
print("Cliente:", maior_pedido["cliente"])
print("Região:", maior_pedido["regiao"])
print("Valor:", maior_pedido["valor"])