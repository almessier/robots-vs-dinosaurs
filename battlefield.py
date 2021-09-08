from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        herd = Herd()
        herd.create_herd()
        fleet = Fleet()
        fleet.create_fleet()
        self.display_welcome()
        self.battle()

    def display_welcome(self):
        print('Welcome to Robots vs Dinosaurs!')

    def battle(self):
        user_dino = input(
            'Which dinosaur do you want to attack with? Type 1 for tyrannosaurus rex, 2 for triceratops, and 3 for velociraptor.')
        self.dino_turn(user_dino)
        user_robo = input(
            'Which robot do you want to attack with? Type 1 for R2-D2, 2 for WALL-E, and 3 for Rosie.')
        self.robo_turn(user_robo)

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass
