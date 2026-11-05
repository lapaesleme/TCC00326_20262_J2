grade = [[0, 0, 1, 0],
         [0, 0, 0, 0],
         [0, 1, 1, 0],
         [0, 0, 0, 0]]

count = 0


def caminhos(grade, inicio):
    global count
    if (inicio[0] == len(grade) - 1 and inicio[1] == len(grade[0]) - 1):
        count += 1
    else:
        nova_linha = inicio[0] + 1
        nova_coluna = inicio[1]
        if (nova_linha < len(grade) and nova_coluna < len(grade[0])):
            if (grade[nova_linha][nova_coluna] == 0):
                caminhos(grade, [nova_linha, nova_coluna])

        nova_linha = inicio[0]
        nova_coluna = inicio[1] + 1
        if (nova_linha < len(grade) and nova_coluna < len(grade[0])):
            if (grade[nova_linha][nova_coluna] == 0):
                caminhos(grade, [inicio[0], inicio[1] + 1])


caminhos(grade, [0, 0])
print(count)
