frases = [
"Medir o progresso da programação por linhas de código é como medir o progresso da construção de aeronaves em termos de peso.",
"Qualquer um pode escrever um código que   o computador entenda. Bons programadores escrevem códigos que os humanos entendam.",
"Um dos meus dias mais produtivos foi quando   eu joguei fora 1000 linhas de código.",
"Todos deveriam aprender  a   programar   porque isso   ensina a pensar",
"O software está comendo o   mundo, em famosa reflexão sobre o impacto da tecnologia na economia global."
]


def limpar_espacos(frase):
    frase_limpa = ""
    for palavra in frase.split():
        frase_limpa += palavra + " "
        print(palavra)
    return frase_limpa

def contar_palavras(frase):
    contagem = 0
    for palavra in frase.split():
        contagem += 1
    return contagem

print(limpar_espacos(frases[1]))
print(contar_palavras(limpar_espacos(frases[1])))



