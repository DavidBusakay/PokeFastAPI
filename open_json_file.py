import json

with open("Pokemons.json", "r+") as f:
    pokemons_list = json.load(f)