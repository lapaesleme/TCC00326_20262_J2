lista = [1,2,3,4,5,6,7,8,9,10]


def recursiva(listas, n, i):
    if 0 <= i < len(listas):
        if listas[i] == n:
            return True
        else:
            return recursiva(listas,n, i + 1)

    else:
        return False

print(recursiva(lista, 45, 0))
