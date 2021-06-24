import sys
import os
import random
import ui
import ObjectGenerator
import engine
EFFECTS = []
Kill_count = 0
Steps_count = 0
Critical_hits = 0
Nail_flag = False
Boss_stun = 0

def key_pressed():
    try:
        import tty, termios
    except ImportError:
        try:
            # probably Windows
            import msvcrt
        except ImportError:
            # FIXME what to do on other platforms?
            raise ImportError('getch not available')
        else:
            key = msvcrt.getch().decode('utf-8')
            return key
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch


def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')


def Attack_chances(attacker:dict,defender):
    tab_poss = []
    for x in range(2):
        random_value = random.randrange(1,101)
        tab_poss.append(random_value)
    if  tab_poss[0] <= defender["DodgeChance"]:
        ui.Information_board(f"{defender['Name']} dodged {attacker['Name']} attack")        
    else:
        if tab_poss[1] <= attacker["CriticalChance"]:
            global Critical_hits
            Critical_hits += 1
            ui.Information_board(f"{attacker['Name']} dealt critical damage: {attacker['BaseDamage']*2} to {defender['Name']}")
            defender["HP"] -= (attacker["BaseDamage"]*2)  
        else:
            defender["HP"] -= attacker["BaseDamage"]
            ui.Information_board(f"{attacker['Name']} dealt damage: {attacker['BaseDamage']} to {defender['Name']}")


def move_player(board, player):
    pressed_key = key_pressed()
    global Nail_flag
    if pressed_key == "w":
        if player["Ypoz"] - 1 >= 0:
            if board[player["Ypoz"] - 1][player["Xpoz"]]["Walkable"]:
                board[player["Ypoz"] - 1][player["Xpoz"]] = player
                if Nail_flag:
                    board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_nail()
                    Nail_flag = False
                else:
                    board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_floor()
                player["Ypoz"] -= 1
            elif board[player["Ypoz"] - 1][player["Xpoz"]]["Type"] == "Enemy":
                Attack_chances(player, board[player["Ypoz"] - 1][player["Xpoz"]])
                engine.CURRENT_ENEMY = board[player["Ypoz"] - 1][player["Xpoz"]]
            elif board[player["Ypoz"] - 1][player["Xpoz"]]["Name"] == "Exit" and player["Progress"]:
                return None
            else:
                return False
        else:
            return False
    elif pressed_key == "s":
        if player["Ypoz"] < len(board) - 1:
            if board[player["Ypoz"] + 1][player["Xpoz"]]["Walkable"]:
                board[player["Ypoz"] + 1][player["Xpoz"]] = player
                if Nail_flag:
                    board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_nail()
                    Nail_flag = False
                else:
                    board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_floor()
                player["Ypoz"] += 1
            elif board[player["Ypoz"] + 1][player["Xpoz"]]["Type"] == "Enemy":
                Attack_chances(player,board[player["Ypoz"] + 1][player["Xpoz"]])
                engine.CURRENT_ENEMY = board[player["Ypoz"] + 1][player["Xpoz"]]
            elif board[player["Ypoz"] + 1][player["Xpoz"]]["Name"] == "Exit" and player["Progress"]:
                return None
            else:
                return False
        else:
            return False
    elif pressed_key == "d":
        if player["Xpoz"] < len(board[0]) - 1:
            if board[player["Ypoz"]][player["Xpoz"] + 1]["Walkable"]:
                board[player["Ypoz"]][player["Xpoz"] + 1] = player
                if Nail_flag:
                    board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_nail()
                    Nail_flag = False
                else:
                    board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_floor()
                player["Xpoz"] += 1
            elif board[player["Ypoz"]][player["Xpoz"] + 1]["Type"] == "Enemy":
                Attack_chances(player,board[player["Ypoz"]][player["Xpoz"] + 1])
                engine.CURRENT_ENEMY = board[player["Ypoz"]][player["Xpoz"] + 1]
            elif board[player["Ypoz"]][player["Xpoz"] + 1]["Name"] == "Exit" and player["Progress"]:
                return None
            else:
                return False
        else:
            return False
    elif pressed_key == "a":
        if player["Xpoz"] - 1 >= 0:
            if board[player["Ypoz"]][player["Xpoz"] - 1]["Walkable"]:
                board[player["Ypoz"]][player["Xpoz"] - 1] = player
                if Nail_flag:
                    board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_nail()
                    Nail_flag = False
                else:
                    board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_floor()
                player["Xpoz"] -= 1
            elif board[player["Ypoz"]][player["Xpoz"] - 1]["Type"] == "Enemy":
                Attack_chances(player,board[player["Ypoz"]][player["Xpoz"] - 1])
                engine.CURRENT_ENEMY = board[player["Ypoz"]][player["Xpoz"] - 1]
            elif board[player["Ypoz"]][player["Xpoz"] - 1]["Name"] == "Exit" and player["Progress"]:
                return None
            else:
                return False
        else:
            return False
    elif pressed_key == "i":
        clear_screen()
        ui.inventory_menagment(player)
        return False    
    elif pressed_key == "u": # testy
        use_item(player, ObjectGenerator.spawn_cat_food())
        return False    
    elif pressed_key == "p":
        ui.display_stats(player)
        return False  
    else:
        return False
    return True

