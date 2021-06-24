global information_board
information_board = [] 

import os
import util
import time
import ObjectGenerator

def display_board(board):
    '''
    Displays complete game board on the screen

    Returns:
    Nothing
    '''
    output = ""
    for i in range(len(board)):
        for j in range(len(board[0])):
            output += board[i][j]["Symbol"]
        if i != len(board)-1:
            output += "\n"
    print(output)

def Information_board(info):
    information_board.insert(0,info)
    if len(information_board) > 5:
       information_board.pop(5)
  
def print_log():
    print("\n")
    for i in range(len(information_board) - 1, -1, -1):
        print(information_board[i])


# def print_table(inventory):
#     print(f"""
#     !BACKPACK!
#     -----------------
#     item name | type
#     -----------------""")
#     for item in inventory:
#         # for key, value in item["Name"], item["Type"]:
#         print(item["Name"], ' : ', item["Type"] ,)
#         print("-----------------")

#     util.key_pressed()

def display_stats(player):
    util.clear_screen()
    additional = 0
    table = ""
    table += "STATISTICS\n"
    table += f"""┌{20*'─'}┐\n"""
    for stat in player:
        if not stat in ["Symbol", "Type", "Xpoz", "Ypoz", "Walkable", "Inventory", "Atributes"]:
            for effect in util.EFFECTS:
                if effect[0] == stat:
                    additional += effect[2]
            if additional != 0:
                count_spaces = f"{player[stat] - additional}+{additional}"
                spaces = 20 - len(stat) - len(str(count_spaces))
                if stat != "Name":
                    table += f"""├{20*'─'}┤\n"""
                table += f"│{stat}{spaces*' '}{player[stat] - additional}+{additional}│\n"
                additional = 0
            else:
                spaces = 20 - len(stat) - len(str(player[stat]))
                if stat != "Name":
                    table += f"""├{20*'─'}┤\n"""
                table += f"│{stat}{spaces*' '}{player[stat]}│\n"
    table += f"""└{20*'─'}┘\n"""
    print(table)
    if player["Atributes"] != 0:
        print("""\n
    ┌─────────────────────────────────┐
    │You have new atributes. Press [g]│
    └─────────────────────────────────┘
        """)
    user_input = util.key_pressed()
    if user_input == "g":
        atributes(player)


def atributes(player):
        if util.key_pressed() == "g":
            util.clear_screen()
            enchant = 0
            while player["Atributes"] > 0:
                util.clear_screen()
                if enchant > 3:
                    enchant = 0
                elif enchant < 0:
                    enchant = 3
                print(display_atributes(player))
                print(f"\nDistribute your {player['Atributes']} points\n")
                print(display_atribute_to_distribute(enchant))
                print("""
Press [g] to choose this enchant
Press [d] to next enchant
Press [a] to previous enchant""")
                user_input = util.key_pressed()
                if user_input == "g":
                    if enchant == 0:
                        player["BaseDamage"] += 15
                        player['Atributes'] -= 1
                    elif enchant == 1:
                        player["MaxHP"] += 25
                        player['Atributes'] -= 1
                    elif enchant == 2:
                        player["DodgeChance"] += 5
                        player['Atributes'] -= 1
                    elif enchant == 3:
                        player["CriticalChance"] += 10
                        player['Atributes'] -= 1
                elif user_input == "d":
                    enchant += 1
                    continue      
                elif user_input == "a":
                    enchant -= 1
                    continue 
                else:
                    util.clear_screen()
                    break

def display_atributes(player):
    table = ""
    table += f"""┌{20*'─'}┐\n"""
    for stat in player:
        if not stat in ["Symbol", "Type", "Xpoz", "Ypoz", "Walkable", "Inventory","Atributes"]:
            spaces = 20 - len(stat) - len(str(player[stat]))
            if stat != "Name":
                table += f"""├{20*'─'}┤\n"""
            table += f"│{stat}{spaces*' '}{player[stat]}│\n"
    table += f"""└{20*'─'}┘\n"""
    return table

def display_atribute_to_distribute(enchant):
    table = ""
    table += f"┌{41*'─'}┐\n"
    if enchant == 0:
        type = ObjectGenerator.strength_atribute()
        spaces = 40 - len(type["Name"]) - len(type["Enchant"])
        table += f"│{type['Name']}{spaces*' '}│{type['Enchant']}│\n"
    elif enchant == 1:
        type = ObjectGenerator.vitality_atribute()
        spaces = 40 - len(type["Name"]) - len(type["Enchant"])
        table += f"│{type['Name']}{spaces*' '}│{type['Enchant']}│\n"
    elif enchant == 2:
        type = ObjectGenerator.speed_atribute()
        spaces = 40 - len(type["Name"]) - len(type["Enchant"])
        table += f"│{type['Name']}{spaces*' '}│{type['Enchant']}│\n"
    elif enchant == 3:
        type = ObjectGenerator.crit_atribute()
        spaces = 40 - len(type["Name"]) - len(type["Enchant"])
        table += f"│{type['Name']}{spaces*' '}│{type['Enchant']}│\n"
    table += f"└{41*'─'}┘\n"
    return table

def inventory_menagment(player):
    inx=1
    print("""
    ╔═════════╗	
    ║INVENTORY║
    ╚═════════╝ """)
    print(f"┌{20*'─'}┐")
    for item in player['Inventory']:
        spaces = 18 - len(item["Name"])
        if inx != 1:
            print(f"├{20*'─'}┤")
        if inx > 9:
            print(f"│{inx}│{item['Name']}{(spaces - 1)*' '}│")
        else:
            print(f"│{inx}│{item['Name']}{spaces*' '}│")
        inx+=1
    success=False
    print(f"└{20*'─'}┘")
    print("""
Press [number] to use item
Press [something else] to leave inventory""")
    while not success:
        user_input=input()
        if user_input.isdigit():
            if int(user_input)>len(player['Inventory']):
                break
            else:
                util.use_item(player,player['Inventory'][int(user_input)-1])
                player['Inventory'].pop(int(user_input)-1)
                success=True
        if user_input =='c':
            success=True
        else:
            break

def experience_level_check(player):
    if player["Experience"] >= player["Level"] * 500:
       player["Experience"] -= player["Level"] * 500
       player["Level"]+=1
       player["HP"] = player["MaxHP"]
       player["Atributes"]+=2
       Information_board(f"You entered level{player['Level']}")
    
        
    
        

    









