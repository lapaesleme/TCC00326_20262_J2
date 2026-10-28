def para_maiusculas(texto):
    return texto.upper()
def remover_espacos(texto):
    return texto.replace(" ","")
def remover_caracteres_extras(texto):
    caracteres = ".,!?;:"
    for caractere in caracteres:
        texto = texto.replace(caractere, "")
    return texto
def processar_textos(texto, transformacao):
    nova_lista = []
    for texto in textos:
        novo_texto = transformacao(texto)
        nova_lista.append(novo_texto)
    return nova_lista
textos = ["Olá, mundo!", "Python é legal.", "Programacao; é muito bom!"]
print("textos originais:")
print(textos)
print("maiusculas:")
print(processar_textos(textos, para_maiusculas))
print("sem espacos:")
print(processar_textos(textos, remover_espacos))
print("sem caracteres extras:")
print(processar_textos(textos, remover_caracteres_extras))