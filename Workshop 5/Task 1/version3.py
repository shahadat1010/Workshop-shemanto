'''
Prompt the user to specify how many tests to generate.
Read the user's input as the number of tests to generate.

For each test to generate:
  Prompt the user to choose between generating an addition or subtraction test ("+" or "-").
  Read the user's choice.

  Display the test number.
    
  If the user's choice is "+":
    Generate an addition test:
      Set question_count to 1.
      Initialize an empty list to store generated questions.
      Repeat until 10 questions are generated:
        Generate two random numbers between 0 and 9.
        Ensure that the same question has not been generated before.
            If the question is a duplicate, generate new numbers until a unique question is formed.
        Calculate the sum of the two numbers.
        Display the question in the format "number1 + number2 = ".
        Add the question to the list of generated questions.
        Increment the question_count.

    If the user's choice is "-":
      Generate a subtraction test:
        Set question_count to 1.
        Initialize an empty list to store generated questions.
        Repeat until 10 questions are generated:
          Generate two random numbers between 0 and 9.
          Ensure that the second number is less than or equal to the first number to prevent negative answers.
          Ensure that the same question has not been generated before.
            If the question is a duplicate, generate new numbers until a unique question is formed.
          Calculate the difference between the two numbers.
          Display the question in the format "number1 - number2 = ".
          Add the question to the list of generated questions.
          Increment the question_count.

    Display the generated test.'''
import random

def generate_test():
    choice = input("Enter '+' for addition test or '-' for subtraction test: ")
    print()
    
    questions = []
    question_count = 1
    
    while len(questions) < 10:
        if choice == '+':
            num1 = random.randint(0, 9)
            num2 = random.randint(0, 9)
            question = f"{num1} + {num2} = "
        elif choice == '-':
            num1 = random.randint(0, 9)
            num2 = random.randint(0, num1)
            question = f"{num1} - {num2} = "
        
        if question not in questions:
            questions.append(question)
            print(f"{question_count}. {question}")
            question_count += 1

def main():
    num_tests = int(input("Enter the number of tests to generate: "))
    print()
    
    for i in range(num_tests):
        print(f"Test {i+1}:")
        generate_test()
        print()

if __name__ == "__main__":
    main()