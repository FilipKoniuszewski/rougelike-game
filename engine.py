import ObjectGenerator
import util
import time
import ui


def create_board(width, height):
    '''
    Creates a new game board based on input parameters.

    Args:
    int: The width of the board
    int: The height of the board

    Returns:
    list: Game board
    '''
    board = []
    for i in range(width):
        board.append([])
        for j in range(height):
            board[i].append(ObjectGenerator.spawn_floor())
    return board

def put_player_on_board(board, player):
    '''
    Modifies the game board by placing the player icon at its coordinates.

    Args:
    list: The game board
    dictionary: The player information containing the icon and coordinates

    Returns:
    Nothing
    '''
    board[player["Ypoz"]][player["Xpoz"]] = player

def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    type = 0
    while True:
        print(""" \nCHOOSE YOUR CHARACTER: \n""")
        if type == 0:
            character_type = ObjectGenerator.labrador_character()
        elif type == 1:
            character_type = ObjectGenerator.shiba_character()
        elif type == 2:
            character_type = ObjectGenerator.doberman_character()
        elif type == 3:
            character_type = ObjectGenerator.mops_character()
        print(create_character_class_as_table(character_type))
        player_input = input("""
Press [c] choose this character
Press [n] next character
Press [p] previous character\n""").lower()
        if player_input == 'c':
            util.clear_screen()
            return character_type
        elif player_input == 'n':
            type += 1
            if type < 4:
                util.clear_screen()
                continue
            else:
                type = 0
                util.clear_screen()
                continue
        elif player_input == "p":
            type -= 1
            if type >= 0:
                util.clear_screen()
                continue
            else:
                type = 3
                util.clear_screen()
                continue
        else:
            util.clear_screen()
            print("Invalid type\n")
            time.sleep(1.5)
            continue

def create_character_class_as_table(character_type):
    statistics = dict()
    table = ""
    for element in character_type:
        if len(statistics) > 5:
            break
        if element != "Name":
            statistics[element] = character_type[element]
    table += f"{character_type['Name'].upper()}\n"
    outside_edges = 25*"="
    table += f"{outside_edges}"
    for i in statistics.items():
        space_before_values = 8 - len(str(i[1]))
        space_after_key = 14 - len(i[0])
        table += f"\n|{i[0]}{' '*space_after_key}|{' '*space_before_values}{str(i[1])}|"
    table += f"\n{outside_edges}"
    return table



