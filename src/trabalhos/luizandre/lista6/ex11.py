m = [[3, 6, 1], [65, 1, 2], [2, 3, 4], [4, 5, 6], [5, 6, 7], [6, 7, 8]]
n = 6


def buscar(m, n):
    linhas = len(m)
    colunas = len(m[0])
    resultado = {"qtd": 0, "posicoes": []}
    for i in range(0, linhas):
        for j in range(0, colunas):
            if m[i][j] == n:
                resultado["qtd"] += 1
                resultado["posicoes"].append((i, j))
    return resultado


print(buscar(m, n))
