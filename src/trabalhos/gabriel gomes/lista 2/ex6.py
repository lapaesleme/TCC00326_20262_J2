def somar(a,b):
    return a+b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    if b ==0:
        return "nao é possivel dividir por 0"
    return a/b
def subtrair(a,b):
    return a-b
def executar_operacao(a,b,operacao):
   return operacao(a,b)

print('a soma é',executar_operacao(10,5,somar))
print('a divisão é',executar_operacao(10,5,dividir))
print('a multiplicação é',executar_operacao(10,5,multiplicar))
print('a divisão é',executar_operacao(10,5,dividir))
