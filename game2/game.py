from player import Player
import random
from spot import Spot
from weapon import Weapon
from animal import Animal
from ui import UI
from utils import calculate_exhaustion, generate_random_event, generate_random_number

class Game:
    def __init__(self):
        self.player = None
        self.spots = []
        self.weapons = []
        self.animals = []

    def create_player(self):
        name = input("Enter your name: ")
        swim = UI.get_yes_no("Are you good at swimming? (yes/no): ")
        climb = UI.get_yes_no("Are you good at climbing? (yes/no): ")
        exhaustion = calculate_exhaustion(0)
        self.player = Player(name, swim, climb, exhaustion)
        print("Player created successfully.")

    def create_spots(self):
        self.spots = [
            Spot("Crash Site", "You have crashed in the ocean."),
            Spot("Beach", "You are on a sandy beach."),
            Spot("Jungle", "You are in a dense jungle."),
            Spot("River", "You are at the riverbank."),
            Spot("Mountains", "You are in the mountains.")
        ]
        print("Spots created successfully.")

    def create_weapons(self):
        self.weapons = [
            Weapon("Spear", "A sharp spear."),
            Weapon("Wooden Weapon", "A sturdy wooden weapon."),
            Weapon("Rock", "A heavy rock.")
        ]
        print("Weapons created successfully.")

    def create_animals(self):
        self.animals = [
            Animal("Snake", "A venomous snake.", 10),
            Animal("Turtle", "A large turtle.", 8),
            Animal("Bird", "A colorful bird.", 6)
        ]
        print("Animals created successfully.")

    def explore_spot(self, spot):
        spot.display_description()
        event = generate_random_event()
        if event == "found_food":
            print("You found some food!")
        elif event == "found_weapon":
            print("You found a weapon!")
        elif event == "found_animal":
            print("You encountered an animal!")
            self.attack_animal(random.choice(self.animals))

    def attack_animal(self, animal):
        print(f"You are being attacked by a {animal.name}!")
        if UI.get_yes_no("Do you want to fight? (yes/no): "):
            # Determine outcome of the fight
            player_attack = generate_random_number(1, 10) + (self.player.swim * 2)
            if player_attack >= animal.attack_power:
                print("You defeated the animal!")
            else:
                print("You were defeated by the animal!")
                self.player.exhaustion = 10 * animal.attack_power
        else:
            print("You ran away from the animal.")

    def run(self):
        print("Welcome to the Survival Game!")
        self.create_player()
        self.create_spots()
        self.create_weapons()
        self.create_animals()

        while True:
            print("\nCurrent Player Status:")
            self.player.display_status()
            print("\nChoose an action:")
            UI.display_menu(["Explore spot", "Collect water","Drink Water","Rest", "Quit"])
            choice = UI.get_choice("Enter your choice: ", 5)
            if choice == 1:
                self.explore_spot(random.choice(self.spots))
            elif choice == 2:
                print("You are collecting water...")
                self.player.exhaustion += 2
                print("You collected some water.")
        
            elif choice == 3:
                print("You are Drinking water...")
                self.player.exhaustion -= 2
                if self.player.exhaustion<0:
                    self.player.exhaustion=0
                print("You collected some water.")   
            elif choice == 4:
                self.player.exhaustion -= 10
                if self.player.exhaustion<0:
                    self.player.exhaustion = 0        
                print("You Took Rest.")           
            elif choice == 5:
                print("Goodbye!")
                break

if __name__ == "__main__":
    game = Game()
    game.run()
