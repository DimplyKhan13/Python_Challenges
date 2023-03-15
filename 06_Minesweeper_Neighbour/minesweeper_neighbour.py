###
#
# https://edabit.com/challenge/v2eHXTn2qobw2WYJP
#
# Minesweeper Number of Neighbouring Mines
# Create a function that takes a list representation of a Minesweeper board, and returns another board where the value of each cell is the amount of its neighbouring mines.
#
# Examples
# The input may look like this:
#
# [
#   [0, 1, 0, 0],
#   [0, 0, 1, 0],
#   [0, 1, 0, 1],
#   [1, 1, 0, 0]
# ]
# The 0 represents an empty space . The 1 represents a mine.
# 
# You will have to replace each mine with a 9 and each empty space with the number of adjacent mines, the output will look like this:
#
# [
#   [1, 9, 2, 1],
#   [2, 3, 9, 2],
#   [3, 9, 4, 9],
#   [9, 9, 3, 1]
# ]
# Notes
# Since in the output the numbers 0-8 are used to determine the amount of adjacent mines, the number 9 will be used to identify the mines instead.
# A wikipedia page explaining how Minesweeper works is available in the Resources tab.
#
###

def minesweeper_numbers(board):
    solution = []
    for row in range(len(board)):
        solution.append([])
        for col in range(len(board[row])):
            if board[row][col] == 1:
                solution[row].append(9)
            else:
                neighbours = 0
                for mod_row in range(-1, 2, 1):
                    check_row = row + mod_row
                    if check_row >= 0 and check_row < len(board):
                        for mod_col in range(-1, 2, 1):
                            check_col = col + mod_col
                            if check_col >= 0 and check_col < len(board[check_row]):
                                if board[check_row][check_col]:
                                    neighbours += 1                         
                
                
                solution[row].append(neighbours)
    return solution

def minesweeper_numbers2(board):
    
    solution = [[]]
    row = 0
    col = 0

    while(row < len(board)):
        
        if board[row][col] == 1:
            solution[row].append(9)
        else:

            mod_row = -1
            mod_col = -1
            neighbours = 0

            while(mod_row <= 1):

                check_row = row + mod_row
                check_col = col + mod_col

                valid_row = check_row >= 0 and check_row < len(board)
                
                if valid_row:
                    valid_col = check_col >= 0 and check_col < len(board[check_row])
                    if valid_col and (board[check_row][check_col]):
                        neighbours += 1

                if mod_col == 1:
                    mod_col = -1
                    mod_row += 1
                else:
                    mod_col += 1

            solution[row].append(neighbours)
            
        col += 1

        if col == len(board[row]):
            col = 0
            row += 1
            solution.append([])

    solution.pop(-1)      
    return solution

board = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0]
]

solution = [
    [1, 9, 2, 1],
    [2, 3, 9, 2],
    [3, 9, 4, 9],
    [9, 9, 3, 1]
]

print(minesweeper_numbers2(board) == solution)