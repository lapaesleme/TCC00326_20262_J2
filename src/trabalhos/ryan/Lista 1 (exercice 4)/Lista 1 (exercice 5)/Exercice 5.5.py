digito = 0

while digito != 6:
    print("\n === CONVERSOR DE MEDIDA ==== ")
    print("1 - Converter Kelvin para Celsius ")
    print(" 2 - Converter Celsius para Kelvin ")
    print(" 3 - Converter Fahrenhaint para Celsius ")
    print("4 - Converter  Celsius para Fahrenhaint")
    print("5 - Converter Fahrenhaint para Kelvin ")
    print("6 -  Converter Kelvin para Fahrenhaint")
    print("Digite uma das opcoes para iniciar:  ")

    digito = int(input("Selecione uma opção, para dar continuidade: ")

    if opcao == 1:
         k = float(input("Digite a temperatura Kelvin:   K"))

         if k > 0:
             k = k - 273,15

             print("A conversão foi feita !!!")
             print(" A conversão é de:    ° ")

         elif k < 0:
             k = k - 273,15°

             print("A coversão foi feita !!! ")
             print("A escala celsius é de    ° ")

         else:
             print("Não foi possível realizar a conversão !!!")


