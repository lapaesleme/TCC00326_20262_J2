numeros = [3,2,6,8,2,7,3,0,9,1]


def soma (vetor,i):
    if 0 <= i < len(vetor):
        return vetor[i] + soma(vetor, i+1)
    else:
        return 0

print(soma(numeros,0))
