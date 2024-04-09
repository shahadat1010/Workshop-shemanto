def inputChoice(prompt, choices):
    while True:
        response = input(prompt)
        if response in choices:
            return response
        else:
            print("Invalid input: please enter one of", choices)