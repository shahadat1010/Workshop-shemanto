'''Import the module inputfunction
Call the inputInt function from inputfunction module:
Prompt the user to enter an integer.
Receive the user input.
Validate the input as an integer.
If the input is not valid, display an error message and prompt the user again.
If the input is valid, assign it to the variable 'value'.
Print the value obtained from inputInt function.
Call the inputFloat function from inputfunction module:
Prompt the user to enter a float.
Receive the user input.
Validate the input as a float.
If the input is not valid, display an error message and prompt the user again.
If the input is valid, assign it to the variable 'value'.
Print the value obtained from inputFloat function.
'''
import inputfunction



value = inputfunction.inputInt('Enter an int: ')
print('Value is', value)

value = inputfunction.inputFloat('Enter a float: ')
print('Value is', value)
