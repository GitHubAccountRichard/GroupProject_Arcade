import random
import requests



def wordle_game():
    book = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
    lines = book.text.split("\n")

    #Make and fill empty list will all the 5-letter words in the dictionary
    five_letter_words = []
    for word in lines:
        if len(word) == 5:
            five_letter_words.append(word)

    #pick a random five letter word
    five_letter_words = five_letter_words[random.randint(0, len(five_letter_words))]

    #make list which corrosponds with length of word
    word_guess_list = ["_"] * len(five_letter_words)
    print(word_guess_list)

    #keep track of wrong and misplaced characters and boundaries
    not_included = []
    wrong_position = []
    upper_cap = 5
    counting_guess = 0

    #The big game loop basically
    while "_" in word_guess_list and counting_guess < upper_cap:
        guess = input("Enter a five letter word: ")
        guess = guess.lower()

        if len(guess) != 5:
            print("Make sure that your word is five letter long")
            continue

        counting_guess += 1
        wrong_position = []
        remaining_letters = list(five_letter_words)

        for i in range(len(five_letter_words)):
            # Correct letters in the correct position
            if guess[i] == five_letter_words[i]:
                word_guess_list[i] = guess[i]
                remaining_letters[i] = None  # Mark matched letter as used

        for i in range(len(five_letter_words)):
            # Correct letters in the wrong position
            if guess[i] in remaining_letters and guess[i] != five_letter_words[i]:
                wrong_position.append(guess[i])
                remaining_letters[remaining_letters.index(guess[i])] = None  # Mark matched letter as used

            # Incorrect letters
            elif guess[i] not in five_letter_words and guess[i] not in not_included:
                not_included.append(guess[i])

        print(f"Incorrect guesses so far: {not_included}")
        print(f"Letters in the word but in the wrong position: {wrong_position}")
        print(f"Current progress of guessed word: {word_guess_list}")

    if "_" not in word_guess_list:
        print(f"Congratulations! You've guessed the word:, {five_letter_words}")
    else:
        print(f"Sorry, you've reached your maximum number of guesses. The word was:, {five_letter_words}")


if __name__ == "__main__":
    wordle_game()