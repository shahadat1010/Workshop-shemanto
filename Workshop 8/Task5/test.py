"""
Create a DicePile object
Roll the dice
Print the DicePile object using __str__ method
Change the quantity
Change the sides
Print the results (will be None since the dice haven't been rolled again)
Roll the dice again
Print the results
Print the roll count
"""
import random
import dice


myDice = dice.DicePile(4, 6)
myDice.roll()
print(myDice)
myDice.setQuantity(8)
myDice.setSides(20)
print(myDice.getResults())
myDice.roll()
print(myDice.getResults())
print(myDice.getRollCount())
