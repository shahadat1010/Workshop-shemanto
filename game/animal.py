# animal.py

import random

class Animal:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def attack(self):
        return random.randint(0, self.damage)
