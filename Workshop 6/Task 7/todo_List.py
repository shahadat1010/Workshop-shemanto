"""

def showList(data):
    if not data:  # Check if the list is empty
        print("Your To Do List is empty.")
    else:
        item_number = 1  # Initialize item number
        for item in data:
            print(f"{item_number}: {item.rstrip()}")  # Remove line breaks and print item
            item_number += 1  # Increment item number 
Function getList(filename):
    Initialize an empty list called data
    
    Try to open the file specified by the filename in read mode:
        If successful:
            Read all lines from the file into the data list using the readlines() method
        If the file does not exist (FileNotFoundError):
            Open the file in write/read mode ('w+') to create an empty file
            (This also allows reading from the file)
        Close the file
        
    Return the data list
Function showList(list):
 If the list is empty:
   Print "Your To Do List is empty."
 Else:
   Initialize item_number to 1
For each item in the list:
Print item_number + ": " + item
Increment item_number
End
End Function
addToList(filename, data):
    Prompt the user to enter an item for the To Do List
    Add the entered item to the data list (append '\n' to the end of the item)
    Open the file in Append ('a') mode
    Write the entered item to the file
    Close the file
    Print a message confirming that the item has been added
    Return the modified data list

deleteFromList(filename, data):
    Prompt the user to enter the item number to delete
    Try to convert the input to an integer
    Handle ValueError if conversion fails by printing an error message and returning the unchanged list
    Subtract 1 from the entered item number to get the appropriate index in the list
    Try to delete the item from the list using the index
    Handle IndexError if the index is out of range by printing an error message and returning the unchanged list
    Open the file in Write ('w') mode
    Write the updated list to the file using the writelines() method
    Close the file
    Print a message confirming that the item has been deleted
    Return the modified list    
    """


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
