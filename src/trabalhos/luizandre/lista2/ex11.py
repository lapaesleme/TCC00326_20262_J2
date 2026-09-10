
v = [ 1,4,5,8,9,0, 2]

def buscar(vetor, n, i ):
    if 0 <= i < len(vetor):
        if vetor[i] == n:
            return True
        else:
            return buscar(vetor, n, i + 1)
    else:
        return False

print (buscar(v, 44, 0))

