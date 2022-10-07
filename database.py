import psycopg2

CRIA_TABELAS = """
    create table if not exists semestre(
        ano int,
        semestre int,
        check (semestre in (1,2)),
        primary key (ano, semestre)
    );
    create table if not exists disciplina(
        id int primary key,
        nome varchar(30) not null,
        carga_horaria int not null,
        nivel_de_ensino varchar not null check (nivel_de_ensino in ('médio', 'técnico', 'superior')),
        constraint unicidade unique (nome, nivel_de_ensino)
    );

    create table if not exists oferta (
        id serial not null primary key,
        ano int not null,
        id_semestre int not null,
        id_disciplina int not null,
        FOREIGN KEY (ano, id_semestre) REFERENCES semestre (ano, semestre),
        constraint oferta_unica unique(ano, id_semestre, id_disciplina)
    );

"""
INSERT_SEMESTRE = "insert into semestre values (%s, %s);"
INSERT_OFERTA = "insert into oferta values (default, %s, %s, %s)"
SELECT_SEMESTRE = "select * from semestre order by ano, semestre;"
DELETE_SEMESTRE = "delete from semestre where ano = %s and semestre = %s;"
DELETE_OFERTA = "delete from oferta where id = %s;"
UPDATE_SEMESTRE = "update semestre set ano = %s, semestre = %s where (ano = %s and semestre = %s);"
SELECT_DISCIPLINA = "select * from disciplina order by nome;"
SELECT_DISCIPLINA_POR_NOME_E_NIVEL = "select * from disciplina where (nome = %s and nivel_de_ensino = %s);"
SELECT_OFERTA = "select * from oferta join disciplina on(oferta.id_disciplina = disciplina.id) order by ano desc, id_semestre desc, nome asc, nivel_de_ensino asc;"
SELECT_OFERTA_COM_CONDICAO = "select * from oferta where ano = %s and id_semestre = %s and id_disciplina = %s;"


parametros = {
    "host" : "localhost",
    "database" : "bd_cronograma",
    "user" : "postgres",
    "password" : "pgsql" # senha do PGADMIN DE vocêsssss!
}

def conecta_bd():
    try:
        conexao = psycopg2.connect(**parametros)
        print('Conexao com banco de dados realizada com sucesso!')
    except Exception as erro:
        print(f'Erro ao conectar com o banco de dados: {erro}')

    return conexao

def create_tables(conexao):
    try:
        with conexao:
            with conexao.cursor() as cursor:
                cursor.execute(CRIA_TABELAS)
                print("Tabela criada com sucesso!")
    except Exception as erro:
        print(f"Erro ao criar a tabela: {erro}")

def insere_semestre(conexao, ano, semestre):
    try:
        with conexao:
            with conexao.cursor() as cursor:
                cursor.execute(INSERT_SEMESTRE, (ano, semestre))
                print("Semestre inserido com sucesso!")
    except Exception as erro:
        print(f"Erro ao inserir o semestre: {erro}")

def insere_oferta(conexao, ano, semestre, disciplina):  
    try:
        with conexao:
            with conexao.cursor() as cursor:
                linhas = None
                erro = None
                cursor.execute(INSERT_OFERTA, (ano, semestre, disciplina))
                linhas = cursor.rowcount
                print("Oferta cadastrada com sucesso!")
    except psycopg2.IntegrityError:
        erro = 1
        print(f"Chave primaria duplicada")
    except Exception as e:
        erro = 2
        print(f" Erro ao inserir a oferta!", e)
    return linhas, erro

def lista_semestres(conexao):
    try:
        with conexao:
            with conexao.cursor() as cursor:
                cursor.execute(SELECT_SEMESTRE)
                return cursor.fetchall()
    except Exception as erro:
        print(f"Erro ao consultar os semestres: {erro}")

def lista_disciplinas(conexao):
    try:
        with conexao:
            with conexao.cursor() as cursor:
                cursor.execute(SELECT_DISCIPLINA)
                return cursor.fetchall()
    except Exception as erro:
        print(f"Erro ao consultar as disciplinas: {erro}")

def consulta_disciplina_por_nome_e_nivel(conexao, nome, nivel):
    try:
        with conexao:
            with conexao.cursor() as cursor:
                cursor.execute(SELECT_DISCIPLINA_POR_NOME_E_NIVEL,(nome, nivel))
                return cursor.fetchall()
    except Exception as erro:
        print(f"Erro ao consultar a disciplina por nome: {erro}")

def lista_ofertas(conexao):
    try:
        with conexao:
            with conexao.cursor() as cursor:
                cursor.execute(SELECT_OFERTA)
                return cursor.fetchall()
    except Exception as erro:
        print(f"Erro ao consultar as ofertas: {erro}")

def consulta_oferta_com_condicao(conexao, ano, semestre, disciplina):
    try:
        with conexao:
            with conexao.cursor() as cursor:
                cursor.execute(SELECT_OFERTA_COM_CONDICAO, (ano, semestre, disciplina))
                return cursor.fetchall()
    except Exception as erro:
        print(f"Erro ao consultar a oferta: {erro}")

def delete_semestre(conexao, ano, semestre):
    try:
        with conexao:
            with conexao.cursor() as cursor:
                cursor.execute(DELETE_SEMESTRE,(ano,semestre))
                print(f"Semestre: {ano}.{semestre} excluido com sucesso!")
    except Exception as erro:
        print(f"Erro ao excluir o semestre: {erro}")

def delete_oferta(conexao, id_oferta):
    try:
        with conexao:
            with conexao.cursor() as cursor:
                cursor.execute(DELETE_OFERTA,(id_oferta,))
                print(f"Oferta excluida com sucesso!")
    except Exception as erro:
        print(f"Erro ao excluir a oferta: {erro}")

def update_semestre(conexao, novo_ano, novo_semestre, ano, semestre):
    try:
        with conexao:
            with conexao.cursor() as cursor:
                cursor.execute(UPDATE_SEMESTRE, (novo_ano, novo_semestre, ano, semestre))
                print("Semestre alterado com sucesso!")
    except Exception as erro:
        print(f"Erro ao alterar o semestre: {erro}")
