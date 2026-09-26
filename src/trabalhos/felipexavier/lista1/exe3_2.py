ent = input("deseja usar menu interativo? (s/n)")
while ent == "s":
    print("1: saudação, 2: mostrar data, 3: sair")
    op = (input("qual opção deseja usar?"))
    if op == "1":
        print("saudação")
    elif op == "2":
        print("20/08/2026")
    elif op == "3":
        ent = "n"
print("saiu")