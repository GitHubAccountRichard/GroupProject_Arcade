import random # Need random to generate random numbers to memorize
import time #Allows me to add a timer, so that there is a timed memorization


def clear_screen():
    """Clears the screen by adding 100 empty lines.
    :return: 100 empty lines
    """
    print("\n" * 100)  # Clear screen by printing 100 empty lines


def play_game():
    """Creates an empty list, so that numbers can be added to it. lists are mutable, allowing this to work.
    :return:
    """
    sequence = []

    while True:
        sequence.append(str(random.randint(0, 9)))  # Adds a new number to the list
        print("Memorize this sequence:")
        print(" ".join(sequence))
        time.sleep(len(sequence) * 2)  #Used chatgpt, to figure out that this allows for 2 seconds per number to memorize.

        clear_screen()  # Clears screen so that player can't see their previous answer
        user_input = input(f"Enter the sequence ({len(sequence)} numbers): ").strip() #asks user to type out the memorized sequence

        if user_input != "".join(sequence): #what happens when they don't get it right
            print("Game Over! You entered the wrong sequence.")
            print(f"The correct sequence was: {' '.join(sequence)}")
            break #stops while loop

        print("Correct! Next round...\n")


if __name__ == "__main__":
    play_game()
