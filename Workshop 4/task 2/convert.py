'''
Define conversion factors as constants:
Define a function cm2inches(cm, rounding=2, addUnit=False) to convert centimeters to inches:
Multiply cm by 0.393 to get the result in inches.
If addUnit is True, append the unit "inches" to the result.
Round the result to the specified number of decimal places.
Return the result.
Define a function m2feet(m, rounding=2, addUnit=False) to convert meters to feet:
Multiply m by 3.281 to get the result in feet.
If addUnit is True, append the unit "feet" to the result.
Round the result to the specified number of decimal places.
Return the result.
Define a function m2yards(m, rounding=2, addUnit=False) to convert meters to yards:
Multiply m by 1.094 to get the result in yards.
If addUnit is True, append the unit "yards" to the result.
Round the result to the specified number of decimal places.
Return the result.
Define a function km2miles(km, rounding=2, addUnit=False) to convert kilometers to miles:
Multiply km by 0.621 to get the result in miles.
If addUnit is True, append the unit "miles" to the result.
Round the result to the specified number of decimal places.
    Return the result.


'''




MM_IN_INCH = 25.4 
MM_IN_FOOT = 304.8
MM_IN_YARD = 914.4
MM_IN_MILE = 1609344

def cm2inches(cm,rounding=2,addUnit=False):
    result = cm * 0.393
    if addUnit:
        return f"{round(result, rounding)} inches"
    return round(result, rounding)

def m2feet(m, rounding=2, addUnit=False):
    result = m * 3.281
    if addUnit:
        return f"{round(result, rounding)} feet"
    return round(result, rounding)

def m2yards(m, rounding=2, addUnit=False):
    result = m * 1.094
    if addUnit:
        return f"{round(result, rounding)} yards"
    return round(result, rounding)

def km2miles(km, rounding=2, addUnit=False):
    result = km * 0.621
    if addUnit:
        return f"{round(result, rounding)} miles"
    return round(result, rounding)