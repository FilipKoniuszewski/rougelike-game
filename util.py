import sys
import os
import ObjectGenerator
import ui
import random
import engine


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


def move_player(board, player):
    pressed_key = key_pressed()
    if pressed_key == "w":
        if player["Ypoz"] - 1 >= 0:
            if board[player["Ypoz"] - 1][player["Xpoz"]]["Walkable"]:
                board[player["Ypoz"] - 1][player["Xpoz"]] = player
                board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_floor()
                player["Ypoz"] -= 1
            elif board[player["Ypoz"] - 1][player["Xpoz"]]["Type"] == "Enemy":
                input("attack")
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
            elif board[player["Ypoz"] + 1][player["Xpoz"]]["Type"] == "Enemy":
                input("attack")
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
            elif board[player["Ypoz"]][player["Xpoz"] + 1]["Type"] == "Enemy":
                input("attack")
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
            elif board[player["Ypoz"]][player["Xpoz"] - 1]["Type"] == "Enemy":
                input("attack")
            else:
                return False
        else:
            return False
    elif pressed_key == "i":
        clear_screen()
        ui.print_table(player["Inventory"])
        return False        
    else:
        return False
    return True

def enemy_activity(board, list_of_enemies):
    for enemy in list_of_enemies:
        success = False
        # if board[enemy["Ypoz"] - 1][enemy["Xpoz"]]

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



def add_to_inventory(inventory, added_items):
    """Add to the inventory dictionary a list of items from added_items."""
    added_items = {
    "FOOD":0,
    "WEPON":0,
    "ARMOR" :0,
    "SPECIAL ITEMS":0,} 

    inventory.update(added_items)

    add_to_inventory(inventory, added_items)
