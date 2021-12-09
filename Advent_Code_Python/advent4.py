import pandas as pd, numpy as np
import os 
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def parseInput(filename):

    file = open(filename)
    start = True
    prev_f = ""
    values = []
    board = []

    for f in file:
        if start:
            values.append(f[:-2])
            start = False
        else:
            if f!= "\n":
                board.append(f[:-1])
            else:
                values.append(board)
                board = []

    numbers = values[0]
    n_numbers = []
    ns = numbers.split(",")

    #Clean Called Numbers
    for n in ns:
        try:
            n = int(n)
            n_numbers.append(n)
        except:
            pass

    #Clean Boards
    values = values[2::]
    n_vals = []
    for board in values:
        new_board = []
        for row in board:
            new_row = []
            numbers = row.split(" ")
            for n in numbers:
                try:
                    n = int(n)
                    new_row.append(n)
                except:
                    pass
            new_board.append(new_row)
        n_vals.append(new_board)

    return n_numbers,n_vals

n_numbers,n_vals = parseInput("input4.txt")

def checkWinner(board,called_nums):
    for i in range(len(board)):
        col_total = 0
        row_total = 0
        for j in range(len(board)):
            if board[i][j] in called_nums:
                col_total +=1
            if board[j][i] in called_nums:
                row_total +=1
            if col_total == 5 or row_total == 5:
                return True
    return False
    
def findWinner(numbers,boards):
    called_nums=[]
    for num in numbers:
        called_nums.append(num)
        for board in boards:
            winner = checkWinner(board,called_nums)
            if winner:
                print(board)
                unmarked_sum = 0
                for i in range(len(board)):
                    for j in range(len(board)):
                        if board[i][j] not in called_nums:
                            unmarked_sum += board[i][j]
                final_score = unmarked_sum * num
                return final_score
    return False

called_nums = []

f_score = findWinner(n_numbers,n_vals)
print(f_score)

def findLastWinner(numbers,boards):
    called_nums=[]
    for num in numbers:
        called_nums.append(num)
        for board in boards:
            winner = checkWinner(board,called_nums)
            if winner and len(boards) > 1:
                boards.remove(board)
            elif winner:
                print(board)
                unmarked_sum = 0
                for i in range(len(board)):
                    for j in range(len(board)):
                        if board[i][j] not in called_nums:
                            unmarked_sum += board[i][j]
                final_score = unmarked_sum * num
                return final_score
    return False

f_loser_score = findLastWinner(n_numbers,n_vals)
print(f_loser_score)