# game.py

from player import Player
from spot import Spot
from ui import UI
from utils import roll_dice

class Game:
    def __init__(self):
        self.player = Player()
        self.current_spot = Spot()
    
    def start(self):
        UI.display_message("Welcome to the Island Survival Game!")
        UI.display_message("Your plane has crashed on a deserted island.")
        UI.display_message("Your goal is to survive and find a way to escape.")

        while not self.player.is_dead() and not self.player.has_found_boat():
            self.current_spot.visit(self.player)
            self.player.consume_resources()

            if self.player.is_dead():
                UI.display_message("Game over! You died.")
                break

            if self.player.has_found_boat():
                UI.display_message("Congratulations! You found a boat and escaped the island.")
                break

            self.current_spot = Spot()

if __name__ == "__main__":
    game = Game()
    game.start()
