grade = [[0, 0, 1, 0],
         [0, 0, 0, 0],
         [1, 1, 1, 0],
         [2, 0, 0, 0]]


def soma(grade):
    soma = 0
    for i in range(len(grade)):
        for j in range(len(grade[0])):
            if (i == 0
                    or j == 0
                    or i == len(grade) - 1
                    or j == len(grade[0]) - 1):
                soma += grade[i][j]
    return soma


print(soma(grade))
