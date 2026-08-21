def celsius_farenheit(celsius):
    return celsius * 9 / 5 + 32

def farenheit_celsius(farenheit):
    return (farenheit - 32) * 5 / 9

opcao = 0
while opcao != 3:
    print("\n=== CONVERSOR DE TEMPERATURAS ===")
    print("1- celsius")
    print("2- farenheit")
    print("3- sair")

    opcao = int(input("escolha uma opção abaixo:"))
    if opcao == 1:
        celsius = float(input("digite a temperatura em celsius:"))
        farenheit = celsius_farenheit(celsius)
        print("temperatura em farenheit:", farenheit)
    elif opcao == 2:
        farenheit = float(input('digite a temperatura em farenheit:'))
        celsius = farenheit_celsius(farenheit)
        print("temperatura em celsius:", celsius)
    elif opcao == 3:
        print("operação finalizada.")
    else:
        print("opção invalida")