import Battleship


def game():

    print("Welcome to Battleship!")

    # Create board
    board = Battleship.makeBoard(size=7)

    # Place the ship
    Battleship.putShip(board, size=4)

    # how many parts are left to hit
    ship_left = 4

    # loopiung the game
    while ship_left > 0:
        # Display the current board, hide true because we dont want to sere the board
        Battleship.print_board(board, hide=True)

        # player's guess
        guess = Battleship.user_input()

        # Check the guess
        result = Battleship.check_hit(board, guess[0], guess[1])
        print(result["message"])

        if result["hit_state"] is True:  # Hit
            ship_left -= 1

    # Player has sunk the ship
    print("\nYou sank the ship!")
    # Reveal board with ship positions
    Battleship.print_board(board, hide=False)


#Still dont understand this but copy and past from his slides and seems to work ¯\_(ツ)_/¯
if __name__ == "__main__":
    game()
