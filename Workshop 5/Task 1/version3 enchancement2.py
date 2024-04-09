'''Prompt the user to enter the number of tests to generate.
Read the user's input as the number of tests.

For each test to generate:
  Print the test number.

   Prompt the user to choose between generating an addition or subtraction test ("+" or "-").
   Read the user's choice.

   Display the test number again.

   If the user's choice is "+":
      Generate an addition test:
        Set question_count to 1.
        Repeat until 9 questions are generated:
            Generate a random question within the numbers range (0 to 9) without repeating questions.
            Display the question in the format "number1 + number2 = ".
            Increment the question_count.
        Prompt the user if they want a challenge question ("y" or "n").
             If they choose "y":
               Generate a challenge addition question within the numbers range (10 to 20) without repeating questions.
               Display the challenge question.

  If the user's choice is "-":
     Generate a subtraction test:
        Set question_count to 1.
        Repeat until 9 questions are generated:
             Generate a random question within the numbers range (0 to 9) without repeating questions.
             Display the question in the format "number1 - number2 = ".
             Increment the question_count.
        Prompt the user if they want a challenge question ("y" or "n").
             If they choose "y":
                Generate a challenge subtraction question within the numbers range (10 to 20) without repeating questions.
                Display the challenge question.


'''


import random
import inputchoice
import inputfunction

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
    num_tests = inputfunction.inputInt("Enter the number of tests to generate: ", "Invalid input: integer required.", 1)
    print()

    for test_num in range(1, num_tests + 1):
        print(f"Test {test_num}:")
        choice = inputchoice.inputChoice("Enter '+' for addition test or '-' for subtraction test: ", ('+', '-'))
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
                
            challenge_choice = inputchoice.inputChoice("Do you want a challenge question? (y/n): ", ('y', 'n'))
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
                
            challenge_choice = inputchoice.inputChoice("Do you want a challenge question? (y/n): ", ('y', 'n'))
            if challenge_choice.lower() == 'y':
                question = generate_question((10, 20), True)
                print(f"{question_count}. {question}")
                generated_questions.append(question)

        print()

if __name__ == "__main__":
    main()
