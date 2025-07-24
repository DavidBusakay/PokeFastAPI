from fastapi import FastAPI, Path, HTTPException
from open_json_file import pokemons_list
from pokemon import Pokemon
from query import *


create_table()
insert_to_table(pokemons_list)

pokemons_dict = {}
for i, j in enumerate(pokemons_list):
    i += 1
    pokemons_dict[i] = j


app = FastAPI()

@app.get("/total_pokemons")
def get_numbers_of_pokemons() -> dict:
    return {"Nombre": len(select_all_pokemons())}


@app.get("/pokemons")
def get_all_pokemons() -> list[Pokemon]:
    pokemons = select_all_pokemons()
    response = []
    for row in pokemons:
        response.append(Pokemon(
            id=row[0],
            name=row[1],
            types=row[2].split(", "),
            total=row[3],
            hp=row[4],
            attack=row[5],
            defense=row[6],
            attack_special=row[7],
            defense_special=row[8],
            speed=row[9],
            evolution_id=row[10]
        ))
    return response


@app.get("/pokemons/{id}")
def get_pokemon(id: int = Path(ge=1)) -> Pokemon:
    row = select_pokemon(id)
    if not row:
        raise HTTPException(404, "Ce Pokémon n'existe pas !")
    return Pokemon(
        id=row[0],
        name=row[1],
        types=row[2].split(", "),
        total=row[3],
        hp=row[4],
        attack=row[5],
        defense=row[6],
        attack_special=row[7],
        defense_special=row[8],
        speed=row[9],
        evolution_id=row[10]
    )


@app.post("/pokemon")
def create_pokemon(pokemon: Pokemon) -> Pokemon:
    pokemons = select_all_pokemons()
    for row in pokemons:
        if pokemon.id == row[0] and pokemon.name == row[1]:
            raise HTTPException(409, "{pokemon.name} existe déjà !")
   
    response = insert_pokemon(pokemon)
    return Pokemon(
        id=response[0],
        name=response[1],
        types=response[2].split(", "),
        total=response[3],
        hp=response[4],
        attack=response[5],
        defense=response[6],
        attack_special=response[7],
        defense_special=response[8],
        speed=response[9],
        evolution_id=response[10]
    )
