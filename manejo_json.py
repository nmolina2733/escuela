import requests
import json
from types import SimpleNamespace

 

url= "https://www.13.cl/"

url2="https://portales.inacap.cl/"

url3="https://api.cmfchile.cl/api-sbifv3/recursos_api/uf?apikey=b672bed2b16b384ef03e8687d655eb6adf699f2d&formato=json"

url4="https://rickandmortyapi.com/api/character/3"

url5="https://pokeapi.co/api/v2/pokemon/snorlax"

datos= requests.get(url5)

 

x = json.loads(datos.text, object_hook=lambda d: SimpleNamespace(**d))

#print(datos.text)

#print(x.UFs [0].Valor)

#print(x.id, x.name, x.status)

print(x.abilities[0].ability.name)

for a in x.abilities:

    print(a.ability.name)