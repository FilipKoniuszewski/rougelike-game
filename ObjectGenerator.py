
def spawn_player():
    return {"Name":"player", "Type":"Player", "Symbol":"@", "Xpoz":1, "Ypoz":1, "Walkable":False}


def spawn_dogge(Xpoz, Ypoz):
    return {"Name":"dogge", "Type":"Enemy", "Symbol":"D", "Xpoz":Xpoz, "Ypoz":Ypoz, "Walkable":False}




def spawn_floor():
    return {"Name":"Floor", "Type":"Map", "Symbol":".", "Walkable":True}