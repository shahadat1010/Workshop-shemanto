'''
Function getList(filename):
    Read the content of the file specified by filename.
    If the file exists:
        Read each line of the file and store it in a list.
    If the file does not exist or is empty:
        Initialize an empty list.
    Return the list of items.
Function showList(data):
    If the list is empty:
        Print "Your To Do List is empty."
    Otherwise:
        Print "To Do List:".
        Loop through each item in the list:
            Print the item number and the item itself.
Function addToList(filename, data):
    Prompt the user to enter an item to add to the list.
    Read the user's input.
    Append the entered item to the list.
    Write the updated list to the file specified by filename.
    Print a confirmation message.
    Return the updated list.
Function deleteFromList(filename, data):
    If the list is empty:
        Print "Nothing to delete."
        Return the unchanged list.
    Otherwise:
        Prompt the user to enter the item number to delete.
        Read the user's input.
        If the input is not a valid item number:
            Print an error message and return the unchanged list.
        Otherwise:
            Remove the item at the specified index from the list.
            Write the updated list to the file specified by filename.
            Print a confirmation message.
            Return the updated list.
Define a function called main:
    Set FILENAME to 'list.txt'
    Call the function getList with FILENAME as argument and store the result in lineList
    
    Enter an infinite loop:
        Display the current list of items using the showList function
        Print instructions for the user:
            - Type "a" to add an item
            - If the list is not empty, type "d" to delete an item
            - Type "x" to exit the program
        
        Prompt the user for input and store it in the variable command
        
        If the user input is 'a':
            Call the addToList function with FILENAME and lineList as arguments, and update lineList with the returned value
        Else, if the user input is 'd' and the list is not empty:
            Call the deleteFromList function with FILENAME and lineList as arguments, and update lineList with the returned value
        Else, if the user input is 'x':
            Print "Goodbye!" and exit the loop
        Otherwise:
            Print "Invalid command."

If the program is executed as the main script:
    Call the main function            

'''




import os

def getList(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            data = file.readlines()
    except FileNotFoundError:
        with open(filename, 'w+') as file:
            pass
    return data

def showList(data):
    if len(data) == 0:
        print("Your To Do List is empty.")
    else:
        item_number = 1
        for item in data:
            print(f"{item_number}) {item.strip()}")
            item_number += 1

def addToList(filename, data):
    new_item = input("Enter an item to add to the To Do List: ")
    data.append(new_item + '\n')
    with open(filename, 'a') as file:
        file.write(new_item + '\n')
    print("Item added to the To Do List.")
    return data

def deleteFromList(filename, data):
    try:
        item_number = int(input("Enter the item number to delete: "))
        index = item_number - 1
        del data[index]
        with open(filename, 'w') as file:
            file.writelines(data)
        print("Item deleted from the To Do List.")
    except ValueError:
        print("Invalid input. Please enter a valid item number.")
    except IndexError:
        print("Invalid item number. Please enter a valid item number.")
    return data


def main():
    FILENAME = 'list.txt'
    lineList = getList(FILENAME)
    
    while True:
        showList(lineList)
        print('\nType "a" to add an item.')
        if len(lineList) > 0:
            print('Type "d" to delete an item.')
        print('Type "x" to exit.')
        
        command = input('> ')
        if command == 'a':
            lineList = addToList(FILENAME, lineList)
        elif command == 'd' and len(lineList) > 0:
            lineList = deleteFromList(FILENAME, lineList)
        elif command == 'x':
            print('Goodbye!')
            break
        else:
            print('Invalid command.\n')

if __name__ == "__main__":
    main()
