import util
import engine
import ui
import ObjectGenerator
import random
import time
import os

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20


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
    player = engine.create_player()
    engine.put_player_on_board(board, player)
    # engine.put_player_on_board(board, ObjectGenerator.spawn_dogge(5,3))
    list_of_enemies = []
    util.add_enemies(board, 3, list_of_enemies)

    enemy_turn = False
    while True:
        util.clear_screen()
        ui.display_board(board)
        ui.print_log()
        success = False
        while not success:
            util.clear_screen()
            ui.display_board(board)
            ui.print_log()
            success = util.move_player(board, player)
        if enemy_turn:
            util.enemy_activity(board, list_of_enemies)
            enemy_turn = False
        else:
            enemy_turn = True


if __name__ == '__main__':

    # DOG = ObjectGenerator.spawn_dogge(1,2)["Name"]
    # ui.Information_board(f"dupa {DOG}")
    # ui.Information_board("cyce")
    # ui.Information_board("cyce")
    # ui.Information_board("cyce")
    # ui.Information_board("cyce")
    # ui.Information_board("cyce")
    # ui.Information_board("cyce")

    # ui.print_log()
    main()
