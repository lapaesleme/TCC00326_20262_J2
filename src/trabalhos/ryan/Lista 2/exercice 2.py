def obter_media():
    notas = []

    while True:
        try:
            entrada = input("Digite uma nota entre 0 e 10 (-1 para encerrar): ")
            nota = float(entrada)

            if nota == -1:
                break

            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Valor inválido! Digite uma nota entre 0 e 10 ou -1 para sair.")

        except ValueError:
            print("Entrada inválida! Digite um número válido.")
    if notas:
        return sum(notas) / len(notas)
    else:
        return None


def classificar_desempenho(media):
    if media >= 7:
        return "bom"
    elif 5 <= media < 7:
        return "regular"
    else:
        return "baixo"


if __name__ == "__main__":
    media = obter_media()

    if media is not None:
        print(f"\nMédia da turma: {media:.2f}")
        print(f"Desempenho: {classificar_desempenho(media)}")
    else:
        print("\nNenhuma nota válida foi informada.")