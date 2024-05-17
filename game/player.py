# player.py

class Player:
    def __init__(self, name):
        self.name = name
        self.energy = 100
        self.hydration = 100
        self.inventory = []
        self.current_location = None

    def display_status(self):
        print(f"Player: {self.name}")
        print(f"Energy: {self.energy}")
        print(f"Hydration: {self.hydration}")
        print("Inventory:", self.inventory)

    def reduce_energy(self, amount):
        self.energy -= amount
        if self.energy < 0:
            self.energy = 0

    def reduce_hydration(self, amount):
        self.hydration -= amount
        if self.hydration < 0:
            self.hydration = 0

    def rest(self):
        self.energy += 20
        if self.energy > 100:
            self.energy = 100

    def eat_food(self, food):
        self.energy += food.energy_value
        self.hydration += food.hydration_value
        self.inventory.remove(food)

    def drink_water(self, water):
        self.hydration += water.hydration_value
        self.inventory.remove(water)

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def set_current_location(self, location):
        self.current_location = location

    def get_current_location(self):
        return self.current_location
