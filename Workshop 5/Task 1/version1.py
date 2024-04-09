'''
Prompt the user to choose between generating an addition or subtraction test ("+" or "-").
Read the user's choice.

If the user's choice is "+":
 Generate an addition test:
   Set question_count to 1.
   Repeat 10 times:
     Generate two random numbers between 0 and 9.
     Calculate the sum of the two numbers.
     Display the question in the format "number1 + number2 = ".
     Increment the question_count.

If the user's choice is "-":
  Generate a subtraction test:
    Set question_count to 1.
    Repeat 10 times:
      Generate two random numbers between 0 and 9.
      Ensure that the second number is less than or equal to the first number to prevent negative answers.
      Calculate the difference between the two numbers.
      Display the question in the format "number1 - number2 = ".
      Increment the question_count.

Display the generated test.'''
import random

def generate_test():
    choice = input("Enter '+' for addition test or '-' for subtraction test: ")
    print()
    
    question_count = 1
    
    if choice == '+':
        for _ in range(10):
            num1 = random.randint(0, 9)
            num2 = random.randint(0, 9)
            question = f"{num1} + {num2} = "
            print(f"{question_count}. {question}")
            question_count += 1
    elif choice == '-':
        for _ in range(10):
            num1 = random.randint(0, 9)
            num2 = random.randint(0, num1)
            question = f"{num1} - {num2} = "
            print(f"{question_count}. {question}")
            question_count += 1

def main():
    generate_test()

if __name__ == "__main__":
    main()
