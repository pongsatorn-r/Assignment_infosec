import requests

# function for get pokemon list url https://pokeapi.co/api/v2/
def get_list_pokemon():
      response = requests.get(f"{url}/pokemon?limit=1000")
      data = response.json()["results"] 
      return data

# function for collect pokemon information (weight,type,ability)
def get_pokemon_data(pokemon_list):
      
      my_dict = {"Weight_pokemon":[],"fire_pokemon":[],"abilitie":[]};
      pokemon_name = "charizard"
      for pokemon in pokemon_list:
            
            response = requests.get(pokemon["url"])
            pokemon_data = response.json()
            Weight =pokemon_data["weight"]
            types = [type["type"]["name"] for type in pokemon_data["types"]]
            if Weight > 5000 :
                  my_dict["Weight_pokemon"].append(f"{pokemon['name']}( {Weight} kg)")
            if "fire" in types :
                  my_dict["fire_pokemon"].append(pokemon["name"]) 
            if pokemon['name'] == pokemon_name:
                for ability_obj in pokemon_data["abilities"]:
                  my_dict["abilitie"].append(ability_obj["ability"]["name"])

           
      print("List of Pokemon that weigh over 5000 kg:")   
      for name in my_dict["Weight_pokemon"][:10]:
              print(name)          
      print("\n")
      print("List of Pokemon that are of the Fire type:")
      for name in my_dict["fire_pokemon"][:10]:
              print(name)
      
        
      print("\n")
      print("Charizard's abilities:")
      print(my_dict["abilitie"])
      
            
      return  "\n"

          
 

url = "https://pokeapi.co/api/v2/" 

# get the list of pokemon form ("https://pokeapi.co/api/v2/pokemon?limit=1000")
pokemon_list = get_list_pokemon()

# get data form function get_pokemon_data(pokemon_list)
pokemon_data = get_pokemon_data(pokemon_list)
print(pokemon_data)


