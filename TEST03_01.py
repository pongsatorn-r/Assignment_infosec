import requests

# URL of the PokeAPI
url = "https://pokeapi.co/api/v2/"

def get_pokemon_list():
    """
    Fetches the list of Pokemon from the PokeAPI
    Returns a list of dictionaries containing the name and URL of each Pokemon
    """
    response = requests.get(f"{url}/pokemon?offset=0&limit=1000")
    results = response.json()["results"]
    return results

def get_heavy_pokemon(pokemon_list):
    """
    Takes a list of Pokemon and returns a list of names of Pokemon that weigh over 300 kg
    """
    heavy_pokemon = []
    for pokemon in pokemon_list:
        response = requests.get(pokemon["url"])
        pokemon_data = response.json()
        weight = pokemon_data["weight"]
        if weight > 300:
            heavy_pokemon.append(pokemon["name"])
    return heavy_pokemon

def get_fire_pokemon(pokemon_list):
    """
    Takes a list of Pokemon and returns a list of names of Pokemon that are of the Fire type
    """
    fire_pokemon = []
    for pokemon in pokemon_list:
        response = requests.get(pokemon["url"])
        pokemon_data = response.json()
        types = [type["type"]["name"] for type in pokemon_data["types"]]
        if "fire" in types:
            fire_pokemon.append(pokemon["name"])
    return fire_pokemon

def get_top_heavy_pokemon(pokemon_list):
    """
    Takes a list of Pokemon and returns a list of the names of the top 10 heaviest Pokemon
    """
    pokemon_weight = {}
    for pokemon in pokemon_list:
        response = requests.get(pokemon["url"])
        pokemon_data = response.json()
        pokemon_weight[pokemon_data["name"]] = pokemon_data["weight"]
    heaviest_pokemon = sorted(pokemon_weight, key=pokemon_weight.get, reverse=True)[:10]
    return heaviest_pokemon

# Get the list of Pokemon
pokemon_list = get_pokemon_list()

# Get the heavy Pokemon
heavy_pokemon = get_heavy_pokemon(pokemon_list)
print("List of Pokemon that weigh over 300 kg:")
print(heavy_pokemon)

# Get the Fire-type Pokemon
fire_pokemon = get_fire_pokemon(pokemon_list)
print("List of Pokemon that are of the Fire type:")
print(fire_pokemon)

# Get the top 10 heaviest Pokemon
top_heavy_pokemon = get_top_heavy_pokemon(pokemon_list)
print("List of the top 10 heaviest Pokemon:")
print(top_heavy_pokemon)

'''
import requests

def get_pokemon_by_weight(weight):
    url = "https://pokeapi.co/api/v2/pokemon?offset=0&limit=1118"
    response = requests.get(url)
    pokemon_list = response.json()["results"]
    pokemon_weight = {}
    for pokemon in pokemon_list:
        url = pokemon["url"]
        response = requests.get(url)
        weight = response.json()["weight"]
        if weight > 300:
            pokemon_weight[pokemon["name"]] = weight
    sorted_pokemon = sorted(pokemon_weight, key=pokemon_weight.get, reverse=True)
    return sorted_pokemon[:10]

def get_pokemon_by_type(type_name):
    url = f"https://pokeapi.co/api/v2/type/{type_name}"
    response = requests.get(url)
    pokemon_list = response.json()["pokemon"]
    pokemon_names = []
    for pokemon in pokemon_list:
        pokemon_names.append(pokemon["pokemon"]["name"])
    return pokemon_names

def get_pokemon_by_ability(ability_name):
    url = f"https://pokeapi.co/api/v2/ability/{ability_name}"
    response = requests.get(url)
    pokemon_list = response.json()["pokemon"]
    pokemon_names = []
    for pokemon in pokemon_list:
        pokemon_names.append(pokemon["pokemon"]["name"])
    return pokemon_names

if __name__ == "__main__":
    # Example usage
    for pokemon in __name__:
           print(f"Pokemon Weight 3000{get_pokemon_by_weight(3000)}")
           print("Pokemon Type Fire",get_pokemon_by_type("fire"))
    #print(get_pokemon_by_ability("pressure"))
'''

