import requests
# Jesus Eduardo Garcia Campos 
# 2000965
def get_pokemon (url ='http://pokeapi.co/api/v2/pokemon-form/', offset=0):
  args = {'offset':offset} if offset else{}
  
  response = requests.get(url, params=args)
  
  if response.status_code ==200:
    payload = response.json()
    results = payload.get('results', [])
    
    if results:
      for pokemon in results:
        name = pokemon['name']
        print(name)
      next = input("Continuar Listando? [Y/N]").lower()
      if next == 'Y' or next == 'y':
        get_pokemon(offset=offset+20)
if __name__ == '__main__':
  url = 'http://pokeapi.co/api/v2/pokemon-form/'
  get_pokemon()
  # Script en python que consulta el api de pokemon 
  # para listar los nombres de pokemon pero se le agrego 
  # interacción para que listaras más pokemons segun se vaya requiriendo. 
  # Contribuyo: <Aquí va tu nombre> 
  # Fecha: <2/19/2023> 
