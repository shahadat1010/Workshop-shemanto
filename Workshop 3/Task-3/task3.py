'''
Initialize a variable named "number" with a random integer between 1 and 100.
Initialize a counter variable to keep track of the number of guesses.
Start an endless loop:
Prompt the user to guess the number between 1 and 100.
Increment the counter by 1.
Check if the user's guess is equal to the generated number:
If yes, print a congratulatory message with the correct number and the number of guesses, then break the loop.
If no, check if the guess is too low or too high:
If too low, print "Too low!".
If too high, print "Too high!".
'''
import random

def guess_the_number():
    number = random.randint(1, 100)
    counter = 0

    while True:
        user_number = int(input("Guess the number between 1 and 100: "))
        counter += 1

        if user_number == number:
            print(f"Congratulations! You've guessed the correct number {number} in {counter} guesses.")
            break
        elif user_number < number:
            print("Too low!")
        else:
            print("Too high!")

guess_the_number()