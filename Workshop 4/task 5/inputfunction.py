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