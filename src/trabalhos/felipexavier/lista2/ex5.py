coringa = []
trad = []

def traducao (n):
    for i in k:
        i = int(i)
        trad.append(i)

def op (j):
    return j * 12

def contas (j,op):
    for i in j:
        i = op(i)
        coringa.append(i)

k = input("Quais números deseja multiplicar por 12? ").split()
traducao (k)
contas (trad,op)
print(coringa)