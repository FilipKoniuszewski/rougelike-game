
from random import randint


def spawn_player():
    return {"Name":"player", "Type":"Player", "Symbol":"@", "Xpoz":1, "Ypoz":1
    , "Walkable":False, "HP": 100, "MaxHP":100, "BaseDamage":20, "CriticalChance":10
    , "HitChance": 60, "DodgeChance": 20, "Armor":0}


def spawn_dogge(Xpoz, Ypoz):
    inventory = [spawn_scooby_crunch(), spawn_scooby_crunch()]
    return {"Name":"dogge", "Type":"Enemy", "Symbol":"D", "Xpoz":Xpoz
    , "Ypoz":Ypoz, "Walkable":False, "Inventory":inventory
    , "HP": 100, "MaxHP":100, "BaseDamage":20, "CriticalChance":10
    , "HitChance": 60, "DodgeChance": 20, "Armor":0}

def spawn_scooby_crunch():
    return {"Name":"scooby crunch", "Type":"Consumable", "HpReward":20}

def spawn_floor():
    return {"Name":"Floor", "Type":"Map", "Symbol":".", "Walkable":True}

