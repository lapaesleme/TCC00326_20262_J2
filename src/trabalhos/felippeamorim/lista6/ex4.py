def maior_por_linha(matriz):
    if not matriz:
        return "Erro: Matriz vazia."

    resultados = []
    for i in range(len(matriz)):
        linha = matriz[i]
        if not linha:
            continue  # Pula linhas vazias ou retorna erro, dependendo da necessidade

        maior_valor = linha[0]
        coluna_maior = 0

        for j in range(1, len(linha)):
            if linha[j] > maior_valor:
                maior_valor = linha[j]
                coluna_maior = j

        resultados.append({"valor": maior_valor, "linha": i, "coluna": coluna_maior})

    return resultados


# Exemplo
M = [[1, 8, 3], [9, 5, 6], [2, 2, 2]]
for res in maior_por_linha(M):
    print(res)
# Saída:
# {'valor': 8, 'linha': 0, 'coluna': 1}
# {'valor': 9, 'linha': 1, 'coluna': 0}
# {'valor': 2, 'linha': 2, 'coluna': 0}