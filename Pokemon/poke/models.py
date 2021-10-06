from django.db import models

#pokemon has: id, name, height, weight, base_stats, base_stats name, evo list, pre evo.
class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    height = models.IntegerField()
    weight = models.IntegerField()
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()
    evo_list = models.CharField(max_length=200)
    pre_evo = models.IntegerField()
    