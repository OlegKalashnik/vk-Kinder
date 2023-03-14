from DB.connect import connection
from DB.create import creat_all_tables
from DB.insert import (add_users, add_users_and_search_params, add_favorites_users, add_black_list)
from DB.select import (select_search_params,select_one_user_for_view, select_favorites,mselect_blacklist)
from app.main_app import (search_people_and_photos, cur_user)
from functions import (event_listen,write_msg,prepare_photo)

creat_all_tables(connection)

favorites = 1
black_list = 1


   
message, user_id = event_listen()
sex, city, dict_cur_user = cur_user(user_id)
add_users(connection,dict_cur_user)
age_at = 29
age_to = 33
status = 6
dict_favorites = select_favorites(connection,user_id)
dict_blacklist = select_blacklist(connection,user_id)


if message == "начать":
    name = dict_cur_user[user_id]['first_name']
    write_msg(user_id=user_id, message=f"""Привет, {name}! Введите 'поиск' для начала поиска анкет, для просмотра избранных анкет введите 'показать избранные анкеты', для просмотра черного списка введите 'показать черный список'""")


elif message == "поиск":
    dict_all_questionnaires = search_people_and_photos(sex, age_at, age_to, city, status)
    add_users_and_search_params(connection,dict_all_questionnaires,sex,age_at,age_to,city,status)
    name = dict_cur_user[user_id]['first_name']
    write_msg(user_id, f"{name}, для просмотра анкет введите 'смотреть'")


elif message == "смотреть":
    dict_for_watch = select_search_params(connection,sex,age_at,age_to,city,status)#

    if dict_for_watch == {}:
        write_msg(user_id, f"Записей для просмотра больше нет. Для повторного описка введите 'Поиск'")
    else:
        dict_one_question = select_one_user_for_view(connection,dict_for_watch[1])
        text, photo = prepare_photo(dict_one_question)
        write_msg(user_id, text, photo)
        write_msg(user_id, "Для добавления в избранное введите 'добавить в избранное', для добавления в черный список введите 'добавить в черный список'")
        id_in_list = dict_one_question['id']


elif message == "добавить в избранное":
    add_favorites_users(connection,user_id,id_in_list)
    name = dict_cur_user[user_id]['first_name']
    write_msg(user_id, f"{name}, для дальнейшего просмотра введите 'смотреть'")


elif message == "добавить в черный список":
    add_black_list(connection,user_id,id_in_list)
    name = dict_cur_user[user_id]['first_name']
    write_msg(user_id, f"{name}, для дальнейшего просмотра введите 'смотреть'")


elif message == "показать избранные анкеты":
    if dict_favorites == {}:
        write_msg(user_id, "У вас нет избранных анкет. Может добавим?")
    else:
        if favorites not in dict_favorites.keys():
            write_msg(user_id, f"Избранные анкеты закончились. Для просмотра сначала введите 'с начала списка избранных'")
        else:
            dict_one_question = dict_favorites[favorites]
            text, photo = prepare_photo(dict_one_question)
            write_msg(user_id, text, photo)
            favorites += 1


elif message == "с начала списка избранных":
    favorites = 1
    write_msg(user_id, "для просмотра избранных анкет введите 'показать избранные анкеты'")


elif message == "показать черный список":
    if dict_blacklist == {}:
        write_msg(user_id, "У вас нет анкет в ЧС. Может добавим?")
    else:
        if black_list not in dict_blacklist.keys():
            write_msg(user_id, f"Анкеты в ЧС закончились. . Для просмотра сначала введите 'с начала черного списка'")
        else:
            dict_one_question = dict_blacklist[black_list]
            text, photo = prepare_photo(dict_one_question)
            write_msg(user_id, text, photo)
            black_list += 1


elif message == "с начала черного списка":
    black_list = 1
    write_msg(user_id, "Смотрим черный список?")


elif message == "пока":
    write_msg(user_id, "Пока((")


else:
    write_msg(user_id, "Не поняла вашего ответа...")
