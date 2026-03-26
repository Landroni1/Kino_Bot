import requests
from config_data.config import API_URL, HEADERS

def get_movie_data(query):
    params = {
        'query': query,
        'limit': 1
    }
    try:
        response = requests.get(API_URL, headers=HEADERS, params=params)
        if response.status_code == 200:
            data = response.json()
            if data.get('docs'):
                return data['docs'][0]
        return None
    except Exception as e:
        print('Ошибка запроса:', e)
        return None