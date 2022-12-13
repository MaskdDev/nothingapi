import requests
import json


def get_user(user_id: int):
    user = requests.get(f"https://nothingapi.crypticcode.org/users/{user_id}")
    user = json.loads(user.text)
    return user
