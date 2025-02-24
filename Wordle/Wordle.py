import random
import requests



def wordle_game():
    book = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
    lines = book.text.split("\n")


    five_letter_words = []
    for word in lines:
        if len(word) == 5:
            five_letter_words.append(word)

    five_letter_words = five_letter_words[random.randint(0, len(five_letter_words))]


    word_guess_list = ["_"] * len(five_letter_words)
    print(word_guess_list)


    not_included = []
    wrong_position = []
    upper_cap = 5
    counting_guess = 0


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

            if guess[i] == five_letter_words[i]:
                word_guess_list[i] = guess[i]
                remaining_letters[i] = None

        for i in range(len(five_letter_words)):

            if guess[i] in remaining_letters and guess[i] != five_letter_words[i]:
                wrong_position.append(guess[i])
                remaining_letters[remaining_letters.index(guess[i])] = None


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