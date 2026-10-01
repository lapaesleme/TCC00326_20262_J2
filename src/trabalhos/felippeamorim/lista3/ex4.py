frases = [
    "Python é uma linguagem de programação muito utilizada.",
    "As funções ajudam a organizar e reutilizar o código.",
    "Programar exige lógica, prática e dedicação.",
    "O desenvolvimento de sistemas envolve análise, programação e testes."
]


def limpar_texto(texto):
    return texto.strip()


def contar_palavras(texto):
    return len(texto.split())


def identificar_frases_longas(frases):
    longas = []

    for frase in frases:
        if contar_palavras(frase) > 8:
            longas.append(frase)

    return longas


def contar_termos_chave(frases, termos):
    ocorrencias = {}

    for termo in termos:
        contador = 0

        for frase in frases:
            palavras = frase.lower().split()

            for palavra in palavras:
                palavra = palavra.strip(".,!?;:")

                if palavra == termo.lower():
                    contador += 1

        ocorrencias[termo] = contador

    return ocorrencias


def gerar_relatorio(frases, termos):
    frases_limpas = []

    for frase in frases:
        frases_limpas.append(limpar_texto(frase))

    total_palavras = 0

    for frase in frases_limpas:
        total_palavras += contar_palavras(frase)

    frases_longas = identificar_frases_longas(frases_limpas)
    ocorrencias = contar_termos_chave(frases_limpas, termos)

    print("===== RELATÓRIO =====")
    print(f"Quantidade de frases: {len(frases_limpas)}")
    print(f"Quantidade total de palavras: {total_palavras}")

    print("\nFrases longas:")
    for frase in frases_longas:
        print("-", frase)

    print("\nOcorrências dos termos-chave:")
    for termo, quantidade in ocorrencias.items():
        print(f"- {termo}: {quantidade}")


termos_chave = ["programação", "Python", "funções"]

gerar_relatorio(frases, termos_chave)