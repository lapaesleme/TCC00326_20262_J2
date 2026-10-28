digito = 0

while digito != 6:
    print("\n === CONVERSOR DE MEDIDA ==== ")
    print("1 - Converter Kelvin para Celsius ")
    print("2 - Converter Celsius para Kelvin ")
    print("3 - Converter Fahrenhaint para Celsius ")
    print("4 - Converter  Celsius para Fahrenhaint")
    print("5 - Converter Fahrenhaint para Kelvin ")
    print("6 -  Converter Kelvin para Fahrenhaint")
    print("Digite uma das opcoes para iniciar:  ")
    def f_c(celsius):
        return (celsius - 32) * 5 / 9
    def c_f(farenhaint):
        return (farenhaint * 9 / 5) + 32 

    def k_c(i):
        return i - 273, 15

    def c_k(d):
        return d - 273, 15

    def k_f(r):
        return (r - 273, 15) * 9/5 + 32

    def f_k(l):
        return (l-32) * 5/9 + 273,15

    digito = int(input("Selecione uma opção, para dar continuidade: "))

    if digito == 1:
         temp = float(input("Digite a temperatura Kelvin:   K"))
         h =  k_c(i)
         print(" A temperatura foi convertida !!! ")
         print( " A temperatura celsius é de :  ", h)

    elif dígito == 2:
        force = float(input("Digite a temperatura Celsius:   "))
        j = c_k(d)
        print(" A temperatura foi convertida !!! ")
        print(" A temperatura kelvin é de:     ", j)

    elif dígito == 3:
        life = float(input("Digite a temperatura Fahrenhaint:    "))
        p = f_c(celsius)
        print(" A temperatura foi convertida !!! ")
        print(" A temperatura Celsius é de:    ", p)

    elif dígito == 4:
        need = float(input(" Digite a temperatura Celsius:  "))
        m = c_f(farenhaint)
        print(" A temperatura foi convertida !!!")
        print(" A temperatura Fahrenhaint é de:  ", m)

    elif dígito == 5:
        obssecion = float(input(" Digite a temperatura Farenhaint"))
        a = f_k(l)
        print = (" A temperatura foi convertida !!! ")
        print = (" A temperatura Kelvin é de:  ", a)

    else:
        win = float(input("Digite a temperatura Kelvin"))
        u = k_f(r)
        print("A temperatura foi convertida !!! ")
        print(" A temperatura Farenhaint é de:    " , u )
