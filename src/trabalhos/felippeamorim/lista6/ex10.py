def verifica_jogo_velha(tabuleiro):
    if len(tabuleiro) != 3 or any(len(linha) != 3 for linha in tabuleiro):
        return "Erro: Tabuleiro inválido."

    # Verifica linhas e colunas
    for i in range(3):
        # Linhas
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] != ' ':
            return f"Vencedor: {tabuleiro[i][0]}"
        # Colunas
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] != ' ':
            return f"Vencedor: {tabuleiro[0][i]}"

    # Diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != ' ':
        return f"Vencedor: {tabuleiro[0][0]}"
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != ' ':
        return f"Vencedor: {tabuleiro[0][2]}"

    # Verifica empate (ou continua se houver espaços em branco)
    for linha in tabuleiro:
        if ' ' in linha:
            return "Partida deve continuar."

    return "Empate."


# Exemplo
tab1 = [['X', 'O', 'X'], [' ', 'X', 'O'], ['O', ' ', 'X']]
print(verifica_jogo_velha(tab1))  # Saída: Vencedor: X