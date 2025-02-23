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
while "Yes" in input("Do you want to play/keep playing? (Yes/No): "):
    while True:
        bet = int(input("Enter your bet amount: "))
        if bet <= credit:
            break
        else:
            print(f"Invalid bet! Your bet cannot exceed your credit (${credit}). Please try again.")
    first12=list(range(1, 13))
    second12=list(range(13, 25))
    third12=list(range(25, 37))
    row1=[i for i in range(1, 37) if (i - 1) % 3 == 0]
    row2=[i for i in range(1,37) if (i-2)%3==0]
    row3=[i for i in range (1,37) if (i-3)%3==0]
    print(f"First 12 is {first12}, Second 12 is {second12}, Third 12 is {third12}.")
    print(f"Row 1 is {row1}, Row 2 is {row2}, Row 3 is {row3}.")
    print(f"Black is even, red is odd.")
    print(f"We are not responsible for any losses due to lack of following the rules.")
    numbet=(input("Enter where you want to bet (options are 0 to 36, red, black, first12, second12, third12, row1, row2, row3): "))
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
    elif numbet is first12:
        if roulette_choice in first12:
            print("You won!")
            credit += bet*3
            print(f"You won ${bet*3}!")
    elif numbet is second12:
        if roulette_choice in second12:
            print("You won!")
            credit += bet*3
            print(f"You won ${bet*3}!")
    elif numbet is third12:
        if roulette_choice in third12:
            print("You won!")
            credit += bet*3
            print(f"You won ${bet*3}!")
    elif numbet is row1:
        if roulette_choice in row1:
            print("You won!")
            credit += bet*3
            print(f"You won ${bet*3}!")
    elif numbet is row2:
        if roulette_choice in row2:
            print("You won!")
            credit += bet*3
            print(f"You won ${bet*3}!")
    elif numbet is row3:
        if roulette_choice in row3:
            print("You won!")
            credit += bet*3
            print(f"You won ${bet*3}!")
    else:
        print("You lost!")
        credit -= bet
        print(f"You lost ${bet}!")
    print(f"Your current credit is ${credit}.")
    print("Thanks for playing!")
    if credit <= 0:
        print("You have run out of credit. Game over.")
        break