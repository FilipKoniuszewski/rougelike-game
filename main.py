import util
import engine
import ui
import ObjectGenerator
import random
import time
import os
import winsound

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

BOARD_WIDTH = 30
BOARD_HEIGHT = 20

# ["EffectName", turnsLeft, value]

def shuffle_effects(player):
    to_pop = []
    for effect in util.EFFECTS:
        effect[1] -= 1
        if effect[1] == 0:
            player[effect[0]] -= effect[2]
            to_pop.append(effect)
    for effect in to_pop:
        util.EFFECTS.remove(effect)

def move_boss(player, board, boss_list):
    attacked = hit_boss(player, board, boss_list)
    if not attacked:
        for item in boss_list:
            if item["Symbol"] == "O":
                Xmid = item["Xpoz"]
                Ymid = item["Ypoz"]
        direction = random.randint(0, 3)
        if Ymid > 2 and direction == 0:
            for part in boss_list:#move up
                part["Ypoz"] -= 1
                board[part["Ypoz"]][part["Xpoz"]] = part
                board[part["Ypoz"] + 1][part["Xpoz"]] = ObjectGenerator.spawn_floor()
        if Xmid > 2 and direction == 1:
            for part in boss_list:#move left
                part["Xpoz"] -= 1
                board[part["Ypoz"]][part["Xpoz"]] = part
                board[part["Ypoz"]][part["Xpoz"] + 1] = ObjectGenerator.spawn_floor()
        if Xmid < len(board[0]) - 3 and direction == 2:
            for part in boss_list:#move right
                part["Xpoz"] += 1
                board[part["Ypoz"]][part["Xpoz"]] = part
                board[part["Ypoz"]][part["Xpoz"] - 1] = ObjectGenerator.spawn_floor()
        if Ymid < len(board) - 3 and direction == 3:
            for part in boss_list:#move down
                part["Ypoz"] += 1
                board[part["Ypoz"]][part["Xpoz"]] = part
                board[part["Ypoz"] - 1][part["Xpoz"]] = ObjectGenerator.spawn_floor()

def hit_boss(player, board, boss_list):
    for part in boss_list:
        if board[part["Ypoz"] + 1][part["Xpoz"]]["Type"] == "Player" or board[part["Ypoz"] - 1][part["Xpoz"]]["Type"] == "Player":
            util.Attack_chances(part, player)
            return True
        elif board[part["Ypoz"]][part["Xpoz"] + 1]["Type"] == "Player" or board[part["Ypoz"]][part["Xpoz"] - 1]["Type"] == "Player":
            util.Attack_chances(part, player)
            return True
    return False

    
    

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
    # util.add_enemies(board, 3, list_of_enemies)
    boss_list = []
    util.spawn_boss(board, 10, 10, boss_list)
    enemy_turn = False
    while player["HP"] > 0:
        util.clear_screen()
        print(engine.display_statistics(player))
        print(engine.display_current_enemy())
        ui.display_board(board)
        ui.print_log()
        success = False
        shuffle_effects(player)
        util.remove_dead_mobs(player, board, list_of_enemies)
        while not success:
            util.clear_screen()
            print(engine.display_statistics(player))
            print(engine.display_current_enemy())
            ui.display_board(board)
            ui.print_log()
            success = util.move_player(board, player)
        if enemy_turn:
            util.enemy_activity(board, list_of_enemies, player)
            move_boss(player, board, boss_list)
            if player["HP"] <= 0:
                util.clear_screen()
                print(engine.display_end_screen(player))
            enemy_turn = False
        else:
            enemy_turn = True


if __name__ == '__main__':
    main()


