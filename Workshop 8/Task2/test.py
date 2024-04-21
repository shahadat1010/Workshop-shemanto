"""
 create an object
 call the roll method
 use the __str__ method
 change the quantity
 change the sides
 notice the results are now None
 roll the dice again
 show the results
"""
import dice

myDice = dice.DicePile(4, 6) 
myDice.roll() 
print(myDice) 
myDice.setQuantity(8) 
myDice.setSides(20) 
print(myDice.getResults()) 
myDice.roll() 
print(myDice.getResults()) 
