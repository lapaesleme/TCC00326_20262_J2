#Programa para ler duas notas e informar se o aluno teve média superior a 6 e foi aprovado
P1=float(input("Insira a primeira nota do aluno:"))
P2=float(input("insira a segunda nota do aluno:"))
if (P1+P2)/2>=6:
    print("Aluno aprovado!")
elif (P1+P2)/2<6 and (P1+P2)/2>=4:
    print("Aluno em recuperação!")
else:
    print("Aluno reprovado :(")