"""
Initialize(initQuantity: integer, initSides: integer): void
    Initialize __quantity and __sides with initQuantity and initSides respectively
    Set __results to None
    Set __rollCount to 0
    Set rolled to False
 ToString(): string
    If dice have been rolled (rolled is True):
        Convert __results to string and store in resultString
    Else:
        Set resultString to 'not rolled'
    Create a description string by concatenating __quantity, 'd', and __sides
    Return description string followed by resultString and roll count
 Roll(): void
    Clear __results list
    Repeat for each die in the pile:
        Generate a random number between 1 and __sides (inclusive) and append to __results
    Increment __rollCount by 1
    Set rolled to True
 GetResults(): list
    Return __results
 GetQuantity(): integer
    Return __quantity
 GetSides(): integer
    Return __sides
 SetQuantity(newQuantity: integer): void
    If newQuantity is less than 1:
        Raise ValueError with message 'dice quantity cannot be less than 1'
    Else:
        Set __quantity to newQuantity
        Set __results to None
        Set rolled to False
 SetSides(newSides: integer): void
    If newSides is less than 2:
        Raise ValueError with message 'dice sides cannot be less than 2'
    Else:
        Set __sides to newSides
        Set __results to None 
        Set rolled to False
 GetRollCount(): integer
    Return __rollCount
"""

import random

class DicePile:
    def __init__(self, initQuantity, initSides): 
        self.setQuantity(initQuantity)
        self.setSides(initSides)
        self.__results = None
        self.__rollCount = 0
        self.rolled = False 
    def __str__(self): 
        if self.rolled:  
            resultString = str(self.__results)
        else:
            resultString = 'not rolled'
        dicescription = str(self.__quantity) + 'd' + str(self.__sides)
        return dicescription + ': ' + resultString + f" (roll count: {self.__rollCount})"

    def roll(self): 
        self.__results = [] 
        for i in range(self.__quantity): 
            self.__results.append(random.randint(1, self.__sides))
        self.__rollCount += 1  
        self.rolled = True  

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

    def getRollCount(self):
        return self.__rollCount
