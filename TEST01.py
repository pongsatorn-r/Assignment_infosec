import requests

url = "https://pokeapi.co/api/v2/"

# Use case 1: List Pokemon names that weigh over 300 kg
response = requests.get(url=f"{url}/pokemon?offset=0&limit=1118")
if response.status_code == 200:
    data = response.json()
    heavy_pokemon = []
    for pokemon in data['results']:
        details_response = requests.get(url=pokemon['url'])
        if details_response.status_code == 200:
            details_data = details_response.json()
            weight = details_data['weight']
            if weight >= 3000:
                heavy_pokemon.append(details_data['name'])
    print("Pokemon that weigh over 300 kg:", heavy_pokemon)
else:
    print('Request failed with status code:', response.status_code)

# Use case 2: List Pokemon names that are of the Fire type
response = requests.get(url=f"{url}/type/fire")
if response.status_code == 200:
    data = response.json()
    fire_pokemon = []
    for pokemon in data['pokemon']:
        fire_pokemon.append(pokemon['pokemon']['name'])
    print("Pokemon that are of the Fire type:", fire_pokemon)
else:
    print('Request failed with status code:', response.status_code)

# Use case 3: Sort the ten heaviest Pokemon in order from greatest to least
response = requests.get(url=f"{url}/pokemon?offset=0&limit=1118")
if response.status_code == 200:
    data = response.json()
    pokemon_weight = {}
    for pokemon in data['results']:
        details_response = requests.get(url=pokemon['url'])
        if details_response.status_code == 200:
            details_data = details_response.json()
            weight = details_data['weight']
            pokemon_weight[details_data['name']] = weight
    heaviest_pokemon = sorted(pokemon_weight, key=pokemon_weight.get, reverse=True)[:10]
    print("The 10 heaviest Pokemon, in order from greatest to least:", heaviest_pokemon)
else:
    print('Request failed with status code:', response.status_code)
