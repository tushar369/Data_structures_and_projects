empty_board = [['-', '-', '-'],
               ['-', '-', '-'],
               ['-', '-', '-']]
board_is_empty = True
turn = 'X'


def display_board(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if j == 1 or j == 2:
                print(' | ', end='')
            print(board[i][j], end='')
        print()    


def check_board(board, pos):
    #It checks the winner
    #check row
    pos_row = board[pos[0]]
    if ['X', 'X', 'X'] == pos_row or ['O', 'O', 'O'] == pos_row:
        return True

    #check col
    pos_col = []
    for i in range(len(board)):
        if i != pos[1]:
            pos_col.append(board[i][pos[1]])
    pos_col.append(pos)        
    if ['X', 'X', 'X'] == pos_col or ['O', 'O', 'O'] == pos_col:
        return True

    #check diagonal
    diagnol_positions = [(0, 0), (1, 1), (2, 2), (2, 0), (0, 2)] 
    diagnol_1 = [board[0][0], board[1][1], board[2][2]]
    diagnol_2 = [board[2][0], board[1][1], board[0][2]]

    if pos in diagnol_positions:
        if ['X', 'X', 'X'] == diagnol_1 or ['O', 'O', 'O'] == diagnol_1:
            return True
    if pos in diagnol_2:
        if ['X', 'X', 'X'] == diagnol_2 or ['O', 'O', 'O'] == diagnol_2:
            return True 

    return None         

def check_tie(board):
    if '-' not in board[0] and '-' not in board[1] and '-' not in board[2]:
        return True        

# choosing the position
def move():
    move_row = input(f'Choose a row(1, 2, 3) player {turn}: ')
    move_row = int(move_row) - 1
    move_col = input(f'Choose a col(1, 2, 3) player {turn}: ')
    move_col = int(move_col) - 1
    return (move_row, move_col)


def move_validation(board, move):
    if board[move[0]][move[1]] == '-':
        return True
    return False



def flip_turn(turn):
    if turn == 'X':
        return 'O'
    else:
        return 'X'    


def play_game(board):
    global board_is_empty
    global turn
    display_board(board)
    if board_is_empty:
        turn = 'X'
        board_is_empty = False
    else:
        turn = flip_turn(turn)

    while True:    
        row, col = move()
        if move_validation(board, (row, col)):
            break
        
    board[row][col] = turn

    if check_tie(board):
        display_board(board)
        print("It's a tie")  
        return True 

    if check_board(board, (row, col)):
        display_board(board)
        print(f"{turn} won !!")
        return True
    else:
        play_game(board) 

        
play_game(empty_board)    