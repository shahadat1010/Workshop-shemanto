"""
Define a class named DicePile:
    Define the __init__ method to initialize the DicePile object with quantity, sides, and results attributes.
        Set the initial rolled attribute to False.
    
    Define the __str__ method to return a string representation of the DicePile object.
        If the dice have been rolled, convert the results to a string; otherwise, set the result string to 'not rolled'.
        Return the description of the dice (quantity and sides) followed by the result string.

    Define a method named roll to simulate rolling the dice.
        Generate random numbers for each die and store them in the results attribute.
        Set the rolled attribute to True.

    Define methods to get the results, quantity, and sides attributes of the DicePile object.

    Define methods to set the quantity and sides attributes of the DicePile object.
        Ensure that the new quantity and sides are valid integers and update the results attribute accordingly.
        Set the rolled attribute to False after updating the quantity or sides.

    Define a method named dicescription to return a string describing the quantity and sides of the DicePile object.

    Define a method named getRollCount to get the roll count attribute.

Test the DicePile class:
    Create a DicePile object with initial quantity 4 and sides 6.
    Print the description of the dice using the dicescription method.
    Print the DicePile object using the __str__ method.

"""

import random

class DicePile:
    def __init__(self, initQuantity, initSides): 
        self.setQuantity(initQuantity)
        self.setSides(initSides)
        self.__results = None
        self.rolled = False  
        self.__rollCount = 0  

    def __str__(self): 
        if self.rolled:
            resultString = str(self.__results)
        else:
            resultString = 'not rolled'
        return self.dicescription() + ': ' + resultString

    def roll(self): 
        self.__results = [] 
        for i in range(self.__quantity): 
            self.__results.append(random.randint(1, self.__sides))
        self.rolled = True  
        self.__rollCount += 1  

    def getResults(self): 
        return self.__results

    def getQuantity(self):
        return self.__quantity

    def getSides(self):
        return self.__sides

    def setQuantity(self, newQuantity): 
        if int(newQuantity) < 1:
            raise ValueError('dice quantity cannot be less than 1')
        else:
            self.__quantity = int(newQuantity)
            self.__results = None
            self.rolled = False  

    def setSides(self, newSides):
        if int(newSides) < 2:
            raise ValueError('dice sides cannot be less than 2')
        else:
            self.__sides = int(newSides)
            self.__results = None 
            self.rolled = False  

    def dicescription(self):
        return str(self.__quantity) + 'd' + str(self.__sides)

    def getRollCount(self):
        return self.__rollCount  

# Test the DicePile class
if __name__ == "__main__":
    myDice = DicePile(4, 6)
    myDice.roll()
    print(myDice)
    print(myDice.getResults())
    print(myDice.getRollCount())  
