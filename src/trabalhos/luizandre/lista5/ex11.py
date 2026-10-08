def substituir_palavra(texto, palavra, substituicao):
    nova_linha = ''
    for elemento in texto.split():
        if elemento == palavra:
            nova_linha += substituicao + ' '
        else:
            nova_linha += elemento + ' '
    return nova_linha.strip()


try:
    with (open("texto.txt", "r") as origem,
          open("saida.txt", "w") as destino):
        for linha in origem:
            destino.write(substituir_palavra(linha, 'assistentes', '***') + '\n')
except FileNotFoundError as e:
    print("arquivo não existe: " + e.strerror)
except IOError as e:
    print("erro de leitura " + e.strerror)
else:
    print("aqui terminou de manipular o arquivo sem erros.")
finally:
    print("aqui terminou de manipular o arquivo independentemente se houve erro ou não.")
