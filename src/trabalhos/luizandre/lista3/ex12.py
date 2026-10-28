raiz = {"conteudo": []}
pasta1 = {"nome": "dir 1", "conteudo": []}
raiz["conteudo"].append(pasta1)
arq1 = {"nome": "arq1.py"}
pasta1["conteudo"].append(arq1)
pasta2 = {"nome": "dir 2", "conteudo": []}
pasta1["conteudo"].append(pasta2)
arq2 = {"nome": "arq2.py"}
arq3 = {"nome": "arq3.py"}
pasta2["conteudo"].append(arq2)
pasta2["conteudo"].append(arq3)

print(raiz)


def eh_pasta(entrada):
    if "conteudo" in entrada:
        return True
    return False


def buscar(arquivo_nome, pasta):
    if eh_pasta(pasta):
        for entrada in pasta["conteudo"]:
            if eh_pasta(entrada):
                return buscar(arquivo_nome, entrada)
            else:
                if arquivo_nome == entrada["nome"]:
                    return pasta
        return None
    else:
        return None


print(buscar("arq2.py", raiz))
