"""
DicePile Class:
    Constructor:
        Initialize quantity, sides, and results attributes.

    Method __str__:
        If results exist:
            Convert results to string.
        Else:
            Set resultString to 'not rolled'.
        Concatenate quantity, sides, and resultString.
        Return the concatenated string.

    Method roll:
        Clear results list.
        Loop for each die in the quantity:
            Generate a random number between 1 and the number of sides.
            Add the number to the results list.

    Method getResults:
        Return the results list.

    Method getQuantity:
        Return the quantity attribute.

    Method getSides:
        Return the sides attribute.

    Method setQuantity:
        Update the quantity attribute.

    Method setSides:
        Update the sides attribute.

"""

import random

class DicePile:
    def __init__(self, initQuantity, initSides): 
        self.setQuantity(initQuantity)
        self.setSides(initSides)
        self.__results = None

    def __str__(self): 
        if self.__results is not None:
            resultString = str(self.__results)
        else:
            resultString = 'not rolled'
        dicescription = str(self.__quantity) + 'd' + str(self.__sides)
        return dicescription + ': ' + resultString

    def roll(self): 
        self.__results = [] 
        for i in range(self.__quantity): 
            self.__results.append(random.randint(1, self.__sides))

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

    def setSides(self, newSides):
        if int(newSides) < 2:
            raise ValueError('dice sides cannot be less than 2')
        else:
            self.__sides = int(newSides)
            self.__results = None
