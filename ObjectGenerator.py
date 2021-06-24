
import random

#characters

def labrador_character():
    inventory = [spawn_scooby_snack(), spawn_scooby_snack()]
    return {"Name":"labrador","Symbol":"L", "HP": 100, "BaseDamage":15, "CriticalChance":20
    , "DodgeChance": 20,"Type":"Player", "Xpoz":1, "Ypoz":1
    , "Walkable":False, "MaxHP":100, "Armor":0, "Level": 1, "Experience" : 0, "Inventory":inventory,
     "Atributes":1, "Progress":False}

def shiba_character():
    inventory = []
    return {"Name":"shiba", "Symbol":"S", "HP": 100, "BaseDamage":40, "CriticalChance":15
    , "DodgeChance": 20, "Type":"Player", "Xpoz":1, "Ypoz":1
    , "Walkable":False, "MaxHP":100, "Armor":0, "Level": 1, "Experience" : 0, "Inventory":inventory,
     "Atributes":0, "Progress":False}

def doberman_character():
    inventory = []
    return {"Name":"doberman", "Symbol":"D", "HP": 100, "BaseDamage":40, "CriticalChance":20
    , "DodgeChance": 15, "Type":"Player", "Xpoz":1, "Ypoz":1
    , "Walkable":False, "MaxHP":100, "Armor":0, "Level": 1, "Experience" : 0, "Inventory":inventory
    ,"Atributes":0, "Progress":False}

def mops_character():
    inventory = []
    return {"Name":"mops","Symbol":"M", "HP": 100, "BaseDamage":15, "CriticalChance":10
    , "DodgeChance": 15, "Type":"Player", "Xpoz":1, "Ypoz":1
    , "Walkable":False, "MaxHP":100, "Armor":0, "Level": 1, "Experience" : 0, "Inventory":inventory,
     "Atributes":0, "Progress":False}

def spawn_dogge(Xpoz, Ypoz):
    inventory = [spawn_scooby_snack(),spawn_dog_food()]
    return {"Name":"dogge", "Type":"Enemy", "Symbol":"D", "Xpoz":Xpoz
    , "Ypoz":Ypoz, "Walkable":False, "Inventory":inventory
    , "HP": 100, "Level": 1, "MaxHP":100, "BaseDamage":20, "CriticalChance":10
    , "DodgeChance": 0, "Armor":0, "XpReward": 300}

def spawn_rat(Xpoz, Ypoz):
    return {"Name":"rat", "Type":"Enemy", "Symbol":"R", "Xpoz":Xpoz
    , "Ypoz":Ypoz, "Walkable":False, "Inventory": package_of_items()
    , "HP": 100, "Level": 1, "MaxHP":100, "BaseDamage":20, "CriticalChance":10
    , "DodgeChance": 0, "Armor":0, "XpReward": 300}

def spawn_cat(Xpoz, Ypoz):
    inventory = []
    for i in range(random.randint(1,2)):
        inventory.append(random.choice([spawn_scooby_snack(), spawn_scooby_snack(), spawn_coffee_bean(), spawn_cat_food(), spawn_cat_food()]))
    return {"Name":"Stray cat", "Type":"Enemy", "Symbol":"C", "Xpoz":Xpoz
    , "Ypoz":Ypoz, "Walkable":False, "Inventory": inventory
    , "HP": 10, "Level": 2, "MaxHP":200, "BaseDamage":15, "CriticalChance":20
    , "DodgeChance": 40, "Armor":0, "XpReward": 300}

def spawn_boar(Xpoz, Ypoz):
    inventory = []
    for i in range(random.randint(1,2)):
        inventory.append(random.choice([spawn_scooby_snack(), spawn_scooby_snack(), spawn_coffee_bean(), spawn_cat_food(), spawn_cat_food()]))
    return {"Name":"Angry Boar", "Type":"Enemy", "Symbol":"B", "Xpoz":Xpoz
    , "Ypoz":Ypoz, "Walkable":False, "Inventory": inventory
    , "HP": 300, "Level": 5, "MaxHP":300, "BaseDamage":40, "CriticalChance":10
    , "DodgeChance": 20, "Armor":0, "XpReward": 1500}

def spawn_boar(Xpoz, Ypoz):
    inventory = []
    for i in range(random.randint(1,2)):
        inventory.append(random.choice([spawn_scooby_snack(), spawn_scooby_snack(), spawn_coffee_bean(), spawn_cat_food(), spawn_cat_food()]))
    return {"Name":"Boar", "Type":"Enemy", "Symbol":"B", "Xpoz":Xpoz
    , "Ypoz":Ypoz, "Walkable":False, "Inventory": inventory
    , "HP": 200, "Level": 2, "MaxHP":300, "BaseDamage":40, "CriticalChance":20
    , "DodgeChance": 0, "Armor":0, "XpReward": 340}

def package_of_items():
    package_of_items = [spawn_scooby_snack(),spawn_collar(),
    spawn_dog_food(),spawn_bone(),spawn_stick(),spawn_ball()]
    inventory = random.choices(package_of_items, weights = [1,1,1,1,1,1,1], k = 3)
    return inventory

#map

