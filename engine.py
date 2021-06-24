import ObjectGenerator
import util
import time
import ui

CURRENT_ENEMY = {}


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
    for i in range(1,29):
        board[0][i] = ObjectGenerator.spawn_wall_horizontal()
        board[19][i] = ObjectGenerator.spawn_wall_horizontal()
    for i in range(1,19):
         board[i][0] = ObjectGenerator.spawn_wall_upright()
         board[i][29] = ObjectGenerator.spawn_wall_upright()
    corners = ObjectGenerator.spawn_corners()
    board[0][0] = corners[0]
    board[0][29] = corners[1]
    board[19][0] = corners[2]
    board[19][29] = corners[3]

    
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
        print("""
Press [e] choose this character
Press [d] next character
Press [a] previous character\n""")
        user_input = util.key_pressed()
        if user_input == 'e':
            player_input = input("Put name of your character: ")
            character_type["Name"] = player_input
            util.clear_screen()
            return character_type
        elif user_input == 'd':
            type += 1
            if type < 4:
                util.clear_screen()
                continue
            else:
                type = 0
                util.clear_screen()
                continue
        elif user_input == "a":
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
            time.sleep(1)
            util.clear_screen()
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
    outside_edges1 = 14*"═"
    outside_edges2 = 8*"═"
    table += f"╔{outside_edges1}╦{outside_edges2}╗"
    for i in statistics.items():
        space_before_values = 8 - len(str(i[1]))
        space_after_key = 14 - len(i[0])
        table += f"\n║{i[0]}{' '*space_after_key}║{' '*space_before_values}{str(i[1])}║"
    table += f"\n╚{outside_edges1}╩{outside_edges2}╝"
    return table


def display_statistics(player):
    HEADERS = f"""
╔══════════╦══════════╦══════════╦══════════╗
║Name      ║HP        ║Level     ║Experience║
╠══════════╬══════════╬══════════╬══════════╣ \n"""
    table = ""
    table += HEADERS
    for element in player:
        if element == "Name":
            spaces = 10 - len(player[element])
            table += f"║{player[element]}{' '*spaces}║"
        elif element == "HP":
            spaces = 10 - len(str(player[element]))
            table += f"{player[element]}{' '*spaces}"
        elif element == "Level":
            spaces = 10 - len(str(player[element]))
            table += f"║{player[element]}{' '*spaces}"
        elif element == "Experience":
            spaces = 10 - len(str(player[element]))
            table += f"║{player[element]}{' '*spaces}║"
    table += "\n╚══════════╩══════════╩══════════╩══════════╝"
    return table

def display_current_enemy():
    if CURRENT_ENEMY == {}:
        table = "\n\n\n\n\n"
    else:
        HEADERS = f"""
╔══════════╦══════════╦══════════╦══════════╗
║Name      ║HP        ║Level     ║XP Reward ║
╠══════════╬══════════╬══════════╬══════════╣ \n"""
        table = ""
        table += HEADERS
        for element in CURRENT_ENEMY:
            if element == "Name":
                spaces = 10 - len(CURRENT_ENEMY[element])
                table += f"║{CURRENT_ENEMY[element]}{' '*spaces}║"
            elif element == "HP":
                spaces = 10 - len(str(CURRENT_ENEMY[element]))
                table += f"{CURRENT_ENEMY[element]}{' '*spaces}"
            elif element == "Level":
                spaces = 10 - len(str(CURRENT_ENEMY[element]))
                table += f"║{CURRENT_ENEMY[element]}{' '*spaces}"
            elif element == "XpReward":
                spaces = 10 - len(str(CURRENT_ENEMY[element]))
                table += f"║{CURRENT_ENEMY[element]}{' '*spaces}║"
        table += "\n╚══════════╩══════════╩══════════╩══════════╝"
    return table
    

def display_end_screen(player):
    counters = [util.KILL_COUNT,util.STEPS_COUNT,util.CRITICAL_HITS]
    table = ""
    table += "YOU LOST THE GAME\nSTATISTICS\n"
    table += "╔══════════╦══════════╗\n"
    for element in player:
        if element == "Name":
            spaces = 10 - len(str(player[element]))
            table += f"║Name{6*' '}║{player[element]}{' '*spaces}║\n"
            table += f"╠{10*'═'}╬{10*'═'}╣\n"
        elif element == "Level":
            spaces = 10 - len(str(player[element]))
            table += f"║Level{5*' '}║{player[element]}{' '*spaces}║\n"
            table += f"╠{10*'═'}╬{10*'═'}╣\n"
        elif element == "Experience":
            spaces = 10 - len(str(player[element]))
            table += f"║Experience║{player[element]}{' '*spaces}║\n"
            table += f"╠{10*'═'}╬{10*'═'}╣\n"
    for info in range(len(counters)):
        if info == 0:
            spaces = 10 - len(str(util.KILL_COUNT))
            table += f"║Kills{5*' '}║{util.KILL_COUNT}{' '*spaces}║\n"
            table += f"╠{10*'═'}╬{10*'═'}╣\n"
        elif info == 1:
            spaces = 10 - len(str(util.STEPS_COUNT))
            table += f"║Steps{5*' '}║{util.STEPS_COUNT}{' '*spaces}║\n"
            table += f"╠{10*'═'}╬{10*'═'}╣\n"
        else:
            spaces = 10 - len(str(util.CRITICAL_HITS))
            table += f"║Criticals{1*' '}║{util.CRITICAL_HITS}{' '*spaces}║\n"
    table += "╚══════════╩══════════╝"
    return table




