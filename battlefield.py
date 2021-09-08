from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle()

    def display_welcome(self):
        print('Welcome to Robots vs Dinosaurs!')

    def battle(self):
        while():
            user_dino_index = input(
                'Which dinosaur do you want to attack with? Type 1 for tyrannosaurus rex, 2 for triceratops, and 3 for velociraptor: ')
            user_dino = self.herd.dinosaurs[int(user_dino_index) - 1]
            self.dino_turn(user_dino)

            user_robo_index = input(
                'Which robot do you want to attack with? Type 1 for R2-D2, 2 for WALL-E, and 3 for Rosie: ')
            user_robo = self.fleet.robots[int(user_robo_index) - 1]
            self.robo_turn(user_robo)
        self.display_winners()

    def dino_turn(self, dinosaur):
        self.show_dino_opponent_options()
        user_attack = input(': ')
        dinosaur.attack(self.fleet.robots[int(user_attack) - 1])

    def robo_turn(self, robot):
        self.show_robo_opponent_options()
        user_attack = input(': ')
        robot.attack(self.herd.dinosaurs[int(user_attack) - 1])

    def show_dino_opponent_options(self):
        print('Attack! 1 for R2-D2, 2 for WALL-E, and 3 for Rosie.')

    def show_robo_opponent_options(self):
        print('Attack! 1 for tyrannosaurus rex, 2 for triceratops, and 3 for velociraptor.')

    def display_winners(self):
        pass
