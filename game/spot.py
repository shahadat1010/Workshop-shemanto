# spot.py

class Spot:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.animal = None
        self.weapon = None
        self.food = None
        self.water = None

    def set_animal(self, animal):
        self.animal = animal

    def set_weapon(self, weapon):
        self.weapon = weapon

    def set_food(self, food):
        self.food = food

    def set_water(self, water):
        self.water = water

    def get_animal(self):
        return self.animal

    def get_weapon(self):
        return self.weapon

    def get_food(self):
        return self.food

    def get_water(self):
        return self.water

    def has_animal(self):
        return self.animal is not None

    def has_weapon(self):
        return self.weapon is not None

    def has_food(self):
        return self.food is not None

    def has_water(self):
        return self.water is not None

    def describe(self):
        print(self.description)
