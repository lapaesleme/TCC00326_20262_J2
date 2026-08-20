def media(nota1,nota2,nota3):
    return (nota1+nota2+nota3)/3
nome=input("digite seu nome:")

nota1=float(input("digite sua primeira nota:"))
nota2=float(input("digite sua segunda nota:"))
nota3=float(input("digite sua terceira nota:"))
mediaProvas = media(nota1,nota2,nota3)
print("\n--- BOLETIM ---")
print("aluno:",nome)
print("media",mediaProvas)

if mediaProvas >= 6:
    print("aprovado")
elif mediaProvas < 6:
    print("recuperação")
else:
    print("reprovado")
