x = int(input("(1-Saudação,2-Mostar Data Fictícia,3-Sair). Escolha uma das opções:"))
while x != 3:
    if x==1 :
        print("Saudação")
    elif x==2 :
       print("Mostrar Data Fictícia")
    x = int(input("Digite 1, 2, 3:"))
    if x== 3:
        print("Saindo...")
