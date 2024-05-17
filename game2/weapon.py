class Weapon:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display_description(self):
        print(self.description)
