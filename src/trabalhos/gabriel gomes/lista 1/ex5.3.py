pontuaçao = 0
print("=== JOGO DE PERGUNTAS ===")
print("/n1. Qual linguagem estamos estudando?")
print("(A) Python")
print("(B) SQL")
print("(C) Java")

resposta = input("resposta:").upper()
if resposta == "A":
    print("resposta certa!")
    pontuaçao =+ 1
else:
    print("resposta errada!")

print("\n2. Qual dessas é uma função?")
print("(A) print")
print("(B) append")
print("(C) As duas acima")
resposta = input("resposta:").upper()
if resposta == "C":
    print("resposta certa!")
    pontuaçao +=1
else:
    print("resposta errada!")

print("\n3. Qual estrutura é usada para repetição?")
print("(A) if")
print("(B) else")
print("(C) for")
resposta = input("resposta:").upper()
if resposta == "C":
    print("resposta certa!")
    pontuaçao +=1
else:
    print("resposta errada!")

print("\n=== RESULTADO ===")
print("Sua pontuação foi:",pontuaçao,"de 3")