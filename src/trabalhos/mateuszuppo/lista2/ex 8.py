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

texto = ["ola mundo", "python", "programacao"]

print(processar_textos(texto, maiusculas))
print(processar_textos(texto, remover_espacos))
print(processar_textos(texto, contar_caracteres))