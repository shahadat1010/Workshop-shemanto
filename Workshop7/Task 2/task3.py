def checkPassword(pword):
    # Define special characters
    specialChars = '\'~!#$%^*()_+-={}|[]\\:<>?,./'
    
    # Check length criteria
    if len(pword) > 16 or len(pword) < 8:
        return False
    
    # Initialize boolean variables to False
    hasUpper = False
    hasLower = False
    hasNumber = False
    hasSpecial = False
    
    # Check other criteria
    for char in pword:
        if not hasUpper and char.isupper():
            hasUpper = True
        if not hasLower and char.islower():
            hasLower = True
        if not hasNumber and char.isdigit():
            hasNumber = True
        if not hasSpecial and char in specialChars:
            hasSpecial = True
        
        # If all criteria are met, return True
        if hasUpper and hasLower and hasNumber and hasSpecial:
            return True
    
    # If the loop completes and all criteria are not met, return False
    return False

# Test the password validity
password = input('Enter your password: ')
if checkPassword(password):
    print('Your password is valid.')
else:
    print('Your password is not valid.')
