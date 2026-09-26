
carteira = [
    {
        "nome": "Antônio",
        "quantidade": 100,
        "preco_compra": 30.00,
        "preco_atual": 35.00
    },
    {
        "nome": "Anderson",
        "quantidade": 50,
        "preco_compra": 60.00,
        "preco_atual": 55.00
    },
    {
        "nome": "José",
        "quantidade": 80,
        "preco_compra": 25.00,
        "preco_atual": 28.00
    }
]

melhor = None
pior = None

for ativo in carteira:
    valor_investido = ativo["quantidade"] * ativo["preco_compra"]
    valor_atual = ativo["quantidade"] * ativo["preco_atual"]

    lucro_prejuizo = valor_atual - valor_investido
    rentabilidade = (lucro_prejuizo / valor_investido) * 100

    print(f"\nAtivo: {ativo['nome']}")
    print(f"Valor investido: R$ {valor_investido:.2f}")
    print(f"Valor atual: R$ {valor_atual:.2f}")
    print(f"Lucro/Prejuízo: R$ {lucro_prejuizo:.2f}")
    print(f"Rentabilidade: {rentabilidade:.2f}%")

    # Verifica melhor desempenho
    if melhor is None or rentabilidade > melhor[1]:
        melhor = (ativo["nome"], rentabilidade)

    # Verifica pior desempenho
    if pior is None or rentabilidade < pior[1]:
        pior = (ativo["nome"], rentabilidade)


print("\n--- DESEMPENHO DA CARTEIRA ---")
print(f"Melhor desempenho: {melhor[0]} ({melhor[1]:.2f}%)")
print(f"Pior desempenho: {pior[0]} ({pior[1]:.2f}%)")