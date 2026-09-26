def transformar(lista, funcao):
    resultado = []

    for item in lista:
        resultado.append(funcao(item))

    return resultado


# 1. Aplicar desconto de 10% nos preços
def aplicar_desconto(preco):
    return preco * 0.90


precos = [100, 200, 50, 80]

print("Preços com desconto:")
print(transformar(precos, aplicar_desconto))


# 2. Colocar nomes em maiúsculas
def maiusculas(nome):
    return nome.upper()


nomes = ["joão", "maria", "carlos", "ana"]

print("Nomes em maiúsculas:")
print(transformar(nomes, maiusculas))


# 3. Converter temperaturas de Celsius para Fahrenheit
def celsius_para_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


temperaturas = [0, 10, 20, 30, 40]

print("Temperaturas em Fahrenheit:")
print(transformar(temperaturas, celsius_para_fahrenheit))