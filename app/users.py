from config.imports import *


def users_get(ids):
    ''' Возвращает расширенную информацию о пользователях.
    '''
    all_persons = {}
    link_profile = 'https://vk.com/id'
    vk = vk_api.VkApi(token=vk_access_token)
    response = vk.method('users.get', {'user_ids': ids,
                                       'fields': 'verified, sex, bdate, city, home_town, has_photo, online, domain, nickname, screen_name, maiden_name, friend_status'})
    for item in response:
        for key in item.keys():
            if key == 'city':
                all_persons[item['id']]['city_id'] = item[key]['id']
                all_persons[item['id']]['city_title'] = item[key]['title']
            elif item['id'] not in all_persons.keys():
                all_persons[item['id']] = {f'{key}' : item[key]}
            else:
                all_persons[item['id']][key] = item[key]
        all_persons[item['id']]['link_pro'] = link_profile + str(item['id'])
    return all_persons


def users_search(sex, age_at, age_to, city, status):
    ''' Возвращает список пользователей в соответствии с заданным критерием поиска.
    '''
    all_persons = {}
    link_profile = 'https://vk.com/id'
    vk = vk_api.VkApi(token=vk_access_token)
    response = vk.method('users.search', {'sort': 1,
                                          'sex': sex,
                                          'status': status,
                                          'age_from': age_at,
                                          'age_to': age_to,
                                          'has_photo': 1,
                                          'count': 50,
                                          'fields': 'verified, sex, bdate, city, home_town, has_photo, online, domain, nickname, screen_name, maiden_name, friend_status',
                                          'city': city})
    for item in response['items']:
        if item["is_closed"] == False:
            for key in item.keys():
                if key == 'city':
                    all_persons[item['id']]['city_id'] = item[key]['id']
                    all_persons[item['id']]['city_title'] = item[key]['title']
                elif item['id'] not in all_persons.keys():
                    all_persons[item['id']] = {f'{key}' : item[key]}
                else:
                    all_persons[item['id']][key] = item[key]
            all_persons[item['id']]['link_pro'] = link_profile + str(item['id'])
    return all_persons
