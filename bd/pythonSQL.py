import psycopg2

def catchRowbyID(table, id):
    conn = psycopg2.connect(database="teste", user="postgres", password="admin", host="localhost", port="5432") # Estabelecendo conexão com o banco de dados PostgreSQL
    cursor = conn.cursor() # Cria um cursor para executar consultas SQL
    cursor.execute(f"SELECT * FROM {table} order by id asc;") # Executa uma consulta SQL para selecionar todas as linhas da tabela desejada
    row_selected = None # Declarando a variável
    for row in cursor: # para cada linha da tabela
        if int(row[0]) == int(id): # compara se o id é compatível
            row_selected = row # Retorna a linha desejada
            
    cursor.close() # Fecha o cursor
    conn.close() # Fecha a conexão com o banco de dados
    return row_selected # Retorna a linha selecionada

def catchAllbyID(id, tables): # Recebe o id e uma lista de tabelas como parâmetro
    row = [] # Declara a lista à ser retornada
    for table in tables: # para cada tabela na lista das tabelas
        row.append(catchRowbyID(table, id)[1::]) # Acrescenta todas as colunas referentes ao mesmo id da tabela
    return row # Retorna todas as colunas de todas as tabelas que possuem um id correspondente
        

# print(catchRowbyID(input("Insira uma tabela válida: "), input("Insira um id válido: ")))

# print(catchAllbyID(102, ["coordenadas", "meses"]))