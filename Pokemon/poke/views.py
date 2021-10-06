from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import *
from django.http import Http404
import json



def get_evolution_data(poke):
    evolutions = []
    for evo_id in json.loads(poke.evo_list):
        evo = Pokemon.objects.get(pk=evo_id)
        evolutions.append({
            'id': evo_id,
            'name': evo.name,
            'evolutions': get_evolution_data(evo)
        })
    return evolutions

def get_pre_evolution_data(poke):
    pre = []
    while(poke.pre_evo != 0):
        poke = Pokemon.objects.get(pk=poke.pre_evo)
        pre.append({
            'id': poke.id,
            'name': poke.name,
            })
    return pre

class PokemonDetail(View):

    def get(self,request,poke_name):
        try:
            pokemon = Pokemon.objects.get(name=poke_name)
            pre = get_pre_evolution_data(pokemon)
            evolutions = get_evolution_data(pokemon)
            poke_data = {
                'name': pokemon.name,
                'id': pokemon.id,
                'height': pokemon.height,
                'weight': pokemon.weight,
                'hp': pokemon.hp,
                'attack': pokemon.attack,
                'defense': pokemon.defense,
                'special-attack': pokemon.special_attack,
                'special-defense': pokemon.special_defense,
                'speed': pokemon.speed,
                'evolutions': evolutions,
                'preevolutions': pre,
            }
        except Pokemon.DoesNotExist:
            raise Http404('There is no pokemon with the given name.')

        return JsonResponse(poke_data)


