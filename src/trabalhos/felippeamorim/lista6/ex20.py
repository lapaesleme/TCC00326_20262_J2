def preenchimento_regiao(matriz, pos_inicial, novo_caractere):
    if not matriz: return []

    linhas = len(matriz)
    colunas = len(matriz[0])
    i_inicial, j_inicial = pos_inicial

    # Validação de limites
    if not (0 <= i_inicial < linhas and 0 <= j_inicial < colunas):
        return "Erro: Posição inicial fora dos limites da matriz."

    caractere_alvo = matriz[i_inicial][j_inicial]

    if caractere_alvo == novo_caractere:
        return matriz  # Não há nada a fazer

    # Nova matriz para não alterar a original
    nova_matriz = [linha[:] for linha in matriz]

    # Fila para controlar as posições a verificar
    fila = [(i_inicial, j_inicial)]

    while fila:
        i, j = fila.pop(0)

        if nova_matriz[i][j] == caractere_alvo:
            nova_matriz[i][j] = novo_caractere

            # Verifica vizinhos (cima, baixo, esquerda, direita)
            if i > 0: fila.append((i - 1, j))
            if i < linhas - 1: fila.append((i + 1, j))
            if j > 0: fila.append((i, j - 1))
            if j < colunas - 1: fila.append((i, j + 1))

    return nova_matriz


# Exemplo
imagem = [['.', '.', '-', '-'],
          ['.', '-', '-', '.'],
          ['.', '-', '.', '.'],
          ['.', '.', '.', '.']]

# Vamos preencher os '-' conectados começando da posição (0, 2) com '*'
nova_imagem = preenchimento_regiao(imagem, (0, 2), '*')
for l in nova_imagem: print(" ".join(l))