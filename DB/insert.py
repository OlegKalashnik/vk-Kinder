from DB.select import select_nalichie_users_DB


def add_users(connection, users_dict):
    for key in users_dict.keys():
        data = select_nalichie_users_DB(connection, key)
        if data == []:
            value = '''insert into users('''
            columns = ''''''
            values = ''''''
            for key2 in users_dict[key].keys():
                if type(users_dict[key][key2]) == str:
                    if "'" in users_dict[key][key2]:
                        users_dict[key][key2] = users_dict[key][key2].replace("'",'"')
                columns += f'''"{key2}",'''
                values += f"""'{users_dict[key][key2]}',"""
            columns = columns[:-1]
            values = values[:-1]
            value = value + columns + ') values (' + values + ');'
            connection.execute(value)
            print('Пользователь добавлен в БД')
        else:
            print('Пользователь уже есть в БД')

def add_users_and_search_params(connection, users_dict, sex, age_from, age_to, city, status):
    for key in users_dict.keys():
        data = select_nalichie_users_DB(connection, key)
        if data == []:
            value = '''insert into users('''
            columns = ''''''
            values = ''''''
            for key2 in users_dict[key].keys():
                if type(users_dict[key][key2]) == str:
                    if "'" in users_dict[key][key2]:
                        users_dict[key][key2] = users_dict[key][key2].replace("'",'"')
                columns += f'''"{key2}",'''
                values += f"""'{users_dict[key][key2]}',"""
            columns = columns[:-1]
            values = values[:-1]
            value = value + columns + ') values (' + values + ') RETURNING bd_id;'
            n = connection.execute(value).fetchone()
            add_search_params(connection, n[0], sex, age_from, age_to, city, status)
            print('Пользователь добавлен в БД')
        else:
            print('Пользователь уже есть в БД')

def add_search_params(connection, bd_id, sex, age_from, age_to, city, status):
    value = '''INSERT INTO search_params("param_sex", "param_age_from", "param_age_to", "param_city", "param_status", "bd_id") VALUES '''
    values = f'''('{sex}', {age_from}, {age_to}, '{city}', '{status}', {bd_id})'''
    query = value + values
    connection.execute(query)
    print('Параметры поиска добавлены в БД')

def add_favorites_users(connection, user_id, id_in_list):
    value = f"INSERT INTO favorites_users (user_id, favorite_id) VALUES ({user_id}, {id_in_list});"
    connection.execute(value)
    print('Пользователь добавлен в Избранное')

def add_black_list(connection, user_id, id_in_list):
    value = f"INSERT INTO black_list (user_id, blacklisted_id) VALUES ({user_id}, {id_in_list});"
    connection.execute(value)
    print('Пользователь добавлен в черный список')
