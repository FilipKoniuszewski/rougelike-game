global information_board
information_board = [] 

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
    if len(information_board) > 5:
       information_board.pop(0)
  

def print_log():
    for line in information_board:
        print(line)



