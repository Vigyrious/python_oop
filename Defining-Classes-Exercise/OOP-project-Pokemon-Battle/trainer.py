from Library import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []


    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemon:
            return f"This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"



    def release_pokemon(self, pokemon_name):
        pokemon = [p for p in self.pokemon if p.name == pokemon_name]
        if pokemon:
            self.pokemon.remove(pokemon[0])
            return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"


    def trainer_data(self):
        data = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n- "
        for p in self.pokemon:
            data += p.pokemon_details() + "\n"
        return data
