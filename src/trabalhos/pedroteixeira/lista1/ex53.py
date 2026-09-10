def mostrar_pontuacao(pontos):
    print("Pontuação final:", pontos, "de 3")
    if pontos == 3:
        print("Parabéns! Você acertou tudo!")
    elif pontos >= 2:
        print("Muito bem!")
    else:
        print("Continue estudando!")
pontos = 0
print("=== QUIZ ===")
print("n1. Qual é a capital do Brasil?")
print("A) São Paulo")
print("B) Brasília")
print("C) Rio de Janeiro")
resposta = input("Resposta: ").lower()
if resposta == "b":
    pontos += 1
print("n2. Quanto é 2 + 2?")
print("A) 3")
print("B) 4")
print("C) 5")
resposta = input("Resposta: ").lower()
if resposta == "b":
    pontos += 1
print("n3. Qual linguagem estamos estudando?")
print("A) Python")
print("B) Java")
print("C) C++")
resposta = input("Resposta: ").lower()
if resposta == "a":
    pontos += 1
mostrar_pontuacao(pontos)