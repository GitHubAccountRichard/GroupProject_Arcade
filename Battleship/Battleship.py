import random


# Function to create a 7x7 battleship board
def makeBoard(size=7):
    """
    Generates a 7x7 representation of a battleship board
    :return: A battleship board where each cell is "[ ]".
    """
    return [["[ ]"] * size for _ in range(size)]


# Function to print the battleship board
def print_board(board, hide=True):
    """
    Prints a visual of the board.
    :param board: print board
    :param hide: decide to hide the ship positions during gameplay.
    """
    for row in board:
        for cell in row:
            if cell == "[X]" and hide:  # Hide ships during game
                print("[ ]", end=" ")
            else:
                print(cell, end=" ")
        print()
    print()


# Function to place a ship on the board
def putShip(board, size, orientation=None):
    """
    Places a ship randomly on the board
    :param board: The board where the ship will be placed
    :param size: The size of the ship
    :param orientation: not necessary but if I want to define the orientation of the ship later
    """
    while True:
        direction = random.randint(0, 1) if orientation is None else orientation
        if direction == 0:  # Horizontal placement
            row = random.randint(0, len(board) - 1)
            col = random.randint(0, len(board[0]) - size)

            if all(board[row][col + i] == "[ ]" for i in range(size)):
                for i in range(size):
                    board[row][col + i] = "[X]"
                return
        else:
            row = random.randint(0, len(board) - size)
            col = random.randint(0, len(board[0]) - 1)

            if all(board[row + i][col] == "[ ]" for i in range(size)):
                for i in range(size):
                    board[row + i][col] = "[X]"
                return


# Function to take player input
def user_input():
    """
    Gathers user input for their guess
    :return: Tuple of the user's guess
    """
    while True:
        try:
            row = int(input("Enter row number (1-7): ")) - 1
            column = int(input("Enter column number (1-7): ")) - 1
            if 0 <= row < 7 and 0 <= column < 7:
                return row, column
            else:
                print("Out of bounds! Please pick numbers between 1 and 7.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")


# Function to check hits or misses
def check_hit(board, row, col):
    """
    Checks whether the user hit a part of the ship or missed
    :param board: The battleship board
    :param row: The row  of the user's guess
    :param col: The column  of the user's guess
    :return: A dictionary with the result (hit/miss)
    """
    if board[row][col] == "[X]":  # Hit
        board[row][col] = "[H]"  # Mark as hit
        return {
            "hit_state": True,
            "message": "You hit part of the ship!"
        }
    elif board[row][col] in ["[O]", "[H]"]:  # Already guessed
        return {
            "hit_state": None,
            "message": "You’ve already guessed this spot!"
        }
    else:  # Miss
        board[row][col] = "[O]"
        return {
            "hit_state": False,
            "message": "Miss!"
        }