def enemy_activity(board, list_of_enemies, player):
    for enemy in list_of_enemies:
        success = False
        if enemy["Ypoz"] - 1 >= 0 and board[enemy["Ypoz"] - 1][enemy["Xpoz"]]["Type"] == "Player":
            Attack_chances(enemy, player)
        elif enemy["Ypoz"] < len(board) - 1 and board[enemy["Ypoz"] + 1][enemy["Xpoz"]]["Type"] == "Player":
            Attack_chances(enemy, player)
        elif enemy["Xpoz"] < len(board[0]) - 1 and board[enemy["Ypoz"]][enemy["Xpoz"] + 1]["Type"] == "Player":
            Attack_chances(enemy, player)   
        elif enemy["Xpoz"] - 1 >= 0 and board[enemy["Ypoz"]][enemy["Xpoz"] - 1]["Type"] == "Player":
            Attack_chances(enemy, player)   
        else:
            while not success:
                x = random.randint(0, 4)
                if x == 0:
                    if enemy["Ypoz"] - 1 >= 0 and board[enemy["Ypoz"] - 1][enemy["Xpoz"]]["Walkable"]:
                        board[enemy["Ypoz"] - 1][enemy["Xpoz"]] = enemy
                        board[enemy["Ypoz"]][enemy["Xpoz"]] = ObjectGenerator.spawn_floor()
                        enemy["Ypoz"] -= 1
                        success = True
                elif x == 1:
                    if enemy["Ypoz"] < len(board) - 1 and board[enemy["Ypoz"] + 1][enemy["Xpoz"]]["Walkable"]:
                        board[enemy["Ypoz"] + 1][enemy["Xpoz"]] = enemy
                        board[enemy["Ypoz"]][enemy["Xpoz"]] = ObjectGenerator.spawn_floor()
                        enemy["Ypoz"] += 1
                        success = True
                elif x == 2:
                    if enemy["Xpoz"] < len(board[0]) - 1 and board[enemy["Ypoz"]][enemy["Xpoz"] + 1]["Walkable"]:
                        board[enemy["Ypoz"]][enemy["Xpoz"] + 1] = enemy
                        board[enemy["Ypoz"]][enemy["Xpoz"]] = ObjectGenerator.spawn_floor()
                        enemy["Xpoz"] += 1
                        success = True
                elif x == 3:
                    if enemy["Xpoz"] - 1 >= 0 and board[enemy["Ypoz"]][enemy["Xpoz"] - 1]["Walkable"]:
                        board[enemy["Ypoz"]][enemy["Xpoz"] - 1] = enemy
                        board[enemy["Ypoz"]][enemy["Xpoz"]] = ObjectGenerator.spawn_floor()
                        enemy["Xpoz"] -= 1
                        success = True

def add_enemies(board, amount, list_of_enemies):
    for i in range(amount):
        temp = ObjectGenerator.spawn_dogge(random.randint(3,15),random.randint(3,15))
        engine.put_player_on_board(board, temp)
        list_of_enemies.append(temp)

def remove_dead_mobs(player, board, list_of_enemies):
    for mob in list_of_enemies:
        if mob["HP"] <= 0:
            ui.Information_board(f"{player['Name']} has defeated {mob['Name']}")
            global Kill_count
            Kill_count += 1
            for item in mob["Inventory"]:
                player["Inventory"].append(item)
            player["Experience"] += mob["XpReward"]
            board[mob["Ypoz"]][mob["Xpoz"]] = ObjectGenerator.spawn_floor()
            list_of_enemies.remove(mob)
            engine.CURRENT_ENEMY = {}


def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    added_items = {
    "FOOD":0,
    "WEPON":0,
    "ARMOR" :0,
    "SPECIAL ITEMS":0,} 

    inventory.update(added_items)

    add_to_inventory(inventory, added_items)


