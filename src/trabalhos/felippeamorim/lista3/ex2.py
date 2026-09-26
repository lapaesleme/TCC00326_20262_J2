alunos = [
    {"nome": "João", "notas": [7, 8, 6, 9]},
    {"nome": "Maria", "notas": [9, 8, 10, 9]},
    {"nome": "Pedro", "notas": [5, 6, 4, 5]},
    {"nome": "Ana", "notas": [8, 7, 9, 8]}
]


def calcular_media(notas):
    soma = 0
    for nota in notas:
        soma += nota
    return soma / len(notas)


def classificar(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def acima_da_media(alunos):
    alunos_selecionados = []

    soma = 0
    for aluno in alunos:
        media = calcular_media(aluno["notas"])
        soma += media
    media_turma = soma / len(alunos)

    for aluno in alunos:
        media = calcular_media(aluno["notas"])
        if media > media_turma:
            alunos_selecionados.append({"nome":aluno["nome"],"media":media})

    return alunos_selecionados


def gerar_resumo(alunos):
    resumo = []

    for aluno in alunos:
        media = calcular_media(aluno["notas"])
        situacao = classificar(media)
        resumo.append({"nome":aluno["nome"],"situacao":situacao})

    return resumo

print(acima_da_media(alunos))
print(gerar_resumo(alunos))