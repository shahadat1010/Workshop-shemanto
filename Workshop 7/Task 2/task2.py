'''
Create a "shortEnough" variable and set it to False
Create a "longEnough" variable and set it to False
Create a "hasUpper" variable and set it to False
Create a "hasLower" variable and set it to False
Create a "hasNumber" variable and set it to False
Create a "hasSpecial" variable and set it to False
Create "specialChars" string containing the special characters

If password length is <= 16:
 Set "shortEnough" to True
If password length is >= 8:
 Set "longEnough" to True

For each character in the password:
 If it is uppercase:
     Set "hasUpper" to True
 If it is lowercase:
     Set "hasLower" to True
 If it is a digit:
     Set "hasNumber" to True
 If it is in the "specialChars" string:
     Set "hasSpecial" to True

If all boolean variables are True:
 Return True
Else:
 Return False
'''

def checkPassword(p_word):
    shortEnough = False
    longEnough = False
    hasUpper = False
    hasLower = False
    hasNumber = False
    hasSpecial = False
    specialChars = '\'~!#$%^*()_+-={}|[]\\:<>?,./'
    if len(p_word) <= 16:
        shortEnough = True
    if len(p_word) >= 8:
        longEnough = True
    for char in p_word:
        if char.isupper():
            hasUpper = True
        if char.islower():
            hasLower = True
        if char.isdigit():
            hasNumber = True
        if char in specialChars:
            hasSpecial = True
    if shortEnough and longEnough and hasUpper and hasLower and hasNumber and hasSpecial:
        return True
    else:
        return False
while True:
    password = input('Enter your password: ')
    if checkPassword(password):
        print('Your password is valid.')
        break
    else:
        print('Your password is not valid. Please make sure your password meets the following criteria:')
        print('- A maximum of 16 characters')
        print('- A minimum of 8 characters')
        print('- A minimum of 1 upper case character')
        print('- A minimum of 1 lower case character')
        print('- A minimum of 1 number')
        print('- A minimum of 1 special character: \'~!#$%^*()_+-={}|[]\\:<>?,./')
        print('Please try again.\n')
