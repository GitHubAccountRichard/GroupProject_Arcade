import random

credit = int(input("Enter the credit amount: "))

roulette_numbers = list(range(37))

# Select a random number from the roulette_numbers list
roulette_choice = (random.choice(roulette_numbers))

# Determine the color based on the number
if roulette_choice == 0:
    colour = "green"
elif roulette_choice % 2 == 0:
    colour = "black"
else:
    colour = "red"

while True:
    bet = int(input("Enter your bet amount: "))
    if bet <= credit:
        break
    else:
        print(f"Invalid bet! Your bet cannot exceed your credit (${credit}). Please try again.")

print(f"We are not responsible for any losses due to lack of following the rules.")
numbet=(input("Enter where you want to bet (options are 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, red, black, green): "))
if numbet.isdigit():
    numbet=int(numbet)
else:
    numbet=numbet

print(f"The roulette number is {roulette_choice}, and the color is {colour}.")


if numbet == colour:
    print("You won!")
    credit += bet
    print(f"You won ${bet}!")
elif numbet==roulette_choice:
    print("You won!")
    credit += bet*36
    print(f"You won ${bet*36}!")
else:
    print("You lost!")
    credit -= bet
    print(f"You lost ${bet}!")
print(f"Your current credit is ${credit}.")