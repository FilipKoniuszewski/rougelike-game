
import engine
import ObjectGenerator
import random
import util

def create_1st_map(list_of_enemies):
    board = engine.create_board(20,30, True)
    board[18][28] = ObjectGenerator.spawn_exit()
    for i in range(15):
        board[random.randint(3,15)][random.randint(3,25)] = ObjectGenerator.spawn_tree()
    for i in range(10):
        success = False
        while not success:
            x = random.randint(3,18)
            y = random.randint(3,18)
            if board[y][x]["Name"] == "Floor":
                temp = ObjectGenerator.spawn_rat(x,y)
                board[y][x] = temp
                list_of_enemies.append(temp)
                success = True
    return board

def create_2nd_map(list_of_enemies):
    board = engine.create_board(20,30)
    board[18][28] = ObjectGenerator.spawn_exit()
    for i in range(15):
        board[random.randint(3,17)][random.randint(3,27)] = ObjectGenerator.spawn_tree()
    for i in range(10):
        success = False
        while not success:
            x = random.randint(3,18)
            y = random.randint(3,18)
            if board[y][x]["Name"] == "Floor":
                temp = ObjectGenerator.spawn_cat(x,y)
                board[y][x] = temp
                list_of_enemies.append(temp)
                success = True
    return board


def create_3nd_map(list_of_enemies):
    board = engine.create_board(20,30)
    board[18][28] = ObjectGenerator.spawn_exit()
    for i in range(25):
        board[random.randint(3,17)][random.randint(3,27)] = ObjectGenerator.spawn_tree()
    temp = ObjectGenerator.spawn_boar(10, 10)
    list_of_enemies.append(temp)
    board[10][10] = temp
    
    return board

def create_boss_arena(boss_list):
    board = engine.create_board(20,30)
    util.spawn_boss(board, 10, 10, boss_list)
    return board
