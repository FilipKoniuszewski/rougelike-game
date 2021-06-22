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
    print(information_board)
    information_board.insert(0,info)
    if len(information_board) > 5:
       information_board.pop(5)
  

def print_log():
    for line in information_board:
        print(line)

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

