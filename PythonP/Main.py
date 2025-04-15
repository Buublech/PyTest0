import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '86f6be5c14d1e5c676ca5f35db39f9a2'
HODOR = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}


body_create = {
    "name": "БоберЪ",
    "photo_id": 33
}


resp_create = requests.post(url = f'{URL}/pokemons', headers = HODOR, json = body_create)
print(resp_create.json())

pokemoshka = resp_create.json()['id']

body_catch = {
    "pokemon_id": pokemoshka
}

resp_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HODOR, json = body_catch)
print(resp_catch.json())

body_change = {
    "pokemon_id": pokemoshka,
    "name": "Ежык",
    "photo_id": 28
}
resp_change = requests.put(url = f'{URL}/pokemons', headers = HODOR, json = body_change)
print(resp_change.json())