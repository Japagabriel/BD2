from sqlalchemy import create_engine, MetaData, Table

dbname = "atividades_BD2_ORM"
user = "japagabriel"
password = "2403"
host = "172.17.0.2"
port = "5432"

engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')

metadata = MetaData()
metadata.reflect(bind=engine)

tabela_projeto = Table('projeto', metadata, autoload_with=engine)
tabela_atividade = Table('atividade', metadata, autoload_with=engine)

#Inserir uma atividade em algum projeto;

stmt1 = tabela_atividade.insert().values(descricao='BD - Atividade 4', projeto=3, data_inicio='2024-03-20', data_fim='2024-04-01')

#Atualizar o líder de algum projeto;

stmt2 = tabela_projeto.update().\
            where(tabela_projeto.c.codigo == 3).\
            values(responsavel=1)

with engine.connect() as connection:
    result = connection.execute(stmt1)

    result = connection.execute(stmt2)

    result = connection.execute(tabela_projeto.select())
    for row in result:
        print(row)

    result = connection.execute(tabela_atividade.select())
    for row in result:
        print(row)