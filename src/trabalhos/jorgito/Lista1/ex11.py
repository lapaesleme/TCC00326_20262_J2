print ("Hello World")

x1 = float(input('Digite o primeiro ponto: '))
y1 = float(input('Digite o terceiro ponto: '))
x2 = float(input('Digite o segundo ponto: '))
y2 = float(input('Digite o quarto ponto: '))
distancia_1 = (x2 - x1) ** 2
distancia_2 = (y2 - y1)  ** 2
d = distancia_1 + distancia_2
print(d ** 0.5)


