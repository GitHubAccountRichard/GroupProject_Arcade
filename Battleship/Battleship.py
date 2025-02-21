import random
# Function to create a 10x10 battleship board
def battleship_board():
    """
    Generates a 10x10 representation of a battleship board.
    :return: A 10x10 battleship board where each cell is initialized as "[ ]".
    """
    return [["[ ]"] * 10 for _ in range(10)]#

# Function to print the battleship board
def print_board(board):
    """
    Prints a visual of the battleship board.
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

# Same for a different ship
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

#Running comparing, in order to check if the ships intersect / crash into another :)
def compare (row1, column1, row2, column2):
    for i in range(-1,1):
        if row1 == row2 or column1 == column2:
            return True
        elif row1 + i == row2 or column1 + i == column2:
            return True
        else:
            return False

#Function to gather the user input
def user_input():
    print("Enter your coordinates: ")
    row_pick = int(input("Enter row number: "))
    column_pick = int(input("Enter column number: "))
    return row_pick, column_pick

#Function to check whether the user input was a hit
def check_hit(row_pick, column_pick, row1, column1, row2, column2):
    if compare(row1, column1, row_pick, column_pick):
        hit = {
            "row": row_pick,
            "column": column_pick,
            "hit_state": True,
            "message": "You have hit the vertical ship!"
        }
        return hit
    elif compare(row2, column2, row_pick, column_pick):
        hit = {
            "row": row_pick,
            "column": column_pick,
            "hit_state": True,
            "message": "You have hit the horizontal ship!"
        }
        return hit
    else:
        hit = {
            "row": row_pick,
            "column": column_pick,
            "hit_state": False,
            "message": "You missed!"
        }
        return hit

# Function to replace [X] with [H] if the ship has been hit
def replace_hit(board, row, column):
    if board[row][column] == "[X]":
        board[row][column] = "[H]"
