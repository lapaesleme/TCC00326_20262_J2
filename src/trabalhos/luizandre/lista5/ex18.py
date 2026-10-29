import csv

bd = []
with open('dados.csv', mode='r', encoding='utf-8') as f:
    leitor = csv.reader(f, delimiter=';')
    chaves = None;
    print(chaves)
    for linha in leitor:
        if chaves == None:
            chaves = linha
        else:
            i = 0
            d = {}
            for chave in chaves:
                d[chave] = linha[i]
                i += 1
            d['Projeção'] = 2 * d['Vendas Planejadas (BRL)']
            print(d['Projeção'])
            bd.append(d)
print(bd)

dados = []
linha_csv = bd[0]
labels_csv = linha_csv.keys()
labels_csv = list(labels_csv)
dados.append(list(bd[0].keys()))
for linha in bd:
    dados.append(list(linha.values()))

with open('dados_saida.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerows(dados)
