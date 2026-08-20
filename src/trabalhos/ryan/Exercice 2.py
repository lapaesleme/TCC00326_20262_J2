idade = int(input("Diga sua idade: "))

if idade >= 18 :
    print("Você é maior de idade. ")

else:
    print("Você é menor de idade. ")


valor = int(input("Digite um valor: "))

if valor > 0:
    print("Valor é positivo. ")

elif valor < 0 :
    print("Valor é negativo ")

else:
    print("O valor é nulo. ")


numero = int(input("Diga um numero"))

if numero % 2 == 0:
    print("O valor é par. ")

else:
    print("O numero é ímpar. ")



media = int(input("Diga sua primeira nota: "))
nota = int(input("Diga sua segunda nota: "))

if media + nota / 2 >= 6:
    print("Parabéns, você foi aprovado !!! ")

else:
    print("Infelizmente, você está reprovado !!! ")


x= int(input("Digite um algarismo: "))
y = int(input("Digite um segundo algarismo: "))
Soma = x + y
Subtracao = x - y
Produto = x * y
Divisao  = x / y

print("Soma : " , Soma, "Subtracao: ", Subtracao, "Produto: ", Produto,"e Divisão : ", Divisao)

if x / y == 0:
    print("O resultado é 0 ")

