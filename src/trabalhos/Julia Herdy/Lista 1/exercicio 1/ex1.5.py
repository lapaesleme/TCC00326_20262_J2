numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
metodo = input("Digite a operação matemática que deseja realizar (soma, subtração, divisão ou multiplicação):")

if metodo == "soma":
    print ("A soma do número", numero1, "com o número", numero2, "é igual a", numero1 + numero2)
elif metodo == "subtração":
    print("A subtração do número", numero1, "com o número", numero2, "é igual a", numero1 - numero2)
elif metodo == "divisão":
    print("A divisão do número", numero1, "com o número", numero2, "é igual a", numero1/numero2)
elif metodo == "multiplicação":
    print("A multiplicação do número", numero1, "com o número", numero2, "é igual a", numero1*numero2)