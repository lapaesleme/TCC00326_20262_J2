def somar(a,b):
    return  a + b
def subtrair(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir (a,b):
    return a / b
def executar_operacao(a,b,operacao):
    return operacao(a,b)
print("soma:", executar_operacao(10,5,somar))
print("subtracao", executar_operacao(10,5,subtrair))
print("multiplicacao", executar_operacao(10,5,multiplicar))
print("divisao", executar_operacao(10,5,dividir))
