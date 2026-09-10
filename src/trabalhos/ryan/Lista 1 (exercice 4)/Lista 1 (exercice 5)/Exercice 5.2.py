def main():
    nomes = []
    print("Digite nomes para cadastrar. Digite 'sair' para encerrar.")
    while True:
        nome = input("Digite um nome: ").strip()  # Remove espaços extras

        if nome.lower() == "sair":
            break

        if not nome:
            print("⚠ Nome vazio não é permitido. Tente novamente.")
            continue

    print("\nNomes cadastrados:")
    for i, nome in enumerate(nomes, start=1):
        print(f"{i}. {nome}")


if __name__ == "__main__":
    main()