def spawn_exit():
    return {"Name":"Exit", "Type":"Map", "Symbol":"E", "Walkable":False}

def spawn_fence():
    return {"Name":"fence", "Type":"Map", "Symbol":"#", "Walkable":False}

def spawn_tree():
    return {"Name":"Tree", "Type":"Map", "Symbol":"Y", "Walkable":False}


def spawn_nail():
    return {"Name":"Nail", "Type":"Map", "Symbol":"X", "Walkable":False}
def spawn_floor():
    return {"Name":"Floor", "Type":"Map", "Symbol":" ", "Walkable":True}

def spawn_wall_horizontal():
    return {"Name":"Wall1", "Type":"Map", "Symbol":"═", "Walkable":False}

def spawn_wall_upright():
    return {"Name":"Wall2", "Type":"Map", "Symbol":"║", "Walkable":False}

def spawn_corners():
    return [{"Name":"corner1", "Type":"Map", "Symbol":"╔", "Walkable":False},
    {"Name":"corner2", "Type":"Map", "Symbol":"╗", "Walkable":False},
    {"Name":"corner3", "Type":"Map", "Symbol":"╚", "Walkable":False},
    {"Name":"corner4", "Type":"Map", "Symbol":"╝", "Walkable":False}]

def spawn_house():
    return [{"Name":"char0", "Type":"Map", "Symbol":"__", "Walkable":False},
    {"Name":"char1", "Type":"Map", "Symbol":"/", "Walkable":False},
    {"Name":"char2", "Type":"Map", "Symbol":"\\", "Walkable":False},
    {"Name":"char3", "Type":"Map", "Symbol":"-", "Walkable":False},
    {"Name":"char4", "Type":"Map", "Symbol":'"', "Walkable":False},
    {"Name":"char5", "Type":"Map", "Symbol":'_', "Walkable":False},
    {"Name":"char6", "Type":"Map", "Symbol":'|', "Walkable":False},
    {"Name":"char7", "Type":"Map", "Symbol":'~', "Walkable":False},
    {"Name":"char8", "Type":"Map", "Symbol":'^', "Walkable":False}]

def tree():
    return {"Name":"Floor", "Type":"Map", "Symbol":"Y", "Walkable":False}
#items 
def spawn_nail():
    return {"Name":"Nail", "Type":"Map", "Symbol":"╳", "Walkable":False}

def spawn_scooby_snack():
    return {"Name":"Scooby snack", "Type":"Consumable", "HpReward":20, "Duration": 1}

def spawn_collar():
    return {"Name": "Collar", "Type": "Cloth", "ArmorReward": 50, "Duration": 1}

def spawn_dog_food():
    return {"Name": "Dog food", "Type": "Consumable", "HpReward": 50,}

def spawn_cat_food():
    return {"Name": "Cat food", "Type": "Consumable", "HpReward": 30,}

def spawn_bone():
    return {"Name": "Bone", "Type": "Usable", "BaseDamageReward": 20, "DodgeChanceReward": -10, "Duration": 5}

def spawn_stick():
    return {"Name": "Stick", "Type": "Usable", "CriticalChanceReward": 20, "Duration": 10}

def spawn_coffee_bean():
    return {"Name": "Coffee bean", "Type": "Usable", "DodgeChanceReward": 10, "Duration": 15} #tu chciałam żeby całkowicie znikała możliwość uniku

def spawn_ball():
    return {"Name": "Ball", "Type": "Usable"}



#Atributes

def strength_atribute():
    return {"Name": "Strength", "Enchant": "BaseDamage+15"}
def vitality_atribute():
    return {"Name": "Vitality", "Enchant": "MaxHP+25"}
def speed_atribute():
    return {"Name": "Speed", "Enchant": "DodgeChance+5"}
def crit_atribute():
    return {"Name": "Critical", "Enchant": "CriticalChance+10"}


# Trophies

def spawn_cats_claw():
    return {"Name": "Cat's claw"}

def spawn_dead_mouse():
    return {"Name": "Dead mouse"}

def spawn_boar_horn():
    return {"Name": "Boar horn"}

Boss_hp = 500

def spawn_tire(Ypoz, Xpoz):
    return {"Name":"Dog catcher", "Symbol":"X", "Xpoz":Xpoz, "Ypoz":Ypoz, "Type":"Enemy", "HP":Boss_hp, "BaseDamage":30, "CriticalChance":15, "DodgeChance": 20
    , "XpReward": 100, "Walkable":False}

def spawn_hull(Ypoz, Xpoz):
    return {"Name":"Dog catcher", "Symbol":"#", "Xpoz":Xpoz, "Ypoz":Ypoz, "Type":"Enemy", "HP":Boss_hp, "BaseDamage":30, "CriticalChance":15, "DodgeChance": 20
    , "XpReward": 100, "Walkable":False}

def spawn_roof(Ypoz, Xpoz):
    return {"Name":"Dog catcher", "Symbol":"O", "Xpoz":Xpoz, "Ypoz":Ypoz, "Type":"Enemy", "HP":Boss_hp, "BaseDamage":30, "CriticalChance":15, "DodgeChance": 20
    , "XpReward": 100, "Walkable":False}

