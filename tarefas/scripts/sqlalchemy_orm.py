from sqlalchemy import create_engine, MetaData, Table

# Configurações de conexão
dbname = "AtividadeBD"
user = "japagabriel"
password = "2403"
host = "172.17.0.2"
port = "5432"

# Criação da engine de conexão
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')

# Refletir o esquema
metadata = MetaData()
metadata.reflect(bind=engine)

tabela_projeto = Table('projeto', metadata, autoload_with=engine)
tabela_atividade = Table('atividade', metadata, autoload_with=engine)

# Inserir uma atividade em algum projeto
stmt_insert_atividade = tabela_atividade.insert().values(descricao='BD - Atividade 4', projeto=3, data_inicio='2024-03-20', data_fim='2024-04-01')

# Atualizar o líder de algum projeto
stmt_update_projeto = tabela_projeto.update().\
    where(tabela_projeto.c.codigo == 3).\
    values(responsavel=1)

# Executar as operações
with engine.connect() as connection:
    connection.execute(stmt_insert_atividade)
    connection.execute(stmt_update_projeto)

    # Listar todos os projetos e suas atividades
    result_projeto = connection.execute(tabela_projeto.select())
    print("Projetos:")
    for row in result_projeto:
        print(row)

    result_atividade = connection.execute(tabela_atividade.select())
    print("\nAtividades:")
    for row in result_atividade:
        print(row)
