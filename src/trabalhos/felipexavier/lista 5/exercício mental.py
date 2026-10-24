class produto ():
    def __init__(self, codigo, nome, categoria, quantidade, valor_venda, valor_compra, valor_lucro, valor_total):
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.valor_venda = valor_venda
        self.valor_compra = valor_compra
        self.valor_lucro = 0
        self.valor_total = 0
        self.valor_lucro = self.valor_venda - self.valor_compra
        self.valor_total = self.valor_venda * self.quantidade

    def __str__(self):
        return f"Código: {self.codigo}, Nome: {self.nome}, Categoria: {self.categoria}, Quantidade: {self.quantidade}, Valor de venda: {self.valor_venda}, Valor de compra: {self.valor_compra}, Valor do lucro: {self.valor_lucro}, Valor total: {self.valor_total}"

def arq ():
    produtos = []
    with open("produtos.txt", "r") as dados:
        for linha in dados:
            campo = linha.strip().split(",")
            prod = produto(codigo=campo[0], nome=campo[1], categoria=campo[2], quantidade=int(campo[3]), valor_venda=float(campo[4]), valor_compra=float(campo[5]), valor_lucro=float(campo[6]), valor_total=float(campo[7]))
            produtos.append(prod)
    return produtos

def salvar_arq (produtos):
    with open("produtos.txt", "w") as dados:
        for prod in produtos:
            dados.write(f"{prod.codigo},{prod.nome},{prod.categoria},{prod.quantidade},{prod.valor_venda},{prod.valor_compra},{prod.valor_lucro},{prod.valor_total}\n")

def sort_all (produtos):
    return sorted(produtos, key=lambda x: (x.categoria, x.codigo, x.nome, x.quantidade, x.valor_venda, x.valor_compra, x.valor_lucro, x.valor_total))
#-------------------------------------------------------------------------------------------------------------------#


def ver_estoque():
    try:
        produtos = arq()
        print("Produtos no estoque:")
        for prod in produtos:
            print(prod)

    except FileNotFoundError as e:
        print(f"Erro: {e}. O arquivo 'produtos.txt' não foi encontrado.")


def add_estoque():
    add = "s"
    while add == "s" or add == "S":
        try:
            produtos = arq()
            nome = input("Digite o nome do produto: ")
            categoria = input("Digite a categoria do produto: ")
            quantidade = int(input("Digite a quantidade do produto: "))
            valor_venda = float(input("Digite o valor de venda do produto: "))
            valor_compra = float(input("Digite o valor de compra do produto: "))
            codigo = input("Digite o código do produto: ")
            for prod in produtos:
                if prod.nome == nome:
                    print("Produto já existe no estoque.")
                    break
                elif prod.codigo == codigo:
                    print("Código já em uso.")
                    break
            else:
                novo_produto = produto(codigo=codigo, nome=nome, categoria=categoria, quantidade=quantidade, valor_venda=valor_venda, valor_compra=valor_compra, valor_lucro=0, valor_total=0)
                produtos.append(novo_produto)
                produtos = sort_all(produtos)
                salvar_arq(produtos)
                print("Produto adicionado ao estoque.")
            add = input("Deseja adicionar mais produtos ao estoque? (S/N): ")

        except FileNotFoundError as e:
            print(f"Erro: {e}. O arquivo 'produtos.txt' não foi encontrado.")
        except ValueError as e:
            print(f"Erro: {e}. Certifique-se de digitar os valores corretamente.")


def att_estoque ():
    att = "s"
    while att == "s" or att == "S":
        try:
            produtos = arq()
            print("Produtos no estoque:")
            for prod in produtos:
                print(prod)
            codigo = input("Digite o código do produto que deseja atualizar: ")
            for prod in produtos:
                if prod.codigo == codigo:
                    print("Produto encontrado.")
                    nome = input("Digite o nome do produto: ")
                    categoria = input("Digite a nova categoria do produto: ")
                    quantidade = int(input("Digite a nova quantidade do produto: "))
                    valor_venda = float(input("Digite o novo valor de venda do produto: "))
                    valor_compra = float(input("Digite o novo valor de compra do produto: "))
                    codigo = codigo
                    produtos.remove(prod)
                    prod = produto(codigo=codigo, nome=nome, categoria=categoria, quantidade=quantidade, valor_venda=valor_venda, valor_compra=valor_compra, valor_lucro=0, valor_total=0)
                    produtos.append(prod)
                    produtos = sort_all(produtos)
                    salvar_arq(produtos)
                    print("Produto atualizado com sucesso.")
                    att = input("Deseja atualizar outro produto do estoque? (S/N): ")
                    break
            else:
                print("Produto não encontrado.")

        except FileNotFoundError as e:
            print(f"Erro: {e}. O arquivo 'produtos.txt' não foi encontrado.")
        except ValueError as e:
            print(f"Erro: {e}. Certifique-se de digitar os valores corretamente.")


def del_estoque():
    dell = "s"
    while dell == "s" or dell == "S":
        try:
            produtos = arq()
            print("Produtos no estoque:")
            for prod in produtos:
                print(prod)
            codigo = input("Digite o código do produto que deseja deletar: ")
            for prod in produtos:
                if prod.codigo == codigo:
                    produtos.remove(prod)
                    salvar_arq(produtos)
                    print("Produto deletado com sucesso.")
                    break
            else:
                print("Produto não encontrado.")
            dell = input("Deseja tentar deletar outro produto do estoque? (S/N): ")

        except FileNotFoundError as e:
            print(f"Erro: {e}. O arquivo 'produtos.txt' não foi encontrado.")


