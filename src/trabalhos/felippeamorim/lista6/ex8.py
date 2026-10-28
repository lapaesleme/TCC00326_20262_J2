def pontos_de_sela(matriz):
    if not matriz:
        return []

    linhas = len(matriz)
    colunas = len(matriz[0])
    pontos = []

    for i in range(linhas):
        menor_linha = matriz[i][0]
        # Encontra o menor valor da linha
        for j in range(1, colunas):
            if matriz[i][j] < menor_linha:
                menor_linha = matriz[i][j]

        # Verifica se esse menor valor é o maior da sua coluna
        for j in range(colunas):
            if matriz[i][j] == menor_linha:  # Achou um(s) menor(es) na linha
                eh_sela = True
                for k in range(linhas):
                    if matriz[k][j] > menor_linha:  # Tem alguém maior na coluna
                        eh_sela = False
                        break

                if eh_sela:
                    pontos.append({"valor": menor_linha, "posicao": (i, j)})

    return pontos


# Exemplo
M = [[9, 8, 7],
     [5, 3, 2],
     [6, 6, 7]]
print(pontos_de_sela(M))  # O 7 (linha 0, col 2) é menor da linha e maior da coluna? Sim. O 7 (linha 2, col 2)? Não.
# Verifique a matriz com cuidado. Exemplo clássico:
M2 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
# Menores linhas: 1, 4, 7.  1 é maior na col 0? Não. 4? Não. 7? Sim.
print(pontos_de_sela(M2))  # Saída: [{'valor': 7, 'posicao': (2, 0)}]