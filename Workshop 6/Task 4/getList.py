'''Function getList(filename):
    Initialize an empty list called data
    
    Try to open the file specified by the filename in read mode:
        If successful:
            Read all lines from the file into the data list using the readlines() method
        If the file does not exist (FileNotFoundError):
            Open the file in write/read mode ('w+') to create an empty file
            (This also allows reading from the file)
        Close the file
        
    Return the data list'''
def getList(filename):
    data = []  
    try:
        with open(filename, 'r') as file:
            data = file.readlines()
    except FileNotFoundError:
        with open(filename, 'w+') as file:
            pass  
    
    return data 

