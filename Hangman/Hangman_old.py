# This is the game of hangman.
print("Welcome to the Hangman game!")
from random import choice
from nltk.corpus import wordnet as wn
noun_synsets = list(wn.all_synsets('n'))
while True:
    random_synset = choice(noun_synsets)
    random_lemma = choice(random_synset.lemmas())
    word = random_lemma.name()
    if "_" in word or " " in word:
        continue
    random_noun_name = word.lower()
    break
print(random_noun_name)
lives = len(random_noun_name)
underscores = []
for _ in range(len(word)):
    underscores.append("_")
print("Word to guess:", underscores)

lives = len(random_noun_name)
while lives > 0:
    guess = input("Guess a letter: ")
    if guess == len(guess) != 1:
        print("Invalid input. Please enter a single letter.")
        continue
    if not guess.isalpha():
        print("Invalid input. Please enter a valid letter.")
        continue
    if guess in random_noun_name:
        print("Good guess!")
        for i in range(0,len(random_noun_name)):
            if random_noun_name[i] == guess:
                underscores[i] = guess
        print(underscores)
    if guess not in random_noun_name:
        print("Oops! That letter is not in the word.")
        lives -= 1
        print(f"You have {lives} lives left.")
    if "_" not in underscores:
        word_guessed = "".join(underscores)
        print(f"Congratulations! You guessed the word!, {word_guessed}.")
        break
if lives == 0:
    print(f"You ran out of lives. The word was: {random_noun_name}")
