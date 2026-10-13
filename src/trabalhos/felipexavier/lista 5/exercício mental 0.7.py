class produtos ():
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

            

def ver_estoque():
    try:
        with open("produtos.txt", "r") as dados:
            print("Produtos no estoque:")
            for linha in dados:
                campo = linha.strip().split(",")
                print(f"Código: {campo[0]}, Nome: {campo[1]}, Categoria: {campo[2]}, Quantidade: {campo[3]}, Valor de venda: {campo[4]}, Valor de compra: {campo[5]}, Valor do lucro: {campo[6]}, Valor total: {campo[7]}")
    except FileNotFoundError as e:
        print(f"Erro: {e}. O arquivo 'produtos.txt' não foi encontrado.")


def add_estoque():
    add = input("Deseja adicionar mais produtos ao estoque? (S/N): ")
    while add == "s" or add == "S":
        try:
            with open("produtos.txt", "r") as dados, open("produtos.txt", "a") as dados_att:
                nome = input("Digite o nome do produto: ")
                categoria = input("Digite a categoria do produto: ")
                quantidade = int(input("Digite a quantidade do produto: "))
                valor_venda = float(input("Digite o valor de venda do produto: "))
                codigo = input("Digite o código do produto: ")
                valor_compra = float(input("Digite o valor de compra do produto: "))
                valor_lucro = valor_venda - valor_compra
                valor_total = valor_venda * quantidade
                for linha in dados:
                    if nome in linha:
                        print("Produto já existe no estoque.")
                        break
                else:
                    dados_att.write(f"{codigo},{nome},{categoria},{quantidade},{valor_venda},{valor_compra},{valor_lucro},{valor_total}\n")
                add = input("Deseja adicionar mais produtos ao estoque? (S/N): ")
        except FileNotFoundError as e:
            print(f"Erro: {e}. O arquivo 'produtos.txt' não foi encontrado.")
        except ValueError as e:
            print(f"Erro: {e}. Certifique-se de digitar os valores corretamente.")


def att_estoque ():
    att = input("Deseja atualizar o estoque? (S/N): ")
    while att == "s" or att == "S":
        try:
            with open("produtos.txt", "r") as dados, open("produtos_att.txt", "w") as dados_att:
                print("Produtos no estoque:")
                for linha in dados:
                    campo = linha.strip().split(",")
                    print(f"Código: {campo[0]}, Nome: {campo[1]}, Categoria: {campo[2]}, Quantidade: {campo[3]}, Valor de venda: {campo[4]}, Valor de compra: {campo[5]}, Valor do lucro: {campo[6]}, Valor total: {campo[7]}")
                codigo = input("Digite o código do produto que deseja atualizar: ")
                for linha in dados:
                    print(linha)
                    campo = linha.strip().split(",")
                    if campo[0] == codigo:
                        print("Produto encontrado.")
                        nome = input("Digite o nome do produto: ")
                        categoria = input("Digite a nova categoria do produto: ")
                        quantidade = int(input("Digite a nova quantidade do produto: "))
                        valor_venda = float(input("Digite o novo valor de venda do produto: "))
                        valor_compra = float(input("Digite o novo valor de compra do produto: "))
                        valor_lucro = valor_venda - valor_compra
                        valor_total = valor_venda * quantidade
                        dados_att.write(f"{codigo},{nome},{categoria},{quantidade},{valor_venda},{valor_compra},{valor_lucro},{valor_total}\n")
                    else:
                        dados_att.write(linha)
                with open("produtos.txt", "w") as dados, open("produtos_att.txt", "r") as dados_att:
                    for linha in dados_att:
                        dados.write(linha)
        except FileNotFoundError as e:
            print(f"Erro: {e}. O arquivo 'produtos.txt' não foi encontrado.")
        except ValueError as e:
            print(f"Erro: {e}. Certifique-se de digitar os valores corretamente.")


def del_estoque():
    dell = input("Deseja deletar algum produto do estoque? (S/N): ")
    while dell == "s" or dell == "S":
        try:
            with open("produtos.txt", "r") as dados, open("produtos_att.txt", "w") as dados_att:
                print("Produtos no estoque:")
                for linha in dados:
                    campo = linha.strip().split(",")
                    print(f"Código: {campo[0]}, Nome: {campo[1]}, Categoria: {campo[2]}, Quantidade: {campo[3]}, Valor de venda: {campo[4]}, Valor de compra: {campo[5]}, Valor do lucro: {campo[6]}, Valor total: {campo[7]}")
                codigo = input("Digite o código do produto que deseja deletar: ")
                find = False
                for linha in dados:
                    print(linha)
                    campo = linha.strip().split(",")
                    if campo[0] == codigo:
                        find = True
                    if codigo not in linha:
                        dados_att.write(linha)
                    dell = input("Deseja deletar outro produto do estoque? (S/N): ")
                if find == False:
                    print("Produto não encontrado.")
                    dell = input("Deseja tentar deletar outro produto do estoque? (S/N): ")


            with open("produtos.txt", "w") as dados, open("produtos_att.txt", "r") as dados_att:
                for linha in dados_att:
                    dados.write(linha)
        except FileNotFoundError as e:
            print(f"Erro: {e}. O arquivo 'produtos.txt' não foi encontrado.")


