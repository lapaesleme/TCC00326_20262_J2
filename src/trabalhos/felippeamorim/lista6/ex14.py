def gerar_identidade(ordem):
    if type(ordem) != int or ordem <= 0:
        return "Erro: A ordem deve ser um número inteiro positivo."

    identidade = []
    for i in range(ordem):
        linha = []
        for j in range(ordem):
            if i == j:
                linha.append(1)
            else:
                linha.append(0)
        identidade.append(linha)
    return identidade


def verifica_identidade(matriz):
    if not matriz:
        return False

    linhas = len(matriz)
    # Verifica se é quadrada
    for linha in matriz:
        if len(linha) != linhas:
            return False

    for i in range(linhas):
        for j in range(linhas):
            if i == j and matriz[i][j] != 1:
                return False
            if i != j and matriz[i][j] != 0:
                return False
    return True


# Exemplo
id_3 = gerar_identidade(3)
print("Matriz gerada:", id_3)
print("É identidade?", verifica_identidade(id_3))
print("É identidade?", verifica_identidade([[1, 0], [0, 2]]))