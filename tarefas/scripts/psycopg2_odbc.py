import psycopg2

# Conexão com o banco de dados
conn = psycopg2.connect(
    dbname="AtividadesBD",
    user="japagabriel",
    password="2403",
    host="172.17.0.2",
    port="5432"
)

cur = conn.cursor()

# Inserir uma atividade em algum projeto
sql_insert_atividade = "INSERT INTO atividade (descricao, projeto, data_inicio, data_fim) VALUES (%s, %s, %s, %s)"
val_insert_atividade = ("ES - Atividade 3", 4, "2024-05-17", "2024-12-05")
cur.execute(sql_insert_atividade, val_insert_atividade)

# Atualizar o líder de algum projeto
sql_update_projeto = "UPDATE projeto SET responsavel = %s WHERE codigo = %s"
val_update_projeto = (4, 3)
cur.execute(sql_update_projeto, val_update_projeto)

# Listar todos os projetos e suas atividades
cur.execute("SELECT * FROM projeto ORDER BY codigo")
projetos = cur.fetchall()
print("Projetos:")
for projeto in projetos:
    print(projeto)

cur.execute("SELECT * FROM atividade ORDER BY codigo")
atividades = cur.fetchall()
print("\nAtividades:")
for atividade in atividades:
    print(atividade)

# Fechar a conexão
cur.close()
conn.close()
