from Battleship import Battleship_main
from Battleship import Battleship_functions
from Hangman.hangaman_alt import hangman_game
from Wordle.Wordle import wordle_game




Games = ["1. Battleship", "2. Hangman", "3. Roulette", "4. TicTacToe", "5. Wordle", "6. Quit"]
print("Welcome to the Arcade!")
for i in Games:
    print(i)

while True:
    try:
        GameChoice = int(input("What game do you want to play? (1-6)"))
        if 1 <= GameChoice <= 6:
            break
        else:
            print("Stop messing around - please enter a number between 1 and 6")
    except ValueError:
        print("Stop messing around - please enter a valid number between 1 and 6")
    
    
if GameChoice == 1:
    if __name__ == "__main__": #I forgot what this does but he mentioned that this is good so use it for your games too I guess ¯\_(ツ)_/¯
        Battleship_main.game()

elif GameChoice == 2:
    if __name__ == "__main__":
        hangman_game()
elif GameChoice == 5:
    if __name__ == "__main__":
        wordle_game()
else:
    quit()