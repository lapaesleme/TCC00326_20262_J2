tabuleiro = [['o', 'o', 'x'],
             ['x', 'x', 'o'],
             ['x', 'o', 'x']]


def jogo(tabuleiro):
    simbolo = None
    vitoria = True
    for i in range(len(tabuleiro)):
        if not simbolo:
            simbolo = tabuleiro[i][i]
        else:
            if (tabuleiro[i][i] != simbolo):
                vitoria = False
                break
    if (vitoria):
        return "vitoria na principal"

    simbolo = None
    vitoria = True
    for i in range(len(tabuleiro) - 1, -1, -1):
        if not simbolo:
            simbolo = tabuleiro[i][len(tabuleiro) - i - 1]
        else:
            if (tabuleiro[i][len(tabuleiro) - i - 1] != simbolo):
                vitoria = False
                break
    if (vitoria):
        return "vitoria na secundaria"

    for i in range(len(tabuleiro)):
        simbolo = None
        vitoria = True
        for j in range(len(tabuleiro)):
            if not simbolo:
                simbolo = tabuleiro[i][j]
            else:
                if (tabuleiro[i][j] != simbolo):
                    vitoria = False
                    break
        if (vitoria):
            return "vitoria na linha " + i

    for j in range(len(tabuleiro)):
        simbolo = None
        vitoria = True
        for i in range(len(tabuleiro)):
            if not simbolo:
                simbolo = tabuleiro[i][j]
            else:
                if (tabuleiro[i][j] != simbolo):
                    vitoria = False
                    break
        if (vitoria):
            if (vitoria):
                return "vitoria na coluna " + j
    return vitoria


print(jogo(tabuleiro))
