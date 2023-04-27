import requests

url = "https://pokeapi.co/api/v2/"

def get_list_pokemon():
      response = requests.get(f"{url}/pokemon?limit=1000")
      data = response.json()["results"] 
      return data

# Get the list of pokemon form ("https://pokeapi.co/api/v2/pokemon?limit=1000")
pokemon_list = get_list_pokemon()

def get_pokemon_weight(pokemon_list):
      Weight_pokemon = []
      for pokemon in pokemon_list:
            response = requests.get(pokemon["url"])
            pokemon_data = response.json()
            Weight =pokemon_data["weight"]
            if Weight > 5000 :
                  Weight_pokemon.append(f"{pokemon['name']}( {Weight} kg)")
                  
      return Weight_pokemon


# Get the heavy Pokemon
weight_pokemon = get_pokemon_weight(pokemon_list)
print("List of Pokemon that weigh over 300 kg:")
for name in weight_pokemon:
           print(name)



def get_fire_pokemon(pokemon_list):
    """
    Takes a list of Pokemon and returns a list of names of Pokemon that are of the Fire type
    """
    fire_pokemon = []
    for pokemon in pokemon_list [:50]:
        response = requests.get(pokemon["url"])
        pokemon_data = response.json()
        types = [type["type"]["name"] for type in pokemon_data["types"]]
        if "fire" in types :
            fire_pokemon.append(pokemon["name"])
    return fire_pokemon          

# Get the Fire-type Pokemon
fire_pokemon = get_fire_pokemon(pokemon_list)
print("List of Pokemon that are of the Fire type:")
for name in fire_pokemon:
           print(name)



# Define the API endpoint for the Pokemon resource
pokemon_endpoint = url + "pokemon/"
def get_pokemon_abilities(pokemon_name):
    # Send a GET request to the API endpoint for the specific Pokemon to retrieve its details
    for pokemon in pokemon_list :
        response = requests.get(pokemon_endpoint + pokemon_name)
        pokemon_data = response.json()
        abilities = []
        for ability_obj in pokemon_data["abilities"]:
             abilities.append(ability_obj["ability"]["name"])

    return abilities
    
    
   

# Example usage:
# Get the abilities of Pikachu
pikachu_abilities = get_pokemon_abilities("pikachu")
print("Pikachu's abilities:")
print(pikachu_abilities)

            
            




            
            


