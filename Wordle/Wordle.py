# First need to import an online dictionary
import random

import requests

book = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
lines = book.text.split("\n")

#Second get one random word from the dictionary
five_letter_words = []
for word in lines:
    if len(word) == 5:
        five_letter_words.append(word)

five_letter_words = five_letter_words[random.randint(0, len(five_letter_words))]

word_guess_list = ["_"] * len(five_letter_words)
print(word_guess_list)

#Write a function that takes the input and checks against the user input
#Get user input
guess = input("Enter a five letter word: ")

for i in range(len(five_letter_words)):
    if guess[i] in five_letter_words:
        word_guess_list[i] = guess[i]
        print(word_guess_list)
