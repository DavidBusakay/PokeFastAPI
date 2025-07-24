import sqlite3

db_name = "pokemon.db"

def create_table():
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS pokemon")
    cur.execute(
        """CREATE TABLE pokemon (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name VARCHAR, types TEXT, total INTEGER, 
        hp INTEGER, attack INTEGER, defense INTEGER, 
        attack_special INTEGER, defense_special INTEGER, 
        speed INTEGER, evolution_id INTEGER)"""
    )
    conn.close()


def insert_to_table(pokemons: list):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    data = []
    
    for p in pokemons:
        name = p.get("name", "")
        types = ", ".join(p.get("types", [])) if isinstance(p.get("types"), list) else str(p.get("types", ""))
        total = p.get("total", None)
        hp = p.get("hp", None)
        attack = p.get("attack", None)
        defense = p.get("defense", None)
        attack_special = p.get("attack_special", None)
        defense_special = p.get("defense_special", None)
        speed = p.get("speed", None)
        evolution_id = p.get("evolution_id", None)
        data.append((name, types, total, hp, attack, defense, attack_special, defense_special, speed, evolution_id))
    
    cur.executemany(
        """INSERT INTO pokemon (name, types, total, hp, attack, defense, attack_special, defense_special, speed, evolution_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", data
    )
    conn.commit()
    conn.close()


def select_all_pokemons():
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM pokemon")
    pokemons = cur.fetchall()
    conn.close()
    return pokemons


def insert_pokemon(pokemon):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    
    if hasattr(pokemon, '__dict__'):
        p = pokemon.__dict__
    else:
        p = dict(pokemon)
    
    name = p.get("name", "")
    types = ", ".join(p.get("types", [])) if isinstance(p.get("types"), list) else str(p.get("types", ""))
    total = p.get("total", None)
    hp = p.get("hp", None)
    attack = p.get("attack", None)
    defense = p.get("defense", None)
    attack_special = p.get("attack_special", None)
    defense_special = p.get("defense_special", None)
    speed = p.get("speed", None)
    evolution_id = p.get("evolution_id", None)

    cur.execute(
        """INSERT INTO pokemon (name, types, total, hp, attack, defense, attack_special, defense_special, speed, evolution_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (name, types, total, hp, attack, defense, attack_special, defense_special, speed, evolution_id)
    )
    conn.commit()

    # On récupère l'id auto-incrémenté
    inserted_id = cur.lastrowid
    cur.execute("SELECT * FROM pokemon WHERE id = ?", (inserted_id,))
    inserted_pokemon = cur.fetchone()
    conn.close()
    return inserted_pokemon


def select_pokemon(id: int):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    cur.execute("SELECT * FROM pokemon WHERE id = ?", (id,))
    pokemon = cur.fetchone()
    conn.close()
    return pokemon


def update_pokemon(pokemon, id):
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    
    if hasattr(pokemon, '__dict__'):
        p = pokemon.__dict__
    else:
        p = dict(pokemon)
    
    name = p.get("name", "")
    types = ", ".join(p.get("types", [])) if isinstance(p.get("types"), list) else str(p.get("types", ""))
    total = p.get("total", None)
    hp = p.get("hp", None)
    attack = p.get("attack", None)
    defense = p.get("defense", None)
    attack_special = p.get("attack_special", None)
    defense_special = p.get("defense_special", None)
    speed = p.get("speed", None)
    evolution_id = p.get("evolution_id", None)

    try:
        print(f"Nom : {name}")
        cur.execute(
            """UPDATE pokemon SET name = ?, types = ?, total = ?, hp = ?, attack = ?, defense = ?, 
            attack_special = ?, defense_special = ?, speed = ?, evolution_id = ? WHERE id = ?""",
            (name, types, total, hp, attack, defense, attack_special, defense_special, speed, evolution_id, id)
        )
        conn.commit()

        if cur.rowcount == 0:
            print(f"DEBUG : Aucune row mise à jour avec le nom : {id}")
            return None

        cur.execute("SELECT * FROM pokemon WHERE name = ?", (name,))
        updated_pokemon = cur.fetchone()
        if updated_pokemon:
            print(f"DEBUG : La query SELECT retourne 'None' pour le pokemon avec le nom : {name}")
            return updated_pokemon
        else:
            return None
    except sqlite3.Error as e:
        print(f"Une erreur s'est produite lors de la mise à jour : {e}")
        conn.rollback()
        return None
    finally:
        conn.close()
