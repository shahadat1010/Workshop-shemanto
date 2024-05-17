class Animal:
    def __init__(self, name, description, attack_power):
        self.name = name
        self.description = description
        self.attack_power = attack_power

    def display_description(self):
        print(self.description)
