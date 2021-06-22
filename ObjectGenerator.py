
from random import randint

def labrador_character():
    inventory = [spawn_scooby_snack(), spawn_scooby_snack()]
    return {"Name":"labrador","Symbol":"L", "HP": 100, "BaseDamage":15, "CriticalChance":20
    , "DodgeChance": 60,"Type":"Player", "Xpoz":1, "Ypoz":1
    , "Walkable":False, "MaxHP":100, "Armor":0, "Xp" : 0, "Inventory":inventory}

def shiba_character():
    inventory = []
    return {"Name":"shiba", "Symbol":"S", "HP": 100, "BaseDamage":30, "CriticalChance":15
    , "DodgeChance": 20, "Type":"Player", "Xpoz":1, "Ypoz":1
    , "Walkable":False, "MaxHP":100, "Armor":0, "Xp" : 0, "Inventory":inventory}

def doberman_character():
    inventory = []
    return {"Name":"doberman", "Symbol":"D", "HP": 100, "BaseDamage":40, "CriticalChance":20
    , "DodgeChance": 15, "Type":"Player", "Xpoz":1, "Ypoz":1
    , "Walkable":False, "MaxHP":100, "Armor":0, "Xp" : 0, "Inventory":inventory}

def mops_character():
    inventory = []
    return {"Name":"mops","Symbol":"M", "HP": 100, "BaseDamage":15, "CriticalChance":10
    , "DodgeChance": 15, "Type":"Player", "Xpoz":1, "Ypoz":1
    , "Walkable":False, "MaxHP":100, "Armor":0, "Xp" : 0, "Inventory":inventory}

def spawn_dogge(Xpoz, Ypoz):
    inventory = [spawn_scooby_snack(), spawn_scooby_snack()]
    return {"Name":"dogge", "Type":"Enemy", "Symbol":"D", "Xpoz":Xpoz
    , "Ypoz":Ypoz, "Walkable":False, "Inventory":inventory
    , "HP": 100, "MaxHP":100, "BaseDamage":20, "CriticalChance":10
    , "DodgeChance": 0, "Armor":0, "XpReward": 100}

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
    return {"Name": "Stick", "Type": "Usable", "CriticalChanceReward": 20, "Duration": 10}

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