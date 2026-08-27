alunos = [
    {"nome": "João", "notas": [7, 8, 6, 9]},
    {"nome": "Maria", "notas": [9, 8, 10, 9]},
    {"nome": "Pedro", "notas": [5, 6, 4, 5]},
    {"nome": "Ana", "notas": [8, 7, 9, 8]}
]


def calcular_media(notas):
    return sum(notas) / len(notas)


def classificar(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def acima_da_media(alunos):
    medias = []

    for aluno in alunos:
        media = calcular_media(aluno["notas"])
        medias.append(media)

    media_turma = sum(medias) / len(medias)

    return media_turma


def gerar_resumo(alunos):
    media_turma = acima_da_media(alunos)

    print("Média da turma:", media_turma)
    print()

    for aluno in alunos:
        media = calcular_media(aluno["notas"])
        situacao = classificar(media)

        print("Aluno:", aluno["nome"])
        print("Média:", media)
        print("Situação:", situacao)
        print()


gerar_resumo(alunos)