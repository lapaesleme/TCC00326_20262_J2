def zerar_linhas_colunas(matriz):
    if not matriz:
        return []

    linhas = len(matriz)
    colunas = len(matriz[0])

    linhas_para_zerar = set()
    colunas_para_zerar = set()

    # Identifica onde estão os zeros na matriz original
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == 0:
                linhas_para_zerar.add(i)
                colunas_para_zerar.add(j)

    # Cria a nova matriz baseada na original, aplicando os zeros
    nova_matriz = []
    for i in range(linhas):
        nova_linha = []
        for j in range(colunas):
            if i in linhas_para_zerar or j in colunas_para_zerar:
                nova_linha.append(0)
            else:
                nova_linha.append(matriz[i][j])
        nova_matriz.append(nova_linha)

    return nova_matriz


# Exemplo
M = [[1, 2, 3],
     [4, 0, 6],
     [7, 8, 9]]
resultado = zerar_linhas_colunas(M)
for l in resultado:
    print(l)