'''Function generate_question(numbers_range, challenge_question):
  Generate two random numbers between the specified numbers_range.
  If challenge_question is True:
        Use the numbers range 10 to 20 instead of the default 0 to 9.
        Print "Challenge question - do your best!" before the question.
  Calculate the sum or difference of the two numbers based on the user's choice.
  Display the question in the appropriate format.
  Return the generated question.

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
        Repeat until 9 questions are generated:
            Generate_question with numbers_range 0 to 9 and challenge_question False.
            Add the question to the list of generated questions.
            Increment the question_count.
        Prompt the user if they want a challenge question ("y" or "n").
          If they choose "y":
            Generate_question with numbers_range 10 to 20 and challenge_question True.
            Add the question to the list of generated questions.

  If the user's choice is "-":
    Generate a subtraction test:
        Set question_count to 1.
        Initialize an empty list to store generated questions.
        Repeat until 9 questions are generated:
           Generate_question with numbers_range 0 to 9 and challenge_question False.
           Add the question to the list of generated questions.
           Increment the question_count.
        Prompt the user if they want a challenge question ("y" or "n").
          If they choose "y":
              Generate_question with numbers_range 10 to 20 and challenge_question True.
              Add the question to the list of generated questions.

  Display the generated test.'''
import random

def generate_question(numbers_range, challenge_question):
    num1 = random.randint(numbers_range[0], numbers_range[1])
    num2 = random.randint(numbers_range[0], numbers_range[1])
    
    if challenge_question:
        print("Challenge question - do your best!")
    
    operator = '+' if random.choice([True, False]) else '-'
    question = f"{num1} {operator} {num2} = "
    
    if operator == '-':
        while num2 > num1:
            num2 = random.randint(numbers_range[0], numbers_range[1])
        question = f"{num1} - {num2} = "
    
    return question

def main():
    num_tests = int(input("Enter the number of tests to generate: "))
    print()

    for test_num in range(1, num_tests + 1):
        print(f"Test {test_num}:")
        choice = input("Enter '+' for addition test or '-' for subtraction test: ")
        print()
        
        print(f"Test {test_num}:")
        question_count = 1
        generated_questions = []

        if choice == '+':
            for _ in range(9):
                question = generate_question((0, 9), False)
                print(f"{question_count}. {question}")
                generated_questions.append(question)
                question_count += 1
                
            challenge_choice = input("Do you want a challenge question? (y/n): ")
            if challenge_choice.lower() == 'y':
                question = generate_question((10, 20), True)
                print(f"{question_count}. {question}")
                generated_questions.append(question)
                
        elif choice == '-':
            for _ in range(9):
                question = generate_question((0, 9), False)
                print(f"{question_count}. {question}")
                generated_questions.append(question)
                question_count += 1
                
            challenge_choice = input("Do you want a challenge question? (y/n): ")
            if challenge_choice.lower() == 'y':
                question = generate_question((10, 20), True)
                print(f"{question_count}. {question}")
                generated_questions.append(question)

        print()

if __name__ == "__main__":
    main()
