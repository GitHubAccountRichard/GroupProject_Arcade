import random
import time
import os


def clear_screen():
    print("\n" * 100)  # Clear screen by printing 100 empty lines


def play_game():
    sequence = []

    while True:
        sequence.append(str(random.randint(0, 9)))  # Add a new random digit
        print("Memorize this sequence:")
        print(" ".join(sequence))
        time.sleep(len(sequence) * 2)  # Wait 2 seconds per number

        clear_screen()  # Clear screen before user inputs their answer
        user_input = input(f"Enter the sequence ({len(sequence)} numbers): ").strip()

        if user_input != "".join(sequence):
            print("Game Over! You entered the wrong sequence.")
            print(f"The correct sequence was: {' '.join(sequence)}")
            break

        print("Correct! Next round...\n")


if __name__ == "__main__":
    play_game()
