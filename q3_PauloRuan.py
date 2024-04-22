import mysql.connector

# Conexão com o banco de dados
database_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NBHL84ownD6ihT",
    database="GeekStore"
)

database_cursor = database_connection.cursor()

# Função para criar banco de dados
create_database = lambda : database_cursor.execute("CREATE DATABASE IF NOT EXISTS GeekStore")

# Função para criar tabela de usuários
create_table_users = lambda : database_cursor.execute(
    "CREATE TABLE IF NOT EXISTS USERS ("
    "id INT AUTO_INCREMENT PRIMARY KEY, "
    "name VARCHAR(255), "
    "country VARCHAR(255), "
    "id_console INT)"
)

# Função para criar tabela de consoles
create_table_consoles = lambda : database_cursor.execute(
    "CREATE TABLE IF NOT EXISTS CONSOLES ("
    "id_console INT AUTO_INCREMENT PRIMARY KEY, "
    "name VARCHAR(255), "
    "id_company INT, "
    "release_date DATE)"
)

# Função para criar tabela de jogos
create_table_games = lambda : database_cursor.execute(
    "CREATE TABLE IF NOT EXISTS GAMES ("
    "id_game INT AUTO_INCREMENT PRIMARY KEY, "
    "title VARCHAR(255), "
    "genre VARCHAR(255), "
    "release_date DATE, "
    "id_console INT)"
)

# Função para criar tabela de empresas
create_table_companies = lambda : database_cursor.execute(
    "CREATE TABLE IF NOT EXISTS COMPANIES ("
    "id_company INT AUTO_INCREMENT PRIMARY KEY, "
    "name VARCHAR(255), "
    "country VARCHAR(255))"
)

# Função para criar todas as tabelas
create_all_tables = lambda : [
    function()
    for function in (create_database, create_table_users, create_table_consoles, create_table_games, create_table_companies)
]
create_all_tables()

# Funções para inserção de dados
insert_user = lambda user_data: (
    database_cursor.execute("INSERT INTO USERS (name, country, id_console) VALUES (%s, %s, %s)", (user_data[0], user_data[1], user_data[2])), 
    database_connection.commit()
)
insert_console = lambda console_data: (
    database_cursor.execute("INSERT INTO CONSOLES (name, id_company, release_date) VALUES (%s, %s, %s)", (console_data[0], console_data[1], console_data[2])),
    database_connection.commit()
)
insert_game = lambda game_data: (
    database_cursor.execute("INSERT INTO GAMES (title, genre, release_date, id_console) VALUES (%s, %s, %s, %s)", (game_data[0], game_data[1], game_data[2], game_data[3])), 
    database_connection.commit()
)
insert_company = lambda company_data: (
    database_cursor.execute("INSERT INTO COMPANIES (name, country) VALUES (%s, %s)", (company_data[0], company_data[1])), 
    database_connection.commit()
)

# Funções para seleção de dados
select_all_users = lambda: (
    database_cursor.execute("SELECT * FROM USERS"),
    [print(row) for row in database_cursor.fetchall()]
)

select_user_by_id = lambda user_id: (
    database_cursor.execute("SELECT * FROM USERS WHERE id = %s", (user_id,)),
    [print(row) for row in database_cursor.fetchall()]
)

select_all_consoles = lambda: (
    database_cursor.execute("SELECT * FROM CONSOLES"),
    [print(row) for row in database_cursor.fetchall()]
)

select_console_by_id = lambda console_id: (
    database_cursor.execute("SELECT * FROM CONSOLES WHERE id_console = %s", (console_id,)),
    [print(row) for row in database_cursor.fetchall()]
)

select_all_games = lambda : (
    database_cursor.execute("SELECT * FROM GAMES"),
    [print(row) for row in database_cursor.fetchall()]        
) 

select_game_by_id = lambda game_id: (
    database_cursor.execute("SELECT * FROM GAMES WHERE id_game = %s", (game_id,)),
    [print(row) for row in database_cursor.fetchall()]
)

select_all_companies = lambda : (
    database_cursor.execute("SELECT * FROM COMPANIES"),
    [print(row) for row in database_cursor.fetchall()]
)

select_company_by_id = lambda company_id: (
    database_cursor.execute("SELECT * FROM COMPANIES WHERE id_company = %s", (company_id,)),
    [print(row) for row in database_cursor.fetchall()]
)

# Funções para atualização de dados
update_user = lambda user_data: (
    database_cursor.execute("UPDATE USERS SET name = %s, country = %s, id_console = %s WHERE id = %s", (user_data[0], user_data[1], user_data[2], user_data[3])),
    database_connection.commit()
)

update_console = lambda console_data: (
    database_cursor.execute("UPDATE CONSOLES SET name = %s, id_company = %s, release_date = %s WHERE id_console = %s", (console_data[0], console_data[1], console_data[2], console_data[3])),
    database_connection.commit()
) 

update_game = lambda game_data: (
    database_cursor.execute("UPDATE GAMES SET title = %s, genre = %s, release_date = %s, id_console = %s WHERE id_game = %s", (game_data[0], game_data[1], game_data[2], game_data[3], game_data[4])),
    database_connection.commit()
)

update_company = lambda company_data: (
    database_cursor.execute("UPDATE COMPANIES SET name = %s, country = %s WHERE id_company = %s", (company_data[0], company_data[1], company_data[2])),
    database_connection.commit()
)

# Funções para deletar dados
delete_user = lambda user_id: (
    database_cursor.execute("DELETE FROM USERS WHERE id = %s", (user_id,)),
    database_connection.commit()
)

delete_console = lambda console_id: (
    database_cursor.execute("DELETE FROM CONSOLES WHERE id_console = %s", (console_id,)),
    database_connection.commit()
)

delete_game = lambda game_id: (
    database_cursor.execute("DELETE FROM GAMES WHERE id_game = %s", (game_id,)),
    database_connection.commit()
) 

delete_company = lambda company_id: (
    database_cursor.execute("DELETE FROM COMPANIES WHERE id_company = %s", (company_id,)),
    database_connection.commit()
) 
