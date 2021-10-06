import requests
import json
from poke.models import *

base_url = 'https://pokeapi.co/api/v2/evolution-chain/'


def fetch_chain(chain_id):
    """Fetch and store the pokemon evolution chain represented by the argument.
    
    :param int chain_id: id of pokemon evolution chain
    :return: returns true if pokemon evolution chain was succesfully stored, false otherwise
    """
    url = base_url + str(chain_id) + '/'
    response = requests.get(url)
    if response.status_code==200:
        chaindata = json.loads(response.text)
        fetch_pokemon_and_evos(chaindata['chain'],0)
        return True
    else:
        return False

def fetch_pokemon_and_evos(chaindata, pre_id):
    """Fetch and store the pokemon and its evolutions recursively from a chaindata.
    
    :param dictionary chaindata: dictionary containing evolution chain data
    :param int pre_id: id of pokemon's pre evolution, 0 if pokemon has no pre evolutions
    :return: current pokemon's id
    :raises ChildProcessError: if there's an error fetching pokemon data
    """
    name = chaindata['species']['name']
    
    url = chaindata['species']['url'] 
    response = requests.get(url)
    # Get Id from species url
    if response.status_code==200:
        speciesdata = json.loads(response.text)
        id = speciesdata['id']
    else:
        raise ChildProcessError('No species data')

    url = 'https://pokeapi.co/api/v2/pokemon/'+str(id)+'/'
    response = requests.get(url)
    # Get height, weight, and stats from pokemon data
    if response.status_code == 200:
        pokedata = json.loads(response.text)
        height = pokedata['height']
        weight = pokedata['weight']
        base_stats = []
        for stat in pokedata['stats']:
            base_stats.append(stat['base_stat'])
    else:
        raise ChildProcessError('No pokemon data')

    evolutions = []
    for evo in chaindata['evolves_to']:
            evolutions.append(fetch_pokemon_and_evos(evo,id))

    pokemon = Pokemon.objects.update_or_create(
        id=id,name=name,
        height=height,
        weight=weight,
        hp=base_stats[0],
        attack=base_stats[1],
        defense=base_stats[2],
        special_attack=base_stats[3],
        special_defense=base_stats[4],
        speed=base_stats[5],
        evo_list=json.dumps(evolutions),
        pre_evo=pre_id
        )
    return id

# There are less than 480 chains
for i in range(480):
    if(fetch_chain(i)):
        print('Fetched and stored pokemon chain: ',i)
