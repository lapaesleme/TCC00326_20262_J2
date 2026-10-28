def celsius_para_fahrenheit():
    c = float(input("Digite a temperatura em Celsius (°C): "))
    f = (c * 9 / 5) + 32
    print(f"{c}°C equivale a {f:.2f}°F")


def fahrenheit_para_celsius():
    f = float(input("Digite a temperatura em Fahrenheit (°F): "))
    c = (f - 32) * 5 / 9
    print(f"{f}°F equivale a {c:.2f}°C")


opcao = 0

while opcao != 3:
    print("\n--- CONVERSOR DE TEMPERATURAS ---")
    print("1- Celsius para Fahrenheit")
    print("2- Fahrenheit para Celsius")
    print("3- Sair")

    opcao = int(input("Escolha a conversão desejada: "))
    print("")

    if opcao == 1:
        celsius_para_fahrenheit()
    elif opcao == 2:
        fahrenheit_para_celsius()
    elif opcao == 3:
        print("Saindo do programa...")
    else:
        print("Opção inválida! Tente novamente.")