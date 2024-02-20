import requests


def create_group(chat_id, name):
    url = "http://127.0.0.1:8000/api/group"
    data = {
        'chat_id': chat_id,
        'name': name
    }
    result = requests.post(url, data)
    return result.status_code


def create_task(chat_id, description):
    url = "http://127.0.0.1:8000/api/task"
    data = {
        'chat_id': chat_id,
        'description': description
    }
    result = requests.post(url, data)
    return result.status_code
