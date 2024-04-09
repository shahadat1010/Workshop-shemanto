''' Define a function named generate_random_numbers(total_number) to generate random numbers.
    Initialize a loop iterating from 1 to total_number (inclusive).
    Generate a random number between 0 and 10 (inclusive) and store it in random_digit.
    Print the index of the current number.
    Print the value of the generated random number.
    Check if the generated number is equal to 7.
    If it is, print "Lucky 7!".
   
Call the generate_random_numbers function with the argument 10 to generate 10 random numbers.'''


import random

def generate_random_numbers(total_number):
    for index in range(1, total_number + 1):
        random_digit = random.randint(0, 10)  
        print(f"Number {index} was {random_digit}")
        if random_digit == 7:
            print("Lucky 7!")

generate_random_numbers(10)