def vendas ():
    vend = "s"
    while vend == "s" or vend == "S":
        try:
            produtos = arq()
            print("Produtos no estoque:")
            for prod in produtos:
                print(f"Código: {prod.codigo}, Nome: {prod.nome}, Categoria: {prod.categoria}, Quantidade: {prod.quantidade}, Valor de venda: {prod.valor_venda}, Valor de compra: {prod.valor_compra}, Valor do lucro: {prod.valor_lucro}, Valor total: {prod.valor_total}")
            vend = input("Deseja registrar outra venda? (S/N): ")
            codigo = input("Digite o código do produto que foi vendido: ")
            for prod in produtos:
                if prod.codigo == codigo:
                    quantidade_venda = int(input("Digite a quantidade que foi vendida: "))
                    if quantidade_venda > prod.quantidade:
                        print("Quantidade insuficiente em estoque.")
                        break
                    else:
                        if quantidade_venda <= 0:
                            print("Quantidade inválida. A quantidade vendida deve ser maior que zero.")
                            break
                        else:
                            prod.quantidade -= quantidade_venda
                            valor_venda_total = prod.valor_venda * quantidade_venda
                            print(f"Valor total da venda: R${valor_venda_total:.2f}")
                            break
            else:
                print("Produto não encontrado.")
            produtos = sort_all(produtos)
            salvar_arq(produtos)

        except FileNotFoundError as e:
            print(f"Erro: {e}. O arquivo 'produtos.txt' não foi encontrado.")
        except ValueError as e:
            print(f"Erro: {e}. Certifique-se de digitar os valores corretamente.")


def compras ():
    compra = "s"
    while compra == "s" or compra == "S":
        try:
            produtos = arq()
            codigo = input("Digite o código do produto que foi comprado: ")
            print("Produtos no estoque:")
            for prod in produtos:
                print(f"Código: {prod.codigo}, Nome: {prod.nome}, Categoria: {prod.categoria}, Quantidade: {prod.quantidade}, Valor de venda: {prod.valor_venda}, Valor de compra: {prod.valor_compra}, Valor do lucro: {prod.valor_lucro}, Valor total: {prod.valor_total}")
                if prod.codigo == codigo:
                    quantidade_compra = int(input("Digite a quantidade que foi comprada: "))
                    if quantidade_compra <= 0:
                        print("Quantidade inválida. A quantidade comprada deve ser maior que zero.")
                        break
                    else:
                        nova_quantidade = prod.quantidade + quantidade_compra
                        valor_compra_total = float(prod.valor_compra) * quantidade_compra
                        print(f"Valor total da compra: R${valor_compra_total:.2f}")
                        prod.quantidade = nova_quantidade
                        produtos = sort_all(produtos)
                        salvar_arq(produtos)
                        break
            else:
                print("Produto não encontrado.")
            compra = input("Deseja registrar uma compra? (S/N): ")

        except FileNotFoundError as e:
            print(f"Erro: {e}. O arquivo 'produtos.txt' não foi encontrado.")
        except ValueError as e:
            print(f"Erro: {e}. Certifique-se de digitar os valores corretamente.")


def saldo ():
    try:
        produtos = arq()
        soma = 0
        for prod in produtos:
            soma += prod.valor_total
        print(f"Saldo total do estoque: R${soma:.2f}")
        soma21 = {}
        for prod in produtos:
            if prod.categoria not in soma21:
                soma21[prod.categoria] = 0
            soma21[prod.categoria] += prod.valor_total
        for categoria, valor in soma21.items():
            print(f"Saldo do estoque da categoria {categoria}: R${valor:.2f}")

    except FileNotFoundError as e:
        print(f"Erro: {e}. O arquivo 'produtos.txt' não foi encontrado.")
    except ValueError as e:
        print(f"Erro: {e}. Certifique-se de digitar os valores corretamente.")


def sistema ():
    while True:

        print("""
==========================================
            MENU DO ESTOQUE
==========================================

1 - Ver produtos do estoque
2 - Modificar produtos do estoque
3 - Vendas e compras
4 - Sair

[][][][][[][][][][][][][][][][][][][][][][]
        """)

        menu = input("Digite o número da opção desejada: ")
        if menu == "1":
            ver_estoque()
        elif menu == "2":
            while True:

                print("""
==========================================
            MENU DE MODIFICAÇÃO
==========================================

1 - Adicionar produtos ao estoque
2 - Atualizar produtos do estoque
3 - Deletar produtos do estoque
4 - Voltar ao menu principal

[][][][][[][][][][][][][][][][][][][][][][]
                """)

                menu_mod = input("Digite o número da opção desejada: ")
                if menu_mod == "1":
                    add_estoque()
                elif menu_mod == "2":
                    att_estoque()
                elif menu_mod == "3":
                    del_estoque()
                elif menu_mod == "4":
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif menu == "3":

            print("""
==========================================
        MENU DE VENDAS E COMPRAS
==========================================

1 - Registrar venda
2 - Registrar compra
3 - Saldo
4 - Voltar ao menu principal

[][][][][[][][][][][][][][][][][][][][][][]
            """)
 
            menu_vendas = input("Digite o número da opção desejada: ")
            if menu_vendas == "1":
                vendas()
            elif menu_vendas == "2":
                compras()
            elif menu_vendas == "3":
                saldo()
            elif menu_vendas == "4":
                break
                
        elif menu == "4":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")



sistema()