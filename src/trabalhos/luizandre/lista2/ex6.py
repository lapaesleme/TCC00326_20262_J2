def somar(a, b):
    return a + b


def executar_operacao(a, b, operacao):
    return operacao(a, b)


a = 2
b = 3
print(executar_operacao(a, b, somar))
