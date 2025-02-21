from Battleship import Battleship_main
from Battleship import Battleship

Games = ["1. Battleship", "2. Hangman", "3. Roulette", "4. TicTacToe", "5. Quit"]
print("Welcome to the Arcade!")
print("We have a couple of game")
for i in Games:
    print(i)

while True:
    try:
        GameChoice = int(input("What game do you want to play? (1-5)"))
        if 1 <= GameChoice <= 5:
            break
        else:
            print("Stop messing around - please enter a number between 1 and 5")
    except ValueError:
        print("Stop messing around - please enter a valid number between 1 and 5")
    
    
if GameChoice == 1:
    if __name__ == "__main__": #I forgot what this does but he mentioned that this is good so use it for your games too I guess ¯\_(ツ)_/¯
        Battleship_main.game()

if GameChoice == 5:
    quit()