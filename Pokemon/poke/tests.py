from django.test import TestCase
from .models import Pokemon
import json

# Create your tests here.
class TestPokemonModel(TestCase):
    
    def setUp(self):
        self.test1 = Pokemon.objects.create(id='1',name='pokemon',height='45',weight='100',hp='20',attack='34',defense='34',special_attack='12',special_defense='65',speed='33',evo_list=json.dumps([12,42,4]),pre_evo='0')
   
    def test_pokemon_model_entry(self):
        """
        Test Pokemon model creation
        """
        self.assertTrue(isinstance(self.test1,Pokemon))
