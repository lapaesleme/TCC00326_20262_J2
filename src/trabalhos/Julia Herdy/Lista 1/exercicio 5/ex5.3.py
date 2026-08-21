def calcular_pontuacao(acertos):
    return acertos * 10


pontuacao = 0

print("=== JOGO DE PERGUNTAS ===")

# Pergunta 1
print("\n1. Qual é a capital do Brasil?")
print("A) São Paulo")
print("B) Brasília")
print("C) Rio de Janeiro")
resposta = input("Resposta: ")

if resposta.upper() == "B":
    pontuacao += 1

# Pergunta 2
print("\n2. Quanto é 12 x 12?")
print("A) 24")
print("B) 12")
print("C) 144")
resposta = input("Resposta: ")

if resposta.upper() == "C":
    pontuacao += 1

# Pergunta 3
print("\n3. Qual time é do estado do Rio de Janeiro?")
print("A) Santos")
print("B) Internacional")
print("C) Botafogo")
resposta = input("Resposta: ")

if resposta.upper() == "C":
    pontuacao += 1

resultado = calcular_pontuacao(pontuacao)

print("\n=== RESULTADO ===")
print("Você acertou", pontuacao, "de 3 perguntas.")
print("Pontuação final:", resultado)