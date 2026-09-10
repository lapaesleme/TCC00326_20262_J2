def calcular_pontuacao(pontos):
    return sum(pontos)


pontos = []

print("1. Qual é a capital do Brasil?")
print("A) São Paulo")
print("B) Brasília")
print("C) Rio de Janeiro")
resposta = input("Resposta: ")

if resposta.upper() == "B":
    pontos.append(1)
else:
    pontos.append(0)


print("\n2. Quanto é 5 + 5?")
print("A) 8")
print("B) 10")
print("C) 12")
resposta = input("Resposta: ")

if resposta.upper() == "B":
    pontos.append(1)
else:
    pontos.append(0)


print("\n3. Qual planeta é conhecido como Planeta Vermelho?")
print("A) Marte")
print("B) Vênus")
print("C) Júpiter")
resposta = input("Resposta: ")

if resposta.upper() == "A":
    pontos.append(1)
else:
    pontos.append(0)


pontuacao = calcular_pontuacao(pontos)

print("\nPontuação final:", pontuacao, "de 3")