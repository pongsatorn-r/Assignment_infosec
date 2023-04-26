import requests
import json

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=1000").json()

heavy_pokemon = []

for pokemon in response["results"]:
    url = pokemon["url"]
    pokemon_data = requests.get(url).json()
    weight = pokemon_data["weight"]
    if weight > 300:
        heavy_pokemon.append(f"{pokemon['name']} ({weight} kg)")
        

print("Pokemon that weigh over 300 kg:")
for name in heavy_pokemon:
           print(name)