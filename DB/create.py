from DB.connect import connection

def create_table_users(connection):
    value = """CREATE TABLE IF NOT EXISTS users (
                                 bd_id serial PRIMARY KEY,
                                 id INTEGER NULL,
                                 first_name varchar(30) NOT NULL,
                                 last_name varchar(30) NOT NULL,
                                 city_id INTEGER NULL,
                                 city_title varchar(50) NULL,
                                 link_pro varchar(50) NOT NULL,
                                 verified INTEGER NULL,
                                 sex INTEGER NULL,
                                 bdate varchar(30) NULL,
                                 home_town varchar(50) NULL,
                                 has_photo INTEGER NULL,
                                 online INTEGER NULL,
                                 domain varchar(50) NOT NULL,
                                 nickname varchar(50) NULL,
                                 screen_name varchar(50) NULL,
                                 maiden_name varchar(50) NULL,
                                 friend_status INTEGER NULL,
                                 can_access_closed BOOLEAN,
                                 is_closed BOOLEAN,
                                 photo_1_id INTEGER NULL,
                                 photo_1_likes INTEGER NULL,
                                 photo_1_url varchar(300) NULL,
                                 photo_2_id INTEGER NULL,
                                 photo_2_likes INTEGER NULL,
                                 photo_2_url varchar(300) NULL,
                                 photo_3_id INTEGER NULL,
                                 photo_3_likes INTEGER NULL,
                                 photo_3_url varchar(300) NULL,
                                 track_code varchar(100) NULL,
                                 online_app INTEGER NULL,
                                 online_mobile INTEGER NULL
                                 );
                                 """
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
                                 );
                                 """
    connection.execute(value)

def create_table_favorites_users(connection):
    value = """CREATE TABLE IF NOT EXISTS favorites_users (
                                 fav_user_id integer references users(bd_id),
                                 id_user integer references users(bd_id),
                                 constraint favorites_users_id primary key (fav_user_id, id_user)
                                 );
                                 """
    connection.execute(value)

def create_table_black_list(connection):
    value = """CREATE TABLE IF NOT EXISTS black_list (
                                 bl_list_id integer references users(bd_id),
                                 id_user integer references users(bd_id),
                                 constraint black_list_id primary key (bl_list_id, id_user)
                                 );
                                 """
    connection.execute(value)

def creat_all_tables(connection):
    create_table_users(connection)
    create_table_search_params(connection)
    create_table_favorites_users(connection)
    create_table_black_list(connection)
