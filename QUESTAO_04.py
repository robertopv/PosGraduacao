import os

# Inicializa um dicionário para armazenar as peças cadastradas
pecas = {}

# Função para cadastrar uma nova peça
def cadastrar_peca():
    codigo = input("Digite o código da peça: ")
    nome = input("Digite o nome da peça: ")
    fabricante = input("Digite o fabricante da peça: ")
    preco = float(input("Digite o preço da peça: "))
    pecas[codigo] = {'nome': nome, 'fabricante': fabricante, 'preco': preco}
    print("Peça cadastrada com sucesso!")

# Função para consultar todas as peças cadastradas
def consultar_todas_pecas():
    print("Lista de todas as peças cadastradas:")
    for codigo, peca in pecas.items():
        print("Código:", codigo)
        print("Nome:", peca['nome'])
        print("Fabricante:", peca['fabricante'])
        print("Preço:", peca['preco'])
        print("------------------------")

# Função para consultar uma peça por código
def consultar_peca_por_codigo():
    codigo = input("Digite o código da peça: ")
    if codigo in pecas:
        peca = pecas[codigo]
        print("------------------------")
        print("Código:", codigo)
        print("Nome:", peca['nome'])
        print("Fabricante:", peca['fabricante'])
        print("Preço:", peca['preco'])
        print("------------------------")
    else:
        print("Peça não encontrada.")

# Função para consultar peças por fabricante
def consultar_peca_por_fabricante():
    fabricante = input("Digite o nome do fabricante: ")
    encontrou = False
    for codigo, peca in pecas.items():
        if peca['fabricante'] == fabricante:
            print(" ")
            print("Código:", codigo)
            print("Nome:", peca['nome'])
            print("Preço:", peca['preco'])
            print("------------------------")
            encontrou = True
    if not encontrou:
        print("Não foram encontradas peças desse fabricante.")

# Função para remover uma peça
def remover_peca():
    codigo = input("Digite o código da peça que deseja remover: ")
    if codigo in pecas:
        del pecas[codigo]
        print("Peça removida com sucesso!")
    else:
        print("Peça não encontrada.")

# Loop principal do programa
flg_Printanome = 0
while True:
    os.system('cls')
    if flg_Printanome == 0:
        print("Bem vindo ao controle de estoque da Bicicletaria do Roberto Pereira do Vale")
        print("-------------------------------------------------------------------------- ")
        flg_Printanome = 137

    print("===== MENU =====")
    print("1. Cadastrar Peça")
    print("2. Consultar Peça")
    print("3. Remover Peça")
    print("4. Sair")
    opcao_menu = input("Digite a opção desejada: ")

    if opcao_menu == "1":
        cadastrar_peca()

    elif opcao_menu == "2":
        while True:
            os.system('cls')
            print("===== CONSULTAR PEÇA =====")
            print("1. Consultar Todas as Peças")
            print("2. Consulta Peças por Código")
            print("3. Consulta Peças por Fabricante")
            print("4. Retornar")
            opcao_consulta = input("Digite a opção desejada:")
            if opcao_consulta == "1":
                consultar_todas_pecas()
            elif opcao_consulta == "2":
                consultar_peca_por_codigo()
            elif opcao_consulta == "3":
                consultar_peca_por_fabricante()
            elif opcao_consulta == "4":
                break
            else:
                print("Opção inválida.")

    elif opcao_menu == "3":
        remover_peca()

    elif opcao_menu == "4":
        print("Encerrando programa...")
        break

    else:
        print("Opção inválida.")