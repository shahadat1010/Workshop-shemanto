class Player:
    def __init__(self, name, swim, climb, exhaustion):
        self.name = name
        self.swim = swim
        self.climb = climb
        self.exhaustion = exhaustion

    def display_status(self):
        print(f"Name: {self.name}")
        print(f"Swim: {'Yes' if self.swim else 'No'}")
        print(f"Climb: {'Yes' if self.climb else 'No'}")
        print(f"Exhaustion: {self.exhaustion}")
