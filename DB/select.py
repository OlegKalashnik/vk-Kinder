# Выбор id в БД по id пользователя vk
def select_nalichie_users_DB(connection, id_vk):
    table = 'users'
    column1 = 'bd_id'
    column2 = 'id'
    value = f"SELECT {column1}, {column2} FROM {table} WHERE {column2} = ?;"
    data = connection.execute(value, (id_vk,)).fetchall()
    return data

# Проверка наличия в ЧС
def select_nalichie_users_v_blaklist(connection, bd_id):
    table = 'black_list'
    column2 = 'bl_list_id'
    value = f"SELECT {column2} FROM {table} WHERE {column2} = ?;"
    data = connection.execute(value, (bd_id,)).fetchall()
    return data

# Проверка наличия в избранных
def select_nalichie_users_v_favorites(connection, bd_id):
    table = 'favorites_users'
    column2 = 'fav_user_id'
    value = f"SELECT {column2} FROM {table} WHERE {column2} = ?;"
    data = connection.execute(value, (bd_id,)).fetchall()
    return data

# Выбор id БД для просмотра
def select_search_params(connection, sex, age_at, age_to, city, status):
    table1 = 'search_params'
    column1 = 'param_sex'
    column2 = 'param_city'
    column3 = 'param_age_at'
    column4 = 'param_age_to'
    column5 = 'param_status'
    column6 = 'id_user'
    value = f"SELECT {column6} FROM {table1} WHERE {column1} = ? AND {column2} = ? AND {column3} = ? AND {column4} = ? AND {column5} = ?;"
    data = connection.execute(value, (sex, city, age_at, age_to, status)).fetchall()
    users_for_view = {}
    n = 1
    for exec in data:
        black_list = select_nalichie_users_v_blaklist(connection, exec[0])
        favorites = select_nalichie_users_v_favorites(connection, exec[0])
        if not black_list and not favorites:
            users_for_view[n] = exec[0]
            n += 1
    return users_for_view

# Выборка одного аккаунта для просмотра
def select_one_user_for_view(connection, bd_id):
