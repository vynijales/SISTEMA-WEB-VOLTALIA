import psycopg2

# Estabelecendo conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(database="teste", user="postgres", password="admin", host="localhost", port="5432")

# Cria um cursor para executar consultas SQL
cursor = conn.cursor()

# Executa uma consulta SQL para selecionar todas as linhas da tabela desejada
cursor.execute("SELECT * FROM coordenadas;")

# Imprimindo as linhas da tabela
for row in cursor:
    print(row)

# Fecha o cursor e a conexão com o banco de dados
cursor.close()
conn.close()
