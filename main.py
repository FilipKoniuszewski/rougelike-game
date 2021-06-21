import util
import engine
import ui
import ObjectGenerator

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!

    Returns:
    dictionary
    '''
    pass


def main():
    # player = create_player()
    # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)

    # util.clear_screen()
    # is_running = True
    # while is_running:
    #     engine.put_player_on_board(board, player)
    #     ui.display_board(board)

    #     key = util.key_pressed()
    #     if key == 'q':
    #         is_running = False
    #     else:
    #         pass
    #     util.clear_screen()


    board = engine.create_board(20,30)
    player = ObjectGenerator.spawn_player()
    engine.put_player_on_board(board, player)
    while True:
        util.clear_screen()
        ui.display_board(board)
        move_player(board, player)


 
def move_player(board, player):
    pressed_key = util.key_pressed()
    if pressed_key == "w":
        if player["Ypoz"] - 1 >= 0 and board[player["Ypoz"] - 1][player["Xpoz"]]["Walkable"]:
            board[player["Ypoz"] - 1][player["Xpoz"]] = player
            board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_floor()
            player["Ypoz"] -= 1
    elif pressed_key == "s":
        if player["Ypoz"] < len(board) - 1 and board[player["Ypoz"] + 1][player["Xpoz"]]["Walkable"]:
            board[player["Ypoz"] + 1][player["Xpoz"]] = player
            board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_floor()
            player["Ypoz"] += 1
    elif pressed_key == "d":
        if player["Xpoz"] < len(board[0]) - 1 and board[player["Ypoz"]][player["Xpoz"] + 1]["Walkable"]:
            board[player["Ypoz"]][player["Xpoz"] + 1] = player
            board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_floor()
            player["Xpoz"] += 1
    elif pressed_key == "a":
        if player["Xpoz"] - 1 >= 0 and board[player["Ypoz"]][player["Xpoz"] - 1]["Walkable"]:
            board[player["Ypoz"]][player["Xpoz"] - 1] = player
            board[player["Ypoz"]][player["Xpoz"]] = ObjectGenerator.spawn_floor()
            player["Xpoz"] -= 1
        

if __name__ == '__main__':
    main()
