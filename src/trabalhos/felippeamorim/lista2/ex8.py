def processar_textos(textos, transformacao):
    resultado = []

    for texto in textos:
        resultado.append(transformacao(texto))

    return resultado


def maiusculas(texto):
    return texto.upper()


def remover_espacos(texto):
    return texto.replace(" ", "")


def contar_caracteres(texto):
    return len(texto)


textos = ["ola mundo", "python", "programacao"]

print(processar_textos(textos, maiusculas))
print(processar_textos(textos, remover_espacos))
print(processar_textos(textos, contar_caracteres))