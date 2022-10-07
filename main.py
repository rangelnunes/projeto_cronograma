import database as db

conexao = db.conecta_bd()
db.create_tables(conexao)

MENU_DE_OPCOES = """ ##### MENU #####

1) Inresir um novo semestre
2) Consultar semestres cadastrados
3) Excluir um semestre
4) Alterar um semestre
5) Sair.

Digite a opcao desejada: """

def cadastra_semestre(conexao):
    ano = input("Digite o ano: ")
    semestre = input("Digite o semestre (1 ou 2): ")
    print("ano", ano, "semestre", semestre)
    # chamar o metodo do database.py
    db.insere_semestre(conexao, ano, semestre)

def consulta_semestres(conexao):
    semestres = db.lista_semestres(conexao)

    for semestre in semestres:
        print(f"Semestre: {semestre[0]}.{semestre[1]}")
        print("----------\n")

def excluir_semestre(conexao):
    ano = input("Digite o ano que deseja excluir: ")
    semestre = input("Digite o semestre que deseja excluir: ")

    db.delete_semestre(conexao, ano, semestre)

def alterar_semestre(conexao):
    ano = input("Digite o ano que deseja alterar: ")
    semestre = input("Digite o semestre que deseja alterar: ")

    novo_ano = input("Digite o novo valor para o ano: ")
    novo_semestre = input("Digite o novo valor para o semestre: ")

    db.update_semestre(conexao, novo_ano, novo_semestre, ano, semestre)

while (opcao := input(MENU_DE_OPCOES)) != '5':
    try:
        print(f"Opcao selecionada: {opcao}")
        if opcao == '1':
            cadastra_semestre(conexao)
        elif opcao == '2':
            consulta_semestres(conexao)
        elif opcao == '3':
            excluir_semestre(conexao)
        elif opcao == '4':
            alterar_semestre(conexao)
    except KeyError:
        print("Opção invalida! Tente novamente.")