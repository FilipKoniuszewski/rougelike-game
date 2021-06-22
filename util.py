import sys
import os
import random
import ui
import ObjectGenerator
import engine
import winsound
EFFECTS = []


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
        ui.Information_board(f"{attacker['Name']} attacked but {defender['Name']} managed to dodge")        
    else:
        if tab_poss[1] <= attacker["CriticalChance"]:
            ui.Information_board(f"{attacker['Name']} managed to do Critical attack and dealed {attacker['BaseDamage']*2} damage to {defender['Name']}")
            defender["HP"] -= (attacker["BaseDamage"]*2)  
            winsound.Beep(250,100)
        else:
            defender["HP"] -= attacker["BaseDamage"]
            ui.Information_board(f"{attacker['Name']} managed to attack and dealed {attacker['BaseDamage']} damage to {defender['Name']}")
            winsound.Beep(200,100)
def move_player(board, player):
    pressed_key = key_pressed()
    if pressed_key == "w":
        if player["Ypoz"] - 1 >= 0:
            if board[player["Ypoz"] - 1][player["Xpoz"]]["Walkable"]:
                board[player["Ypoz"] - 1][player["Xpoz"]] = player
                board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_floor()
                player["Ypoz"] -= 1
                winsound.Beep(150,100)
            elif board[player["Ypoz"] - 1][player["Xpoz"]]["Type"] == "Enemy":
                Attack_chances(player, board[player["Ypoz"] - 1][player["Xpoz"]])
                engine.CURRENT_ENEMY = board[player["Ypoz"] - 1][player["Xpoz"]]
            else:
                return False
        else:
            return False
    elif pressed_key == "s":
        if player["Ypoz"] < len(board) - 1:
            if board[player["Ypoz"] + 1][player["Xpoz"]]["Walkable"]:
                board[player["Ypoz"] + 1][player["Xpoz"]] = player
                board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_floor()
                player["Ypoz"] += 1
                winsound.Beep(150,100)
            elif board[player["Ypoz"] + 1][player["Xpoz"]]["Type"] == "Enemy":
                Attack_chances(player,board[player["Ypoz"] + 1][player["Xpoz"]])
                engine.CURRENT_ENEMY = board[player["Ypoz"] + 1][player["Xpoz"]]
            else:
                return False
        else:
            return False
    elif pressed_key == "d":
        if player["Xpoz"] < len(board[0]) - 1:
            if board[player["Ypoz"]][player["Xpoz"] + 1]["Walkable"]:
                board[player["Ypoz"]][player["Xpoz"] + 1] = player
                board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_floor()
                player["Xpoz"] += 1
                winsound.Beep(150,100)
            elif board[player["Ypoz"]][player["Xpoz"] + 1]["Type"] == "Enemy":
                Attack_chances(player,board[player["Ypoz"]][player["Xpoz"] + 1])
                engine.CURRENT_ENEMY = board[player["Ypoz"]][player["Xpoz"] + 1]
            else:
                return False
        else:
            return False
    elif pressed_key == "a":
        if player["Xpoz"] - 1 >= 0:
            if board[player["Ypoz"]][player["Xpoz"] - 1]["Walkable"]:
                board[player["Ypoz"]][player["Xpoz"] - 1] = player
                board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_floor()
                player["Xpoz"] -= 1
                winsound.Beep(150,100)
            elif board[player["Ypoz"]][player["Xpoz"] - 1]["Type"] == "Enemy":
                Attack_chances(player,board[player["Ypoz"]][player["Xpoz"] - 1])
                engine.CURRENT_ENEMY = board[player["Ypoz"]][player["Xpoz"] - 1]
            else:
                return False
        else:
            return False
    elif pressed_key == "i":
        clear_screen()
        ui.print_table(player["Inventory"])
        return False    
    elif pressed_key == "u": # testy
        use_item(player, ObjectGenerator.spawn_stick())
        return False    
    elif pressed_key == "p": # testy
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
            winsound.Beep(300,100)
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
    if "HpReward" in item:
        player["HP"] += item["HpReward"]
        if player["HP"] > player["MaxHP"]:
            player["HP"] = player["MaxHP"]
    if "CriticalChanceReward" in item:
        player["CriticalChance"] += item["CriticalChanceReward"]
        EFFECTS.append(["CriticalChance", item["Duration"], item["CriticalChanceReward"]])


