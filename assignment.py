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
                  Weight_pokemon.append(pokemon["name"])
      return Weight_pokemon


# Get the heavy Pokemon
weight_pokemon = get_pokemon_weight(pokemon_list)
print("List of Pokemon that weigh over 300 kg:")
for name in weight_pokemon:
           print(name)



            
            


