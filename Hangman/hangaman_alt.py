# This another version of the hangman game !!
from random import choice

def hangman_game():
    print("Welcome to Hangman Game !!")

    with open("common.txt", "r") as file:
        words = file.read().splitlines()

    valid_words = []
    for word in words:
        if word.isalpha():
            valid_words.append(word.lower())
    secret_word = choice(valid_words)

    lives = len(secret_word)
    underscores = []
    for _ in range(len(secret_word)):
        underscores.append("_")
    print("Word to guess:", underscores)

    while lives > 0:
        guess = input("Guess a letter: ")
        if len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue
        if not guess.isalpha():
            print("Invalid input. Please enter a valid letter.")
            continue
        if guess in secret_word:
            print("Good guess!")
            for i in range(0, len(secret_word)):
                if secret_word[i] == guess:
                    underscores[i] = guess
            print(underscores)
        if guess not in secret_word:
            print("Oops! That letter is not in the word.")
            lives -= 1
            print(f"You have {lives} lives left.")
        if "_" not in underscores:
            word_guessed = "".join(underscores)
            print(f"Congratulations! You guessed the word!, {word_guessed}.")
            break
    if lives == 0:
        print(f"You ran out of lives. The word was: {secret_word}")

if __name__ == "__main__":
    hangman_game()
