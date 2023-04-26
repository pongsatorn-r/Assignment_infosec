import requests






Web_url = "https://pokeapi.co/api/v2/"
#connent to URL of API
#pokemon_name = input("Enter a Pokemon name or ID: ")
#Get input for pokemon name or ID
# f" = formatted string literals 

#print(f"{Web_url}pokemon/{pokemon_name}")
#print(response)

'''def Pokemon_Weight():
    response = requests.get(f"{Web_url}pokemon?offset=20&limit=1000")
    heavy_pokemon = []
    name_pokemon = []
    pokemon_weight = [heavy_pokemon + name_pokemon]
    for pokemon in response.json()["results"]:
        pokemon_url = pokemon["url"]
        pokemon_data = requests.get(pokemon_url).json()
        if pokemon_data["weight"] > 300:
            name_pokemon.append(pokemon_data["name"])
            heavy_pokemon.append(pokemon_data["weight"])
            
    
    # Return the list of heavy Pokemon names
    return name_pokemon,heavy_pokemon'''



#print("Heavy Pokemon:")
#print(Pokemon_Weight())

response = requests.get(url=f"{Web_url}/pokemon?offset=0&limit=1118")
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
    heaviest_pokemon_with_weight = []
    for pokemon in heaviest_pokemon:
        weight = pokemon_weight[pokemon]
        heaviest_pokemon_with_weight.append(f"{pokemon} ({weight} lbs)")
    print("The 10 heaviest Pokemon, in order from greatest to least:")
    print("\n".join(heaviest_pokemon_with_weight))
else:
    print('Request failed with status code:', response.status_code)
