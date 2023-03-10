import vk_api
import pandas as pd
from config import vk_access_token, access_token_group, group_id


def get_top_photos(owner_id):
    '''Returns the top three photos for a user or group, sorted by number of likes.'''
    photos_dict = {}
    vk = vk_api.VkApi(token=vk_access_token)
    response = vk.method('photos.getAll',
                          {'owner_id': owner_id,
                           'extended': 1,
                           'count': 200})
    for item in response['items']:
        m = 0
        for i in item['sizes']:
            if i['height'] > m:
                m = i['height']
                url = i['url']
        photos_dict[item['id']] = {'url': url,
                                   'likes': item['likes']['count']}

    df = pd.DataFrame(photos_dict)
    data = df.transpose()
    data = data.sort_values(by='likes', ascending=False)
    top_photos = data.head(3)
    return top_photos.to_dict('index')


def get_messages_upload_server():
    '''Returns the upload server URL for group messages.'''
    vk = vk_api.VkApi(token=access_token_group)
    response = vk.method('photos.getMessagesUploadServer',
                          {'group_id': group_id})
    return response
