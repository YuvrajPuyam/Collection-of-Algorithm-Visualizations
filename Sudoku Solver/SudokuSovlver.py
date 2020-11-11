from tkinter import *
from tkinter import messagebox


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
row = 0
col = 0
def findLocation(board, row, col):
    global board 
    global row, col
    for i in range(9):
        for j in range(9):
            if(board[i][j] == '.'):
                row = i
                col = j
                return True
    return False

def isValidRow(board,row,num):
    for i in range(9):
        if(board[row][i] == num):
            return False
    return True        

def isValidCol(board,col,num):
    for i in range(9):
        if(board[i][col] == num):
            return False
    return True

def isValidGrid(board,row,col,num):
    rowkey = row - row%3
    colkey = col - col%3
    for i in range(3):
        for j in range(3):
            if board[i+rowkey][j+colkey] == num:
                return False
    return True      

def isValid(board,row,col,num):
    return isValidRow(board,row,num) and isValidCol(board,col,num) and isValidGrid(board,row,col,num) 

def helper(board){
    if !findLocation(row,col):
        return True
}                 