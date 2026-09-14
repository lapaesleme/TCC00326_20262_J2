
def filtrar_palavras(palavras,tamanho_min):
    resultado = []
    for palavra in palavras:
        if len(palavra) >= tamanho_min:
            resultado.append(palavra)
    return resultado
palavras = ['casa','pai','incompleto','incostitucional','adpto']
resultado = filtrar_palavras(palavras,5)
print(resultado)
