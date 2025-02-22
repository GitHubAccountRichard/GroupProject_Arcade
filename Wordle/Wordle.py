#File to add a Wordle game


#First need to import an online dictionary
import requests
import random

book = requests.get("https://www.mit.edu/~ecprice/wordlist.10000")
lines = book.text.split("\n")
number_of_words = len(lines)
print(number_of_words)

#Second get one random word from the dictionary
random_word = lines[random.randint(0, number_of_words-1)]
print(random_word)

word_guess_list = ["_"] * len(random_word)
print(word_guess_list)

#Write a function that takes the input and checks against the user input


