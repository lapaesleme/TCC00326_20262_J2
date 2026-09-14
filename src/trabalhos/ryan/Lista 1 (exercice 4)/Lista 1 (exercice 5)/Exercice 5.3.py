contador = 0

P1 = print("Quem ganhou a copa do mundo em 1994 ??? ")
print("A) Brasil")
print("B) Holanda")
print("C) Espanha")
print("D) Argentina")
print("E) Inglaterra")
input(": ")
resposta = "A"

if "A"== resposta:
    print("Você Acertou !!!")
    contador =+1
elif "A" != resposta:
    print("Você Errou !!!")

P2 = print("Qual é o melhor time do Rio de Janeiro ???")
print("A) Fluminense ")
print("B) Vasco ")
print("C) Botafogo")
print("D) Palmeiras")
print("E) Flamengo ")
input(": ")

gabarito = "E"
if "E" == gabarito:
    print("Você Acertou!!!")
    contador =+1
elif "E"!= gabarito:
     print("Você Errou !!!")

P3 = print("Qual é o maior continente do mundo ???")
print("A) Oceania ")
print("B) Americano")
print("C) Asiático")
print("D) Africano")
print("E) Europeu")
input(": ")

i = "C"
if i == "C" :
    print("Você Acertou !!!")
    contador =+1
elif i!= "C":
    print("Você Errou !!!")

print("Vc acertou: ", contador,"de 3")
print()
