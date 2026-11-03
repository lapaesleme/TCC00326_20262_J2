m = [[1, 10, 20, 30],
     [5, 15, 27, 36],
     [11, 22, 32, 41],
     [16, 26, 35, 46],
     [24, 31, 40, 51]]
n = 23


def buscar(m, n):
    for i in range(0, len(m)):
        if m[i][0] > n:
            break;
        for j in range(0, len(m[i])):
            if m[i][j] > n:
                break;
            if m[i][j] == n:
                return (i, j)
    return None
