"""import random

number = random.randrange(0, 100)
guessCheck = "wrong"
print("Welcome to Number Guess")

while guessCheck == "wrong":
    response = int(input("Please input a number between 0 and 100:"))
    try:
        val = int(response)
    except ValueError:
        print("This is not a valid integer. Please try again")
        continue
    val = int(response)
    if val < number:
        print("This is lower than actual number. Please try again.")
    elif val > number:
        print("This is higher than actual number. Please try again.")
    else:
        print("This is the correct number")
        guessCheck = "correct"

print("Thank you for playing Number Guess. See you again")


# Guess a number game
# https://github.com/hardikvasa/guess-the-number-game
# Add feature to check if the input number was between 1-100
# Add levels to the game to make it more exciting

from random import randint  # To generate a random number

name = input("Please Enter your name: ")
print("Welcome to my Number game, " + name)


def game():
    rand_number = randint(0, 100)  # Generates a random number
    print("\nI have selected a number between 1 to 100...")
    print("You have 6 chances to guess that number...")
    i = 1
    r = 1
    while i < 7:  # 6 Chances to the user
        user_number = int(input('Enter your number: '))
        if user_number < rand_number:
            print("\n" + name + ", My number is greater than your guessed number")
            print("you now have " + str(6 - i) + " chances left")
            i = i + 1
        elif user_number > rand_number:
            print("\n" + name + ", My number is less than your guessed number")
            print("you now have " + str(6 - i) + " chances left")
            i = i + 1
        elif user_number == rand_number:
            print("\nCongratulations " + name + "!! You have guessed the correct number!")
            r = 0;
            break
        else:
            print("This is an invalid number. Please try again")
            print("you now have " + str(6 - i) + " chances left")
            continue
    if r == 1:
        print("Sorry you lost the game!!")
        print("My number was = " + str(rand_number))


def main():
    game()
    while True:
        another_game = input("Do you wish to play again?(y/n): ")
        if another_game == "y":
            game()
        else:
            break


main()
print("\nEnd of the Game! Thank you for playing!")


"""

# This is a guess the number game.
# https://github.com/InterfaithCoding/GuessNumber/blob/master/guess.py
import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

while guessesTaken < 6:
    print('Take a guess.')  # There are four spaces in front of print.
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess > 20:
        print("Please enter a number into 0 from 20 ")
    else:
        if guess < number:
            print('Your guess is too low.')  # There are eight spaces in front of print.

        if guess > number:
            print('Your guess is too high.')

        if guess == number:
            break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
