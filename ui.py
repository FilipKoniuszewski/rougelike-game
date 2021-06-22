global information_board
information_board = [] 

import os

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
        output += "\n"
    print(output)

def Information_board(info):
    if len(information_board)<0:
       information_board.append(info)
    else:
        information_board.insert(0,info)
    for x in range(len(information_board)):
        if x >= 0 and x < 5:
            print(information_board[x])

def display_inventory(inventory):
    """Display the contents of the inventory in a simple way."""

    inventory = {}


    display_inventory(inventory) # stack overflow


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




