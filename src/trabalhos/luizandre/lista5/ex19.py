import json

with open('dados.json', 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)
    for linha in dados:
        print(linha)
