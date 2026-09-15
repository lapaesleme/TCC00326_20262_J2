def corretor():
    certo = 0
    if x == "B":
        certo+=1
    if y == "A":
        certo +=1
    if z == "A":
        certo +=1
    return certo

print("Pergunta 1: Qual a cor do ceu?")
print("A- verde", "B- azul", "C- amarelo")
x = input()
print("Pergunta 2: Qual a cor do sol?")
print("A- amarelo", "B- verde", "C- azul")
y = input()
print("Pergunta 3: Qual a cor da grama?")
print("A- verde", "B- amarelo", "C- azul")
z = input()
print(corretor())