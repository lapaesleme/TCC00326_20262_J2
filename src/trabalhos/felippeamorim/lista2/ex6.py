def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b


def executar_operacao(a, b, operacao):
    return operacao(a, b)


print(executar_operacao(10, 5, somar))
print(executar_operacao(10, 5, subtrair))
print(executar_operacao(10, 5, multiplicar))
print(executar_operacao(10, 5, dividir))