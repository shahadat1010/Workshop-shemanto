# utils.py

import random

def roll_dice(chance):
    """
    Simulate rolling a dice to determine if an event occurs based on a given chance.
    Args:
        chance (float): The probability of the event occurring (0.0 to 1.0).
    Returns:
        bool: True if the event occurs, False otherwise.
    """
    return random.random() < chance
