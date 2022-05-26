import json
import config
import requests


def get_headers():
    return {
        'Accept': 'application/json',
        'Authorization': f'Bearer {config.API_TOKEN}',
        'Content-Type': 'application/json'
    }


def get_url(path):
    path = path.strip()
    path = path[0] == '/' and path or path[1:]
    return f'{config.API_BASE_URL}{path}'


def get_request(url: str):
    return requests.get(get_url(url), headers=get_headers())


def post_request(url: str, data):
    return requests.post(get_url(url), headers=get_headers(), data=data)


def put_request(url: str, data):
    return requests.put(get_url(url), headers=get_headers(), data=data)


def delete_request(url: str):
    return requests.delete(get_url(url), headers=get_headers())


def create_character(discord_id: int):
    return post_request('/api/characters', data=json.dumps({
        'data': {
            'discordId': f'{discord_id}',
            'level': 1,
            'exp': 0,
            'money': 5,
        }
    }))
