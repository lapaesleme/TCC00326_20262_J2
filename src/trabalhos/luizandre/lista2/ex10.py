v =[ 2, 3, 5, 6]

def soma(vetor, i ):
    if  0 <= i < len(vetor):
        return vetor[i] + soma(vetor, i+1)
    else:
        return 0


print(soma(v, 0))