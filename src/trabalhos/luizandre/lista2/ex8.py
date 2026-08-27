textos = ["tdagfasdf", "dsfas", ""]

def maiusculas (texto ):
    return texto.upper()

def processar_textos (textos, processador):
    novaLista = []
    for t in textos:
        novaLista.append(maiusculas(t))
    return novaLista

print (processar_textos(textos, maiusculas))