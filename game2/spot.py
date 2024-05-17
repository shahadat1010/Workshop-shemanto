import random

class Spot:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display_description(self):
        print(self.description)

    def explore(self):
        print(f"You are exploring {self.name}...")
        found_food = random.random() < 0.18
        if found_food:
            print("You found some food!")
        else:
            print("You didn't find any food.")

    def collect_water(self):
        print(f"You are collecting water from {self.name}...")
        print("You collected some water.")
