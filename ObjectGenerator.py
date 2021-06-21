
from random import randint

def labrador_character():
    return {"Name":"labrador","Symbol":"S", "HP": 100, "BaseDamage":30, "CriticalChance":10
    , "HitChance": 50, "DodgeChance": 30,"Type":"Player", "Symbol":"L", "Xpoz":1, "Ypoz":1
    , "Walkable":True, "MaxHP":100, "Armor":0, "lvlExp" : 0}

def shiba_character():
    return {"Name":"shiba", "Symbol":"S", "HP": 100, "BaseDamage":30, "CriticalChance":15
    , "HitChance": 50, "DodgeChance": 20, "Type":"Player", "Xpoz":1, "Ypoz":1
    , "Walkable":True, "MaxHP":100, "Armor":0, "lvlExp" : 0}

def doberman_character():
    return {"Name":"doberman", "Symbol":"S", "HP": 100, "BaseDamage":30, "CriticalChance":15
    , "HitChance": 50, "DodgeChance": 20, "Type":"Player", "Xpoz":1, "Ypoz":1
    , "Walkable":True, "MaxHP":100, "Armor":0, "lvlExp" : 0}

def mops_character():
    return {"Name":"mops","Symbol":"S", "HP": 100, "BaseDamage":10, "CriticalChance":5
    , "HitChance": 30, "DodgeChance": 15, "Type":"Player", "Xpoz":1, "Ypoz":1
    , "Walkable":True, "MaxHP":100, "Armor":0, "lvlExp" : 0}

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