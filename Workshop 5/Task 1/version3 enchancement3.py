'''
Prompt the user to specify how many tests to generate.
Read the user's input as the number of tests to generate.

Open a file named "output.txt" for writing.

For each test to generate:
    Write the test number to the file.
    Display the test number.

    Prompt the user to choose between generating an addition or subtraction test ("+" or "-").
    Read the user's choice.
    Write the user's choice to the file.

    Display the test number.

    Set question_count to 1.

    If the user's choice is "+":
        Repeat 9 times:
            Generate a random addition question using numbers from 0 to 9.
            Write the question to the file.
            Display the question.
            Increment question_count.
        
        Prompt the user if they want a challenge question ("y" or "n").
        If yes:
            Generate a random addition question using numbers from 10 to 20.
            Write the question to the file.
            Display the question.
    
    If the user's choice is "-":
        Repeat 9 times:
            Generate a random subtraction question using numbers from 0 to 9.
            Write the question to the file.
            Display the question.
            Increment question_count.
        
        Prompt the user if they want a challenge question ("y" or "n").
        If yes:
            Generate a random subtraction question using numbers from 10 to 20.
            Write the question to the file.
            Display the question.

Close the file.

Display "Tests saved in output.txt file."

'''


import random
import inputchoice
import inputfunction

def generate_question(numbers_range, challenge_question):
    num1 = random.randint(numbers_range[0], numbers_range[1])
    num2 = random.randint(numbers_range[0], numbers_range[1])
    
    if challenge_question:
        question = "Challenge question - do your best!\n"
    else:
        question = ""
    
    operator = '+' if random.choice([True, False]) else '-'
    
    if operator == '-':
        while num2 > num1:
            num2 = random.randint(numbers_range[0], numbers_range[1])
        question += f"{num1} - {num2} = \n"
    else:
        question += f"{num1} + {num2} = \n"
    
    return question

def main():
    num_tests = inputfunction.inputInt("Enter the number of tests to generate: ", "Invalid input: integer required.", 1)
    print()
    
    with open("output.txt", "w") as file:
        for test_num in range(1, num_tests + 1):
            file.write(f"Test {test_num}:\n")
            print(f"Test {test_num}:")
            
            choice = inputchoice.inputChoice("Enter '+' for addition test or '-' for subtraction test: ", ('+', '-'))
            file.write(choice + "\n\n")
            print()
            
            question_count = 1

            if choice == '+':
                for _ in range(9):
                    question = generate_question((0, 9), False)
                    file.write(f"{question_count}. {question}")
                    print(f"{question_count}. {question}", end="")
                    question_count += 1
                    
                challenge_choice = inputchoice.inputChoice("Do you want a challenge question? (y/n): ", ('y', 'n'))
                if challenge_choice.lower() == 'y':
                    question = generate_question((10, 20), True)
                    file.write(f"{question_count}. {question}")
                    print(f"{question_count}. {question}", end="")
                    
            elif choice == '-':
                for _ in range(9):
                    question = generate_question((0, 9), False)
                    file.write(f"{question_count}. {question}")
                    print(f"{question_count}. {question}", end="")
                    question_count += 1
                    
                challenge_choice = inputchoice.inputChoice("Do you want a challenge question? (y/n): ", ('y', 'n'))
                if challenge_choice.lower() == 'y':
                    question = generate_question((10, 20), True)
                    file.write(f"{question_count}. {question}")
                    print(f"{question_count}. {question}", end="")

            file.write("\n\n")
            print()

    print("Tests saved in output.txt file.")

if __name__ == "__main__":
    main()
