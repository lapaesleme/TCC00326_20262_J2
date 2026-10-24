def ordena_linhas(matriz):
    if not matriz:
        return []

    nova_matriz = []
    for linha in matriz:
        # Cria uma cópia da linha para não alterar a original
        linha_copia = linha[:]
        # Algoritmo de ordenação simples (Bubble Sort) para evitar bibliotecas
        n = len(linha_copia)
        for i in range(n):
            for j in range(0, n - i - 1):
                if linha_copia[j] > linha_copia[j + 1]:
                    linha_copia[j], linha_copia[j + 1] = linha_copia[j + 1], linha_copia[j]
        nova_matriz.append(linha_copia)

    return nova_matriz


# Exemplo
M = [[3, 1, 2], [9, 5, 7]]
M_ord = ordena_linhas(M)
print("Original:", M)
print("Ordenada:", M_ord)