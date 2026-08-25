def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


print("=== CONVERSOR DE TEMPERATURA ===")
print("1 - Celsius para Fahrenheit")
print("2 - Fahrenheit para Celsius")

opcao = input("Escolha uma opção: ")

if opcao == "1":
    celsius = float(input("Digite a temperatura em Celsius: "))
    resultado = celsius_para_fahrenheit(celsius)
    print(f"Resultado: {resultado:.2f} °F")

elif opcao == "2":
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    resultado = fahrenheit_para_celsius(fahrenheit)
    print(f"Resultado:{resultado:.2f} °C")

else:
    print("Opção inválida!")