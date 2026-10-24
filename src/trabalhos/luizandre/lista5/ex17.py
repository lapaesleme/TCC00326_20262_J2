from pathlib import Path

diretorio = Path('.')
with open("saida.txt", "w") as destino:
    for item in diretorio.iterdir():
        if item.is_file():
            if (item.name != 'saida.txt'):
                with open(item.name, "r") as origem:
                    for linha in origem:
                        destino.write(linha)
