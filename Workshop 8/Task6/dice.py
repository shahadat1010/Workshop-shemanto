"""
Class: DicePile
    __init__(initQuantity, initSides):
        Initialize quantity, sides, results to None, rolled to False, and rollCount to 0
    
    __str__():
        If rolled, convert results to string, else set resultString to 'not rolled'
        Generate dicescription
        Return dicescription + ': ' + resultString
    
    roll():
        Clear results list
        Loop over quantity:
            Append random integer between 1 and sides to results
        Set rolled to True
        Increment rollCount by 1
    
    getResults():
        Return results
    
    setQuantity(newQuantity):
        If newQuantity < 1, raise ValueError
        Set quantity to newQuantity, results to None, and rolled to False
    
    setSides(newSides):
        If newSides < 2, raise ValueError
        Set sides to newSides, results to None, and rolled to False
    
    dicescription():
        Return "<quantity>d<sides>"
    
    getRollCount():
        Return rollCount
    
    maxTotal():
        If not rolled, raise AttributeError, else return quantity * sides
    
    getAverage():
        If not rolled, raise AttributeError, else return sum of results divided by quantity
    
    sortResults():
        If not rolled, raise AttributeError, else sort results in ascending order
    
If executed as main program:
    Create DicePile object with quantity 4 and sides 6
    Roll dice
    Print dice description
    Print DicePile object
    Print maximum total possible
    Print average result of rolls
    Print results before sorting
    Sort results
    Print results after sorting

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

    def maxTotal(self):
        if not self.rolled:
            raise AttributeError("Dice haven't been rolled yet")
        return self.__quantity * self.__sides

    def getAverage(self):
        if not self.rolled:
            raise AttributeError("Dice haven't been rolled yet")
        return sum(self.__results) / self.__quantity

    def sortResults(self):
        if not self.rolled:
            raise AttributeError("Dice haven't been rolled yet")
        self.__results.sort()

# Test the DicePile class
if __name__ == "__main__":
    myDice = DicePile(4, 6)
    myDice.roll()
    print("Dice description:", myDice.dicescription())
    print("Dice object:", myDice)
    print("Max total:", myDice.maxTotal())
    print("Average result:", myDice.getAverage())
    print("Results before sorting:", myDice.getResults())
    myDice.sortResults()
    print("Results after sorting:", myDice.getResults())
