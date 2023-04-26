import requests

# Use case 1: Get the name and weight of Pokemon
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1000")
if response.status_code == 200:
    data = response.json()
    heavy_pokemon = []
    for pokemon in data['results'][:100]:
        #print(pokemon['name'], pokemon['url'])
        details_response = requests.get(url=pokemon['url'])
        data2 = details_response.json()
        #print(pokemon['name'], data2['weight'])
        weight = data2['weight']
        if weight >= 3000:
                heavy_pokemon.append(f"{data2['name']} ({data2['weight']} kg)")
    print("Pokemon that weigh over 3000 :", heavy_pokemon)
else:
    print('Request failed with status code:', response.status_code)

# Use case 2: Get the base experience, 

# Use case 3: Get the name and URL of the first 20 Pokemon that are of the Fire type
def Pokemon_type 
response = requests.get("https://pokeapi.co/api/v2/type/fire")
if response.status_code == 200:
    data = response.json()
    Fire_pokemon =[]
    print("Pokemon Fire Type")
    for pokemon in data['pokemon'][:20]:
        Fire_pokemon.append([pokemon['pokemon']['name'],pokemon['pokemon']['url']])
        #print(f" name {pokemon['pokemon']['name']} url {pokemon['pokemon']['url']}")
    print("Pokemon that are of the Fire type:",Fire_pokemon)
else:
    print('Request failed with status code:', response.status_code)

"""print(f"Types: {[type['type']['name'] for type in pokemon['types']]}")
    print(f"Abilities: {[ability['ability']['name'] for ability in pokemon['abilities']]}")"""