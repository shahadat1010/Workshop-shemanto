"""
 Import the json module for working with JSON data
 Define the dictionary of students with student numbers as keys and names as values
 Define a function to generate a unique username from a student's name
     Extract the first letter of the first name and the first 4 letters of the surname
     If the username is less than 5 characters long, pad it with zeroes
     Check for uniqueness by appending a counter if needed
 Create an empty dictionary to store the generated usernames
 Iterate over each student in the students dictionary
     Split the student's name into first name and surname
     Generate a unique username for the student
     Add the username to the usernames dictionary with the student number as the key
 Write the usernames to a text file in JSON format
     Open the file in write mode
     Use json.dump() to write the usernames dictionary to the file
     Close the file
 Display the generated usernames
"""


import json

students = {
    60254: 'John Smith',
    60255: 'Gert Hans-Dyer',
    60256: 'Sun Po',
    60257: 'Bort Woods',
    60258: 'Andrew Butters',
    60259: 'Betty Ho',
    60260: 'Jonah Smithers',
    60261: 'Sha Po',
    60262: 'Jane Smitt'
}

def generate_username(first_name, surname, usernames):
    username = first_name[0].lower() + surname[:4].lower()
    if len(username) < 5:
        username = username.ljust(5, '0')
    
    counter = 1
    while True:
        new_username = username + str(counter)
        if new_username not in usernames.values():
            return new_username
        counter += 1

usernames = {}

for student_number, student_name in students.items():
    first_name, surname = student_name.split()
    username = generate_username(first_name, surname, usernames)
    usernames[student_number] = username

with open('usernames.txt', 'w') as file:
    json.dump(usernames, file)

for student_number, username in usernames.items():
    print(f"{student_number}: {username}")
