
from random import randint

def labrador_character():
    return {"Name":"labrador","Symbol":"L", "HP": 100, "BaseDamage":15, "CriticalChance":20
    , "HitChance": 40, "DodgeChance": 60,"Type":"Player", "Symbol":"L", "Xpoz":1, "Ypoz":1
    , "Walkable":True, "MaxHP":100, "Armor":0, "lvlExp" : 0}

def shiba_character():
    return {"Name":"shiba", "Symbol":"S", "HP": 100, "BaseDamage":30, "CriticalChance":15
    , "HitChance": 40, "DodgeChance": 20, "Type":"Player", "Xpoz":1, "Ypoz":1
    , "Walkable":True, "MaxHP":100, "Armor":0, "lvlExp" : 0}

def doberman_character():
    return {"Name":"doberman", "Symbol":"D", "HP": 100, "BaseDamage":40, "CriticalChance":20
    , "HitChance": 50, "DodgeChance": 15, "Type":"Player", "Xpoz":1, "Ypoz":1
    , "Walkable":True, "MaxHP":100, "Armor":0, "lvlExp" : 0}

def mops_character():
    return {"Name":"mops","Symbol":"M", "HP": 100, "BaseDamage":15, "CriticalChance":10
    , "HitChance": 30, "DodgeChance": 15, "Type":"Player", "Xpoz":1, "Ypoz":1
    , "Walkable":True, "MaxHP":100, "Armor":0, "lvlExp" : 0}

def spawn_dogge(Xpoz, Ypoz):
    inventory = [spawn_scooby_snack(), spawn_scooby_snack()]
    return {"Name":"dogge", "Type":"Enemy", "Symbol":"D", "Xpoz":Xpoz
    , "Ypoz":Ypoz, "Walkable":False, "Inventory":inventory
    , "HP": 100, "MaxHP":100, "BaseDamage":20, "CriticalChance":10
    , "HitChance": 60, "DodgeChance": 20, "Armor":0}

def spawn_scooby_snack():
    return {"Name":"Scooby snack", "Type":"Consumable", "HpReward":20}

def spawn_floor():
    return {"Name":"Floor", "Type":"Map", "Symbol":".", "Walkable":True}

def spawn_collar():
    return {"Name": "Collar", "Type": "Cloth", "ArmorReward": 50}

def spawn_dog_food():
    return {"Name": "Dog food", "Type": "Consumable", "HpReward": 50}

def spawn_bone():
    return {"Name": "Bone", "Type": "Usable", "BaseDamageReward": 20, "DodgeChanceReward": -10}

def spawn_stick():
    return {"Name": "Stick", "Type": "Usable", "CriticalChanceReward": 20}

def spawn_banana_peel():
    return {"Name": "Banana peel", "Type": "Usable", "DodgeChanceReward": 0} #tu chciałam żeby całkowicie znikała możliwość uniku

def spawn_ball():
    return {"Name": "Ball", "Type": "Usable"}

# Trophies

def spawn_cats_claw():
    return {"Name": "Cat's claw"}

def spawn_dead_mouse():
    return {"Name": "Dead mouse"}

def spawn_boar_horn():
    return {"Name": "Boar horn"}