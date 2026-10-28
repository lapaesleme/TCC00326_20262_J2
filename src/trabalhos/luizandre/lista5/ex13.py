def gerar_arquivo():
    from random import randint

    with open("numeros.txt", "w") as arquivo:
        for i in range(1000):
            arquivo.write(str(randint(0, 99)) + "\n")


def gerar_estatisticas(nome_arquivo):
    contador = 0
    soma = 0
    max = float('-infinity')
    min = float('infinity')
    with open("numeros.txt", "r") as arquivo:
        for linha in arquivo:
            contador += 1
            soma += int(linha)
            if (int(linha) > max):
                max = int(linha)
            if (int(linha) < min):
                min = int(linha)

    media = soma / contador
    return {'qtd_numeros': contador, 'soma': soma, 'max': max, 'min': min, 'media': media}


def gerar_histograma(nome_arquivo):
    histograma = [0] * 100
    with open("numeros.txt", "r") as arquivo:
        for linha in arquivo:
            numero = int(linha)
            histograma[numero] += 1
    return histograma


gerar_arquivo()
print(gerar_estatisticas("numeros.txt"))
print(gerar_histograma("numeros.txt"))
