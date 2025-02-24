import Blackjack.Blackjack_game as Blackjack_game_funciton
from Battleship import Battleship_main
from Hangman.hangaman_alt import hangman_game
from Roulette.Roulette import Roulette_game
from TicTacToe.TicTacToe import play_game
from Wordle.Wordle import wordle_game

Games = ["1. Battleship", "2. Hangman", "3. Roulette", "4. Wordle", "5. Blackjack", "6. Tic-Tac-Toe", "7. Memory Game",
         "8. Quit"]


while True:
    for i in Games:
        print(i)

    try:
        GameChoice = int(input("What game do you want to play? (1-8)"))
        if 1 <= GameChoice <= 8:
            if GameChoice == 8:
                print("Thank you for playing! Goodbye!")
                break
            elif GameChoice == 1:
                if __name__ == "__main__":
                    Battleship_main.game()
            elif GameChoice == 2:
                if __name__ == "__main__":
                    hangman_game()
            elif GameChoice == 3:
                if __name__ == "__main__":
                    Roulette_game()
            elif GameChoice == 4:
                if __name__ == "__main__":
                    wordle_game()
            elif GameChoice == 5:
                if __name__ == "__main__":
                    Blackjack_game_funciton()
            elif GameChoice == 6:
                if __name__ == "__main__":
                    play_game()
        else:
            print("Stop messing around - please enter a number between 1 and 8")
    except ValueError:
        print("Stop messing around - please enter a valid number between 1 and 8")
