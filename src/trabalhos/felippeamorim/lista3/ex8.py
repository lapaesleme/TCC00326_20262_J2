tarefas = [
    {
        "titulo": "Fazer trabalho de Python",
        "prioridade": 1,
        "duracao": 120,
        "status": "pendente"
    },
    {
        "titulo": "Estudar para a prova",
        "prioridade": 2,
        "duracao": 90,
        "status": "pendente"
    },
    {
        "titulo": "Fazer exercícios",
        "prioridade": 3,
        "duracao": 60,
        "status": "concluida"
    },
    {
        "titulo": "Revisar conteúdo",
        "prioridade": 1,
        "duracao": 45,
        "status": "pendente"
    }
]


# 1. Calcular o tempo total das tarefas pendentes
tempo_total = 0

for tarefa in tarefas:
    if tarefa["status"] == "pendente":
        tempo_total += tarefa["duracao"]

print("Tempo total pendente:", tempo_total, "minutos")


# 2. Listar tarefas urgentes não concluídas
print("\nTarefas urgentes:")

for tarefa in tarefas:
    if tarefa["prioridade"] == 1 and tarefa["status"] != "concluida":
        print("-", tarefa["titulo"])


# 3. Ordenar tarefas pendentes por prioridade
pendentes = []

for tarefa in tarefas:
    if tarefa["status"] == "pendente":
        pendentes.append(tarefa)

pendentes.sort(key=lambda tarefa: tarefa["prioridade"])


print("\nTarefas pendentes por prioridade:")

for tarefa in pendentes:
    print(
        f"Prioridade {tarefa['prioridade']} - "
        f"{tarefa['titulo']} - "
        f"{tarefa['duracao']} minutos"
    )