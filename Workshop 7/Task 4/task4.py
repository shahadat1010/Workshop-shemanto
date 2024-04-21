"""
Create an empty dictionary to store the usernames
Loop through each student in the students dictionary
   Split the student's name into first name and surname
   Create the username following the rules
   Check if the username length is less than 5
      Add zeros to the end of the username to make it at least 5 characters long
   Remove dashes from the username
   Add the username to the usernames dictionary with the student number as the key
Loop through the usernames dictionary to display the usernames
"""

students = {
    60256: 'Sun Po',
    60257: 'Bethany Wood',
    60258: 'Adam Buttock',
    60259: 'Brian Ho',
    60254: 'John Smith',
    60255: 'Grace Duca'
}

usernames = {}

for student_number, student_name in students.items():
    first_name, surname = student_name.split()
    username = first_name[0].lower() + surname[:4].lower()
    if len(username) < 5:
        username = username.ljust(5, '0')
    username = username.replace('-', '')
    usernames[student_number] = username
for student_number, username in usernames.items():
    print(f"{student_number}: {username}")
