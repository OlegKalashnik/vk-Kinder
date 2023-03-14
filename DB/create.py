from DB.connect import connection


def create_table_users(connection):
    value = """CREATE TABLE IF NOT EXISTS users (
                 bd_id serial PRIMARY KEY,
                 id INTEGER NULL
             );"""
    connection.execute(value)


def create_table_search_params(connection):
    value = """CREATE TABLE IF NOT EXISTS search_params (
                 bd_id serial PRIMARY KEY,
                 param_sex INTEGER NULL,
                 param_city INTEGER NULL,
                 param_age_at INTEGER NULL,
                 param_age_to INTEGER NULL,
                 param_status INTEGER NULL,
                 id_user integer not null,
                 FOREIGN KEY (id_user) REFERENCES users (bd_id) ON DELETE CASCADE
             );"""
    connection.execute(value)


def create_table_favorites_users(connection):
    value = """CREATE TABLE IF NOT EXISTS favorites_users (
                 fav_user_id integer references users(bd_id),
                 id_user integer references users(bd_id),
                 constraint favorites_users_id primary key (fav_user_id, id_user)
             );"""
    connection.execute(value)


def create_table_black_list(connection):
    value = """CREATE TABLE IF NOT EXISTS black_list (
                 bl_list_id integer references users(bd_id),
                 id_user integer references users(bd_id),
                 constraint black_list_id primary key (bl_list_id, id_user)
             );"""
    connection.execute(value)


def create_all_tables(connection):
    create_table_users(connection)
    create_table_search_params(connection)
    create_table_favorites_users(connection)
    create_table_black_list(connection)


def creat_all_tables():
    conn = connection()
    create_all_tables(conn)
    conn.close()
