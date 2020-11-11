from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import copy
from functools import partial
from SudokuSolver import solve_sudoku
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

#functionsc
def inputVal(row,col):
    answer = simpledialog.askstring("Input", "Enter Value", parent=root)
    print(answer)
    if int(answer) in range(1,10):
        cells[(row,col)].config(text=answer)
        board[row][col] = answer
        print(board)

def changeVal(row,col,val):
    # print(row,col,val)
    cells[(row,col)].config(text=val)
    root.update_idletasks()

def Generate():
    for row in range(9):
        for col in range(9):
            val = (board[row][col])
            if val != '.':
                cells[(row,col)].config(text=val,state=DISABLED) 

def Check(board,flag,Generate):
    board_copy = copy.deepcopy(board)
    ans = solve_sudoku(board_copy,flag,changeVal)
    if ans :messagebox.showinfo('Result','Correct Placement')
    else: messagebox.showwarning('Result','Wrong Placement')

def solve(board,flag,changeVal):
    solve_sudoku(board,flag,changeVal)
    messagebox.showinfo('Result','Sudoku Solved!')

root = Tk()
root.title('Sudoku')

# dividing into three parts
label = Label(root,text='SUDOKU SOLVER', font="times 15")
label.grid(row=0,column=0)

canvas = Canvas(root, width=600, height=380, bg='white')
canvas.grid(row=1,column=0, padx=10,pady=5)

UI_frame = Canvas(root, width=600, height=30)
UI_frame.grid(row=2,column=0,padx=10,pady=5)

cells = {}

#Sudoku Canvas
for row in range(9):
    for column in range(9):
        cell = Button(canvas,width=5,height=2,bg='#B392AC')
        cell.grid(row=row,column=column)
        if (row in range(3,6) and column not in range(3,6)) or column in range(3,6) and row not in range(3,6):
            cell.config(bg='#FFD3BA')
        cells[(row,column)] = cell
        cells[(row,column)].config(command=lambda row1=row,col1=column :inputVal(row1,col1))

generate = Button(UI_frame,width=20,height=3,text='Generate',command=lambda:Generate())
generate.grid(row=0,column=0,padx=5)

check = Button(UI_frame,width=20,height=3,text='Check',command= lambda:Check(board,0,changeVal))
check.grid(row=0,column=1,padx=5)

Solve = Button(UI_frame,width=20,height=3,text='Solve',command=lambda:solve(board,1,changeVal))
Solve.grid(row=0,column=2,padx=5)

root.mainloop()