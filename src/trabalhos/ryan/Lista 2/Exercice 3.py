
def eh_primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limite = int(n ** 0.5) + 1
    for i in range(3, limite, 2):
        if n % i == 0:
            return False
    return True


def main():
    try:

        inicio = int(input("Digite o primeiro número do intervalo: "))
        fim = int(input("Digite o segundo número do intervalo: "))


        if inicio > fim:
            inicio, fim = fim, inicio


        primos = [num for num in range(inicio, fim + 1) if eh_primo(num)]


        if primos:
            print(f"Números primos entre {inicio} e {fim}: {primos}")
        else:
            print(f"Não há números primos entre {inicio} e {fim}.")

    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.")


if __name__ == "__main__":
    main()

