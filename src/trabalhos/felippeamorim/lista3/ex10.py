senhas = [
    "Senha123!",
    "abc123",
    "Teste@2026",
    "senha123!",
    "ABCDEF12",
    "Python#1"
]


def validar_tamanho(senha):
    if len(senha) >= 8:
        return True
    else:
        return False


def validar_numero(senha):
    for caractere in senha:
        if caractere.isdigit():
            return True

    return False


def validar_maiuscula(senha):
    for caractere in senha:
        if caractere.isupper():
            return True

    return False


def validar_especial(senha):

    especiais = "!@#$%&*"

    for caractere in senha:
        if caractere in especiais:
            return True

    return False


def validar_senha(senha):

    tamanho = validar_tamanho(senha)
    numero = validar_numero(senha)
    maiuscula = validar_maiuscula(senha)
    especial = validar_especial(senha)

    if tamanho and numero and maiuscula and especial:
        return "Forte"
    else:
        return "Fraca"


for senha in senhas:

    resultado = validar_senha(senha)

    print(senha, "-", resultado)