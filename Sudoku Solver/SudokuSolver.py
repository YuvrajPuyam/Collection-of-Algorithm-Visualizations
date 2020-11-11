import time



board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]


def find_location(board,row, col):
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                row[0] = i
                col[0] = j
                return True
    return False


def is_valid_row(board,row, num):
    for i in range(9):
        if board[row[0]][i] == num:
            return False
    return True


def is_valid_col(board,col, num):
    for i in range(9):
        if board[i][col[0]] == num:
            return False
    return True


def is_valid_grid(board,row, col, num):
    row_key = row[0] - row[0] % 3
    col_key = col[0] - col[0] % 3
    for i in range(3):
        for j in range(3):
            if board[i + row_key][j + col_key] == num:
                return False
    return True


def is_valid(board,row, col, num):
    return is_valid_row(board,row, num) and is_valid_col(board,col, num) and is_valid_grid(board,row, col, num)


def helper(board,flag,changeVal):
    row, col = [0], [0]
    if not find_location(board,row, col):
        return True
    for i in range(1, 10):
        if is_valid(board,row, col, str(i)):
            board[row[0]][col[0]] = str(i)

            if flag == 1:
                changeVal(row[0],col[0],str(i))
                time.sleep(0.01)     
                 
            if helper(board,flag,changeVal):
                return True 
            board[row[0]][col[0]] = '.'
            
                
    return False


def solve_sudoku(board,flag,changeVal):
     ans = helper(board,flag,changeVal)
     return ans
     
    

   


