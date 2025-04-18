import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'сюда Токен свой надо написать'
HODOR = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '27994'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_Part_train():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["id"] == '27994'