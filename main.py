import requests

class Pokemon:
  base_url = 'https://pokeapi.co/api/v2' # https://pokeapi.co/api/v2/pokemon/nome_de_um_pokemon

  def __init__(self, name:str) -> None:
    self.name:str  = name
    self.url = f"{self.base_url}/pokemon/{name}"

  def get_pokemon_information(self) -> None:
    response:str = requests.get(self.url)
    return response.json()
  
  def search_pokemon_by_ability(self, ability_name) -> None:
    try:
      response:str = requests.get(f"{self.base_url}/ability/{ability_name}")
      response.raise_for_status()

      ability_data = response.json()
      return ability_data


    except requests.exceptions.HTTPError as error:
      if error.response.status_code == 404:
        return 'Habilidade não encontrada'
      else:
        raise

  def __repr__(self) -> str:
    pokemon_data:dict = self.get_pokemon_information()
    pokemon:str = f"Nome: {pokemon_data['name']}\n"
    pokemon += f"ID: {pokemon_data['id']}\n"
    pokemon += f"Height: {pokemon_data['height']}\n"
    pokemon += f"Weight: {pokemon_data['weight']}\n"
    pokemon += f"Ordenation: {pokemon_data['order']}\n"

    # return f"<Pokemon: {pokemon['name']}"
    return pokemon

if __name__ == '__main__':
  pokemon_name = input('Digite um pokemon: ')
  p: Pokemon = Pokemon(pokemon_name)
  print(p)

  ability_name = input('Digite o nome da habilidade: ')
  result = p.search_pokemon_by_ability(ability_name)

  if isinstance(result, dict):
    # print(f"Pokemons com a habilidade '{ability_name}': {result}")

    for pokemon_name in result['pokemon']:
      print(pokemon_name['pokemon']['name'])
  else:
    print(result)