try:
    with open("teste2.txt", "r") as file:
        print(file.readline(), end="\n")
except FileNotFoundError as e:
    print("arquivo não existe: " + e.strerror)
except IOError as e:
    print("erro de leitura " + e.strerror)
else:
    print("aqui terminou de manipular o arquivo sem erros.")
finally:
    print("aqui terminou de manipular o arquivo independentemente se houve erro ou não.")
