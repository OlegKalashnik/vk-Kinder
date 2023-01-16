# СДЕЛАНО выбор id в БД по id пользователя vk
def select_nalichie_users_DB(connection,id_vk):
    table = 'users'
    column1 = 'bd_id'
    column2 = 'id'
    value = f"""SELECT {column1},{column2} FROM {table} WHERE {column2}={id_vk};"""
    data = connection.execute(value).fetchall()
    return data

# проверка наличия в ЧС
def select_nalichie_users_v_blaklist(connection,bd_id):
    table = 'black_list'
    column2 = 'bl_list_id'
    value = f"""SELECT {column2} FROM {table} WHERE {column2}={bd_id};"""
    data = connection.execute(value).fetchall()
    return data

# проверка наличия в ЧС
def select_nalichie_users_v_favorites(connection,bd_id):
    table = 'favorites_users'
    column2 = 'fav_user_id'
    value = f"""SELECT {column2} FROM {table} WHERE {column2}={bd_id};"""
    data = connection.execute(value).fetchall()
    return data

# СДЕЛАНО выбор id БД для просмотра
def select_search_params(connection,sex,age_at,age_to,city,status):
    table1 = 'search_params'
    column1 = 'param_sex'
    column2 = 'param_city'
    column3 = 'param_age_at'
    column4 = 'param_age_to'
    column5 = 'param_status'
    column6 = 'id_user'
    value = f"""SELECT {column6} FROM {table1}
    WHERE {column1}={sex} AND {column2}={city} AND {column3}={age_at} AND {column4}={age_to} AND {column5}={status};"""
    data = connection.execute(value).fetchall()
    users_for_view = {}
    n = 1
    for exec in data:
        black_list = select_nalichie_users_v_blaklist(connection,exec[0])
        favorites = select_nalichie_users_v_favorites(connection,exec[0])
        if black_list == [] and favorites == []:
            users_for_view[n] = exec[0]
            n += 1
    return users_for_view


# выборка одного аккаунта для просмотра
def select_one_user_for_view(connection,bd_id):
    table = 'users'
    column1 = 'bd_id'
    value = f"""SELECT * FROM {table} WHERE {column1}={bd_id};"""
    data = connection.execute(value).fetchall()[0]
    return {'bd_id' : data[0],
            'id' : data[1],
            'first_name' : data[2],
            'last_name' : data[3],
            'city_id' : data[4],
            'city_title' : data[5],
            'link_pro' : data[6],
            'verified' : data[7],
            'sex' : data[8],
            'bdate' : data[9],
            'home_town' : data[10],
            'has_photo' : data[11],
            'online' : data[12],
            'domain' : data[13],
            'nickname' : data[14],
            'screen_name' : data[15],
            'maiden_name' : data[16],
            'friend_status' : data[17],
            'can_access_closed' : data[18],
            'is_closed' : data[19],
            'photo_1_id' : data[20],
            'photo_1_likes' : data[21],
            'photo_1_url' : data[22],
            'photo_2_id' : data[23],
            'photo_2_likes' : data[24],
            'photo_2_url' : data[25],
            'photo_3_id' : data[26],
            'photo_3_likes' : data[27],
            'photo_3_url' : data[28],
            'track_code' : data[29],
            'online_app' : data[30],
            'online_mobile' : data[31]
            }


# выборка всего списка избранных
def select_favorites(connection,id):
    table1 = 'users'
    column1 = 'id'
    value = f"""SELECT * FROM {table1} WHERE {column1}={id};"""
    bd_id = connection.execute(value).fetchall()[0][0]
    table2 = 'favorites_users'
    column2 = 'id_user'
    value2 = f"""SELECT * FROM {table2} WHERE {column2}={bd_id};"""
    data = connection.execute(value2).fetchall()
    n = 1
    dict = {}
    for item in data:
        dict[n]=select_one_user_for_view(connection,item[0])
        n +=1
    return dict


# выборка всего черного списка
def select_blacklist(connection,id):
    table1 = 'users'
    column1 = 'id'
    value = f"""SELECT * FROM {table1} WHERE {column1}={id};"""
    bd_id = connection.execute(value).fetchall()[0][0]
    table2 = 'black_list'
    column2 = 'id_user'
    value2 = f"""SELECT * FROM {table2} WHERE {column2}={bd_id};"""
    data = connection.execute(value2).fetchall()
    n = 1
    dict = {}
    for item in data:
        dict[n]=select_one_user_for_view(connection,item[0])
        n +=1
    return dict
