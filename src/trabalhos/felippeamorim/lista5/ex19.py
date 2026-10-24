import json

with open("alunos.json", "r") as arquivo:
    alunos = json.load(arquivo)

aprovados = []
reprovados = []

for aluno in alunos:
    nome = aluno["nome"]
    notas = aluno["notas"]

    media = sum(notas) / len(notas)

    dados = {"nome": nome, "media": media}

    if media >= 6:
        aprovados.append(dados)
    else:
        reprovados.append(dados)

relatorio = {
    "aprovados": aprovados,
    "reprovados": reprovados
}

with open("relatorio.json", "w") as arquivo:
    json.dump(relatorio, arquivo, indent=4)

print("Relatório criado!")