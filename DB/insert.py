from DB.select import select_nalichie_users_DB


# СДЕЛАНО добавление множества либо одного пользователя
def add_users(connection,dict):
    for key in dict.keys():
        data = select_nalichie_users_DB(connection,key)
        if data == []:
            value = f'''insert into users('''
            columns = ''''''
            values = f""""""
            for key2 in dict[key].keys():
                if type(dict[key][key2]) == str:
                    if "'" in dict[key][key2]:
                        dict[key][key2] = dict[key][key2].replace("'",'"')
                columns += f'''"{key2}",'''
                values += f"""'{dict[key][key2]}',"""
            columns = columns[:len(columns)-1]
            values = values[:len(values)-1]
            value = value + columns + ') values (' + values + ');'
            connection.execute(value)
            print('пользователь добавлен в БД')
        else:
            print('пользователь есть в БД')

# СДЕЛАНО добавление множества пользователей vk вместе с параметрами поиска
def add_users_and_search_params(connection,dict,sex,age_at,age_to,city,status):
    for key in dict.keys():
        data = select_nalichie_users_DB(connection,key)
        if data == []:
            value = f'''insert into users('''
            columns = ''''''
            values = f""""""
            for key2 in dict[key].keys():
                if type(dict[key][key2]) == str:
                    if "'" in dict[key][key2]:
                        dict[key][key2] = dict[key][key2].replace("'",'"')
                columns += f'''"{key2}",'''
                values += f"""'{dict[key][key2]}',"""
            columns = columns[:len(columns)-1]
            values = values[:len(values)-1]
            value = value + columns + ') values (' + values + ') RETURNING bd_id;'
            n = connection.execute(value).fetchone()
            add_search_params(connection,n[0],sex,age_at,age_to,city,status)
            print('пользователь добавлен в БД')
        else:
            print('пользователь есть в БД')


# СДЕЛАНО встроенная функция добавления параметров поиска
def add_search_params(connection,n,sex,age_at,age_to,city,status):
    value = f'''INSERT INTO search_params('''
    columns = '''"param_sex","param_age_at","param_age_to","param_city","param_status","id_user"'''
    values = f"""{sex},{age_at},{age_to},{city},{status},{n}"""
    value = value + columns + ') VALUES (' + values + ')'
    connection.execute(value)


# СДЕЛАНО добавление избранных
def add_favorites_users(connection,user_id,id_in_list):
    id_user = select_nalichie_users_DB(connection,id_in_list)[0][0]
    fav_user_id = select_nalichie_users_DB(connection,user_id)[0][0]
    value = f'''INSERT INTO favorites_users('''
    columns = '''"fav_user_id","id_user"'''
    values = f"""{id_user},{fav_user_id}"""
    value = value + columns + ') VALUES (' + values + ')'
    connection.execute(value)



# СДЕЛАНО добавление черного списка
def add_black_list(connection,user_id,id_in_list):
    id_user = select_nalichie_users_DB(connection,id_in_list)[0][0]
    bl_list_id = select_nalichie_users_DB(connection,user_id)[0][0]
    value = f'''INSERT INTO black_list('''
    columns = '''"bl_list_id","id_user"'''
    values = f"""{id_user},{bl_list_id}"""
    value = value + columns + ') VALUES (' + values + ')'
    connection.execute(value)
