'''Define a function named inputInt(prompt, errorMessage='Invalid input: integer required.', minValue=None, maxValue=None):
Start an endless loop:
Prompt the user with the provided prompt message.
Try to convert the user's input to an integer and store it in num_response.
On ValueError exception:
Print errorMessage.
Continue to the next iteration of the loop.
If minValue is not None and num_response < minValue:
Print Value below minimum error message.
Continue to the next iteration of the loop.
If maxValue is not None and num_response > maxValue:
Print Value above maximum error message.
Continue to the next iteration of the loop.
Return num_response.

Define a function named inputFloat(prompt, errorMessage='Invalid input: float required.', minValue=None, maxValue=None):
Start an endless loop:
Prompt the user with the provided prompt message.
Try to convert the user's input to a float and store it in float_response.
On ValueError exception:
Print errorMessage.
Continue to the next iteration of the loop.
If minValue is not None and float_response < minValue:
Print Value below minimum error message.
Continue to the next iteration of the loop.
If maxValue is not None and float_response > maxValue:
Print Value above maximum error message.
Continue to the next iteration of the loop.
Return float_response.'''
def inputInt(prompt, errorMessage='Invalid input: integer required.', minValue=None, maxValue=None):
    while True:
        try:
            response = input(prompt)
            num_response = int(response)
            if minValue is not None and num_response < minValue:
                print("Value below minimum: ", minValue)
                continue
            
            if maxValue is not None and num_response > maxValue:
                print("Value above maximum: ", maxValue)
                continue   
            return num_response
            
        except ValueError:
            print(errorMessage)

def inputFloat(prompt, errorMessage='Invalid input: float required.', minValue=None, maxValue=None):
    while True:
        try:
            response = input(prompt)
            float_response = float(response)
            if minValue is not None and float_response < minValue:
                print("Value below minimum: ", minValue)
                continue
            
            if maxValue is not None and float_response > maxValue:
                print("Value above maximum: ", maxValue)
                continue   
            return float_response
         
        except ValueError:
            print(errorMessage)