def use_item(player, item):
    global Nail_flag
    if "HpReward" in item:
        player["HP"] += item["HpReward"]
        if player["HP"] > player["MaxHP"]:
            player["HP"] = player["MaxHP"]
    elif "CriticalChanceReward" in item:
        player["CriticalChance"] += item["CriticalChanceReward"]
        # if player["CriticalChanceReward"] > 100:
        #     player["CriticalChanceReward"] = 100
        EFFECTS.append(["CriticalChance", item["Duration"], item["CriticalChanceReward"]])
    elif "DodgeChanceReward" in item:
        player["DodgeChance"] += item["DodgeChanceReward"]
        # if player["DodgeChanceReward"] > 100:
        #     player["DodgeChanceReward"] = 100
        EFFECTS.append(["DodgeChance", item["Duration"], item["DodgeChanceReward"]])
    elif "ArmorReward" in item:
        player["Armor"] += item["ArmorReward"]
        if player["DodgeChanceReward"] > 100:
            player["DodgeChanceReward"] = 100
        EFFECTS.append("ArmorChance", item["Duration"]), item["ArmorChanceReward"]
    elif "BaseDamageReward" in item:
        player["BaseDamage"] += item["BaseDamageReward"]
        EFFECTS.append(["BaseDamage", item["Duration"], item["BaseDamageReward"]])    
    elif item["Name"] == "Nail":
        Nail_flag = True

    


def spawn_boss(board, Xpoz, Ypoz, boss_list):
    # temp = ObjectGenerator.spawn_roof(Xpoz, Ypoz)
    # boss_list.append(temp)
    # board[Ypoz][Xpoz] = temp
    temp = ObjectGenerator.spawn_tire(Ypoz - 1, Xpoz - 1)
    boss_list.append(temp)
    board[Ypoz - 1][Xpoz - 1] = temp
    temp = ObjectGenerator.spawn_tire(Ypoz - 1, Xpoz + 1)
    boss_list.append(temp)
    board[Ypoz - 1][Xpoz + 1] = temp
    temp = ObjectGenerator.spawn_roof(Ypoz, Xpoz)
    boss_list.append(temp)
    board[Ypoz][Xpoz] = temp
    temp = ObjectGenerator.spawn_tire(Ypoz + 1, Xpoz - 1)
    boss_list.append(temp)
    board[Ypoz + 1][Xpoz - 1] = temp
    temp = ObjectGenerator.spawn_tire(Ypoz + 1, Xpoz + 1)
    boss_list.append(temp)
    board[Ypoz + 1][Xpoz + 1] = temp
    

def move_boss(player, board, boss_list):
    global Boss_stun
    attacked = hit_boss(player, board, boss_list)
    if not attacked:
        for item in boss_list:
            if item["Symbol"] == "O":
                Xmid = item["Xpoz"]
                Ymid = item["Ypoz"]
        direction = random.randint(0, 3)
        if Ymid > 2 and direction == 0:
            for part in boss_list:#move up
                if board[part["Ypoz"] - 1][part["Xpoz"]]["Name"] == "Nail":
                    Boss_stun = 10
                    ui.Information_board("Dog Catcher is stuned!")
                part["Ypoz"] -= 1
                board[part["Ypoz"]][part["Xpoz"]] = part
                board[part["Ypoz"] + 1][part["Xpoz"]] = ObjectGenerator.spawn_floor()
        if Xmid > 2 and direction == 1:
            for part in boss_list:#move left
                if board[part["Ypoz"]][part["Xpoz"] - 1]["Name"] == "Nail":
                    Boss_stun = 10
                    ui.Information_board("Dog Catcher is stuned!")
                part["Xpoz"] -= 1
                board[part["Ypoz"]][part["Xpoz"]] = part
                board[part["Ypoz"]][part["Xpoz"] + 1] = ObjectGenerator.spawn_floor()
        if Xmid < len(board[0]) - 3 and direction == 2:
            for part in boss_list:#move right
                if board[part["Ypoz"]][part["Xpoz"] + 1]["Name"] == "Nail":
                    Boss_stun = 10
                    ui.Information_board("Dog Catcher is stuned!")
                part["Xpoz"] += 1
                board[part["Ypoz"]][part["Xpoz"]] = part
                board[part["Ypoz"]][part["Xpoz"] - 1] = ObjectGenerator.spawn_floor()
        if Ymid < len(board) - 3 and direction == 3:
            for part in boss_list:#move down
                if board[part["Ypoz"] + 1][part["Xpoz"]]["Name"] == "Nail":
                    Boss_stun = 10
                    ui.Information_board("Dog Catcher is stuned!")
                part["Ypoz"] += 1
                board[part["Ypoz"]][part["Xpoz"]] = part
                board[part["Ypoz"] - 1][part["Xpoz"]] = ObjectGenerator.spawn_floor()

def hit_boss(player, board, boss_list):
    for part in boss_list:
        if board[part["Ypoz"] + 1][part["Xpoz"]]["Type"] == "Player" or board[part["Ypoz"] - 1][part["Xpoz"]]["Type"] == "Player":
            Attack_chances(part, player)
            return True
        elif board[part["Ypoz"]][part["Xpoz"] + 1]["Type"] == "Player" or board[part["Ypoz"]][part["Xpoz"] - 1]["Type"] == "Player":
            Attack_chances(part, player)
            return True
    return False

    





