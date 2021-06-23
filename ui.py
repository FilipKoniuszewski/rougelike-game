global information_board
information_board = [] 

import os
import util

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
    for i in range(len(information_board) - 1, -1, -1):
        print(information_board[i])

    # for line in information_board:
    #     print(line)

def print_table(inventory):
    print(f"""
    !BACKPACK!
    -----------------
    item name | type
    -----------------""")
    for item in inventory:
        # for key, value in item["Name"], item["Type"]:
        print(item["Name"], ' : ', item["Type"] ,)
        print("-----------------")

    os.system('pause')

def display_stats(player):
    util.clear_screen()
    additional = 0
    for stat in player:
        if not stat in ["Symbol", "Type", "Xpoz", "Ypoz", "Walkable", "Inventory"]:
            for effect in util.EFFECTS:
                if effect[0] == stat:
                    additional += effect[2]
                    # print(f"{stat} --- {player[stat] - effect[2]} + {effect[2]}")
                    # break
            if additional != 0:
                print(f"{stat} --- {player[stat] - additional} + {additional}")
                additional = 0
            else:
                print(f"{stat} --- {player[stat]}")
    util.key_pressed()
