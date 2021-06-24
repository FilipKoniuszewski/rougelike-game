import MapCreator
import dialogue
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


def play_map(player, board, list_of_enemies):
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
        ui.experience_level_check(player)
        if len(list_of_enemies) == 0:
            player["Progress"] = True
        while not success:
            util.clear_screen()
            print(engine.display_statistics(player))
            print(engine.display_current_enemy())
            ui.display_board(board)
            ui.print_log()
            success = util.move_player(board, player)
            if success == None:
                return True
        if enemy_turn:
            util.enemy_activity(board, list_of_enemies, player)
            if player["HP"] <= 0:
                return False
            enemy_turn = False
        else:
            enemy_turn = True


def game_loop():
    player = engine.create_player()
    dialogue.dialogue_with_Benek(player) # poprawić imię 
    list_of_enemies = []
    board = MapCreator.create_1st_map(list_of_enemies)
    success = play_map(player, board, list_of_enemies)
    if success:
        dialogue.second_dialogue_with_Benek(player)
        dialogue.waiting_screen(dialogue.frames_2)
        dialogue.third_dialogue_with_Benek(player)
        dialogue.waiting_screen(dialogue.frames)
        dialogue.dialogue_with_cat(player)
        player["Inventory"].append(ObjectGenerator.spawn_dog_food())
        player["Progress"] = False
        list_of_enemies = []
        board = MapCreator.create_2nd_map(list_of_enemies)
        board[1][1] = player
        player["Xpoz"] = 1
        player["Ypoz"] = 1
        success = play_map(player, board, list_of_enemies)
        if success:
            dialogue.second_dialogue_with_cat(player)
            dialogue.waiting_screen(dialogue.cat_frames)
            dialogue.dialogue_with_boar(player)
            player["Progress"] = False
            board = MapCreator.create_3nd_map(list_of_enemies)
            board[1][1] = player
            player["Xpoz"] = 1
            player["Ypoz"] = 1
            success = play_map(player, board, list_of_enemies)
            if success:
                player["Progress"] = False
                boss_list = []
                board = MapCreator.create_boss_arena(boss_list)
                board[1][1] = player
                player["Xpoz"] = 1
                player["Ypoz"] = 1
                for i in range(4):
                    player["Inventory"].append(ObjectGenerator.spawn_nail())
                enemy_turn = False
                while player["HP"] > 0:
                    util.clear_screen()
                    print(engine.display_statistics(player))
                    print(engine.display_current_enemy())
                    ui.display_board(board)
                    ui.print_log()
                    success = False
                    shuffle_effects(player)
                    ui.experience_level_check(player)
                    if boss_list[0]["HP"] <= 0:
                        util.clear_screen()
                        print(engine.display_end_screen(player, True))
                        util.key_pressed()
                        break
                    if util.Boss_stun > 0:
                        util.Boss_stun -= 1
                        if util.Boss_stun == 0:
                            ui.Information_board("Dog Catcher is not stuned anymore!")
                    while not success:
                        util.clear_screen()
                        print(engine.display_statistics(player))
                        print(engine.display_current_enemy())
                        ui.display_board(board)
                        ui.print_log()
                        success = util.move_player(board, player)
                    if enemy_turn:
                        if util.Boss_stun <= 0:
                            util.move_boss(player, board, boss_list)
                        if player["HP"] <= 0:
                            util.clear_screen()
                            print(engine.display_end_screen(player))
                        enemy_turn = False
                    else:
                        enemy_turn = True
            else:
                util.clear_screen()
                print(engine.display_end_screen(player))

        else:
            util.clear_screen()
            print(engine.display_end_screen(player))
    else:
        util.clear_screen()
        print(engine.display_end_screen(player))



if __name__ == '__main__':
    user_input = "y"
    while user_input.lower() == "y":
        util.clear_screen()
        game_loop()
        input("Do you want to play again? (y/n)")


