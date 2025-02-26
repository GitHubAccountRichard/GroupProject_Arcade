from Battleship.Battleship_functions import makeBoard, putShip, print_board, user_input, check_hit


def game():
    """
    This functions runs the battleship game using all the functions in the Battleship_functions.py file, basically just convenient way to run it

    :raises ValueError: If user input is invalid or out of bounds.
    :return: None
    """
    print("Welcome to Battleship!")

    # Create board
    board = makeBoard(size=7)

    # Place the ship
    putShip(board, size=4)

    # how many parts are left to hit
    ship_left = 4

    # loopiung the game
    while ship_left > 0:
        # Display the current board, hide true because we dont want to sere the board
        print_board(board, hide=True)

        # player's guess
        guess = user_input()

        # Check the guess
        result = check_hit(board, guess[0], guess[1])
        print(result["message"])

        if result["hit_state"] is True:  # Hit
            ship_left -= 1


    print("\nYou sank the ship!")

    print_board(board, hide=False)


#Still dont understand this but copy and past from his slides and seems to work ¯\_(ツ)_/¯
if __name__ == "__main__":
    game()
