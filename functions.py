from config.imports import *
from vk_api.longpoll import VkLongPoll, VkEventType


vkt = vk_api.VkApi(token=access_token_group)
longpoll = VkLongPoll(vkt)


def event_listen():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                message = event.text.lower()
                return message, event.user_id


def write_msg(user_id, message, attachment=None):
    if attachment != None:
        att = 'Прикреплены фото'
    else:
        att = 'Нет'
    print(f'''Пользователю с ID {user_id} отправлено сообщение"{message}"
    Вложения: {att}''')
    vkt.method('messages.send',
              {'user_id': user_id,
               'message': message,
               'random_id': randrange(10 ** 7),
               'attachment': attachment})


def prepare_photo(dict_all_persons):
    if 'photo_1_url' in dict_all_persons.keys() and 'photo_2_url' in dict_all_persons.keys() and 'photo_3_url' in dict_all_persons.keys():
        attachment = [dict_all_persons['photo_1_url'], dict_all_persons['photo_2_url'],dict_all_persons['photo_3_url']]
    elif 'photo_1_url' in dict_all_persons.keys() and 'photo_2_url' in dict_all_persons.keys() and 'photo_3_url' not in dict_all_persons.keys():
        attachment = [dict_all_persons['photo_1_url'], dict_all_persons['photo_2_url']]
    elif 'photo_1_url' in dict_all_persons.keys() and 'photo_2_url' not in dict_all_persons.keys() and 'photo_3_url' not in dict_all_persons.keys():
        attachment = [dict_all_persons['photo_1_url']]
    text = f"""{dict_all_persons['first_name']} {dict_all_persons['last_name']}
    {dict_all_persons['link_pro']}"""
    photo = ''
    for att in range(1,len(attachment)+1):
        if photo == '':
            photo += 'photo'+str(dict_all_persons['id'])+'_'+str(dict_all_persons[f'photo_{att}_id'])
        else:
            photo += ',photo'+str(dict_all_persons['id'])+'_'+str(dict_all_persons[f'photo_{att}_id'])
    return text, photo
