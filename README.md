# PokéFastAPI

PokéFastAPI est une API REST développée avec FastAPI permettant de consulter et manipuler les données des Pokémon de la première génération. Les données sont stockées dans une base SQLite et initialisées à partir d'un fichier JSON.

## Fonctionnalités

- **Consultation du nombre total de Pokémon**
- **Liste de tous les Pokémon**
- **Consultation d'un Pokémon par son identifiant**
- **Ajout d'un nouveau Pokémon**

## Structure des fichiers

- `main.py` : Point d'entrée de l'API FastAPI, routes et logique principale.
- `query.py` : Fonctions d'accès à la base de données SQLite (création, insertion, sélection).
- `pokemon.py` : Définition de la classe `Pokemon` (dataclass).
- `open_json_file.py` : Chargement des données Pokémon depuis le fichier JSON.
- `Pokemons.json` : Fichier contenant les données des Pokémon.
- `requirements.txt` : Dépendances Python du projet.

## Installation

1. **Cloner le projet**
2. **Créer un environnement virtuel**
   ```powershell
   python -m venv env
   .\env\Scripts\activate
   ```
3. **Installer les dépendances**
   ```powershell
   pip install -r requirements.txt
   ```

## Initialisation de la base de données

Lors du lancement de l'API, la base de données est créée et les Pokémon sont insérés automatiquement à partir du fichier JSON.

## Lancement de l'API

```powershell
uvicorn main:app --reload
```

L'API sera accessible sur `http://127.0.0.1:8000`.

## Endpoints

- `GET /total_pokemons` : Retourne le nombre total de Pokémon.
- `GET /pokemons` : Retourne la liste complète des Pokémon.
- `GET /pokemons/{id}` : Retourne les informations d'un Pokémon par son identifiant.
- `POST /pokemon` : Ajoute un nouveau Pokémon à la base de données.

## Exemple de réponse

```json
{
  "id": 1,
  "name": "Bulbasaur",
  "types": ["Poison"],
  "total": 318,
  "hp": 45,
  "attack": 49,
  "defense": 49,
  "attack_special": 65,
  "defense_special": 65,
  "speed": 45,
  "evolution_id": 2
}
```

## Remarques

- Les données sont automatiquement insérées à chaque démarrage (attention à la duplication si la base existe déjà).
- Le fichier JSON doit être correctement formaté et contenir tous les champs nécessaires.
- L'ajout d'un Pokémon vérifie la non-duplication par id et nom.

## Auteur

David Busakay

---

N'hésitez pas à adapter ce projet pour d'autres générations ou à enrichir les fonctionnalités !
