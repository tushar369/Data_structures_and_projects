sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 7],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]


def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) 
                #empty position (row,col)

    return None


def valid(num, pos, board):
    #check row
    for i in range(len(board)):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    #check 3x3 box         
    box_x = pos[0]//3
    box_y = pos[1]//3

    for i in range(box_x*3, box_x*3 + 3):
        for j in range(box_y*3, box_y*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    found_position = findEmpty(board)
    if found_position: 
        row, col = found_position
    else:
        return True    

    for i in range(1, 10):
        if valid(i, (row, col), board):
            board[row][col] = i

            if solve(board):
                return True
            board[row][col] = 0
            
    return False    


def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')
        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')
            print(str(board[i][j]) + ' ' , end='')   
        print()     


printBoard(sudoku_board)
solve(sudoku_board)
print('\n\n')
printBoard(sudoku_board)