def vendas ():
    while True:
        try:
            with open("produtos.txt", "r") as dados, open("produtos_att.txt", "w") as dados_att:
                print("Produtos no estoque:")
                for linha in dados:
                    campo = linha.strip().split(",")
                    print(f"Código: {campo[0]}, Nome: {campo[1]}, Categoria: {campo[2]}, Quantidade: {campo[3]}, Valor de venda: {campo[4]}, Valor de compra: {campo[5]}, Valor do lucro: {campo[6]}, Valor total: {campo[7]}")
                codigo = input("Digite o código do produto que foi vendido: ")
                for linha in dados:
                    campo = linha.strip().split(",")
                    if campo[0] == codigo:
                        quantidade_venda = int(input("Digite a quantidade que foi vendida: "))
                        if quantidade_venda > int(campo[3]):
                            print("Quantidade insuficiente em estoque.")
                            break
                        else:
                            nova_quantidade = int(campo[3]) - quantidade_venda
                            valor_total = float(campo[4]) * quantidade_venda
                            dados_att.write(f"{campo[0]},{campo[1]},{campo[2]},{nova_quantidade},{campo[4]},{campo[5]},{campo[6]},{valor_total}\n")
                            valor_venda_total = float(campo[4]) * quantidade_venda
                            print(f"Valor total da venda: R${valor_venda_total:.2f}")
                    else:
                        dados_att.write(linha)
            with open("produtos.txt", "w") as dados, open("produtos_att.txt", "r") as dados_att:
                for linha in dados_att:
                    dados.write(linha)
        except FileNotFoundError as e:
            print(f"Erro: {e}. O arquivo 'produtos.txt' não foi encontrado.")
        except ValueError as e:
            print(f"Erro: {e}. Certifique-se de digitar os valores corretamente.")


def compras ():
    while True:
        try:
            with open("produtos.txt", "r") as dados, open("produtos_att.txt", "w") as dados_att:
                print("Produtos no estoque:")
                for linha in dados:
                    campo = linha.strip().split(",")
                    print(f"Código: {campo[0]}, Nome: {campo[1]}, Categoria: {campo[2]}, Quantidade: {campo[3]}, Valor de venda: {campo[4]}, Valor de compra: {campo[5]}, Valor do lucro: {campo[6]}, Valor total: {campo[7]}")
                    if campo[0] == codigo:
                        quantidade_compra = int(input("Digite a quantidade que foi comprada: "))
                        nova_quantidade = int(campo[3]) + quantidade_compra
                        valor_total = float(campo[4]) * nova_quantidade
                        dados_att.write(f"{campo[0]},{campo[1]},{campo[2]},{nova_quantidade},{campo[4]},{campo[5]},{campo[6]},{valor_total}\n")
                        valor_compra_total = float(campo[5]) * quantidade_compra
                        print(f"Valor total da compra: R${valor_compra_total:.2f}")
                    else:
                        dados_att.write(linha)
            with open("produtos.txt", "w") as dados, open("produtos_att.txt", "r") as dados_att:
                for linha in dados_att:
                    dados.write(linha)
        except FileNotFoundError as e:
            print(f"Erro: {e}. O arquivo 'produtos.txt' não foi encontrado.")
        except ValueError as e:
            print(f"Erro: {e}. Certifique-se de digitar os valores corretamente.")


def saldo ():
    try:
        with open("produtos.txt", "r") as dados:
            saldo_total = 0
            pesquisa = input("Deseja pesquisar por código ou categoria? (S/N): ")
            if pesquisa == "codigo" or pesquisa == "Código" or pesquisa == "CÓDIGO":
                codigo = input("Digite o código do produto: ")
                for linha in dados:
                    campo = lina.strip().split(",")
                    if campo[0] == codigo:
                        saldo_total += float(campo[7])
            elif pesquisa == "categoria" or pesquisa == "Categoria" or pesquisa == "CATEGORIA":
                categoria = input("Digite a categoria do produto: ")
                for linha in dados:
                    campo = linha.strip().split(",")
                    if campo[2] == categoria:
                        saldo_total += float(campo[7])
            else:
                for linha in dados:
                    campo = linha.strip().split(",")
                    saldo_total += float(campo[7])
                print(f"Saldo total do estoque: R${saldo_total:.2f}")
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

        menu = input("Escolha uma opção: ")
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

                menu_mod = input("Escolha uma opção: ")
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
 
            menu_vendas = input("Escolha uma opção: ")
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