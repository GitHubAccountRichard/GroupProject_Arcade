import random

# Function to create a 10x10 battleship board
def battleship_board():
    """
    Generates a 10x10 representation of a battleship board.
    :return: A 10x10 battleship board where each cell is initialized as "[ ]".
    """
    return [["[ ]"] * 10 for _ in range(10)]

# Function to print the battleship board
def print_board(board):
    """
    Prints a visual representation of the battleship board.
    :param board: The battleship board to print (list of lists).
    """
    row_number = 1
    for row in board:
        if row_number == 10:
            print(f"Row10 {' '.join(row)}")  #Because "Row 10" string is longer than single digit rows
        else:
            print(f"Row {row_number} {' '.join(row)}")
        row_number += 1

# Function to pick a random starting position for the ship
def ship_position():
    """
    Picks a random starting position for a ship on the board.
    :return: A tuple (row, column) representing the ship's position.
    """
    row = random.randint(0, 9)
    column = random.randint(0, 9)
    return row, column

# Function to mark a ship's position on the board
def long_mark_ship(board, row, column):
    """
    Marks a position on the battleship board with "[X]"
    :param board: The battleship board to update (list of lists).
    :param row: The row index (0-based).
    :param column: The column index (0-based).
    """
    board[row][column] = "[X]"
    if row +1 > 9:
        board[row-2][column] = "[X]"
    else:
        board[row+1][column] = "[X]"
    if row -1 < 0:
        board[row+2][column] = "[X]"
    else:
        board[row-1][column] = "[X]"


def broad_mark_ship(board, row, column):
    board[row][column] = "[X]"
    if column +1 > 9:
        board[row][column-2] = "[X]"
    else:
        board[row][column+1] = "[X]"
    if column -1 < 0:
        board[row][column+2] = "[X]"
    else:
        board[row][column-1] = "[X]"

#Running this bs


position1 = ship_position()
row1 = position1[0]
column1 = position1[1]

position2 = ship_position()
row2 = position2[0]
column2 = position2[1]

def compare (row1, column1, row2, column2):
    for i in range(-1,1):
        if row1 == row2 or column1 == column2:
            return True
        elif row1 + i == row2 or column1 + i == column2:
            return True
        else:
            return False

while compare(row1, column1, row2, column2) == True:
    position1 = ship_position()
    row1 = position1[0]
    column1 = position1[1]

    position2 = ship_position()
    row2 = position2[0]
    column2 = position2[1]
    if compare(row1, column1, row2, column2) == False:
        break

board = battleship_board()
broad_mark_ship(board, row2, column2)
long_mark_ship(board, row1, column1)
print_board(board)
