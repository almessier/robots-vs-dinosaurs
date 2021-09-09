from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.display_welcome()
        self.battle()
        self.display_winners()

    def display_welcome(self):
        print('Welcome to Robots vs Dinosaurs!')

    def battle(self):
        while(True):
            # Receive dinosaur attack from user and validate it
            valid = False
            while(valid == False):
                user_dino_index = input(
                    'Which dinosaur do you want to attack with? Type 1 for Tyrannosaurus rex, 2 for Triceratops, and 3 for Velociraptor: ')
                if (user_dino_index != 1 or 2 or 3):
                    print('Invalid input, Type 1, 2, or 3')
                elif (self.herd.dinosaurs[int(user_dino_index) - 1].health <= 0):
                    print('That dinosaur is dead! Pick another dinosaur.')
                else:
                    valid = True

            user_dino = self.herd.dinosaurs[int(user_dino_index) - 1]
            self.dino_turn(user_dino)

            # Checks if all robots are 0 health
            count = 0
            for obj in self.fleet.robots:
                if obj.health <= 0:
                    count += 1
            if count == 3:
                break

            # Receive robot attack from user and validate it
            valid = False
            while(valid == False):
                user_robo_index = input(
                    'Which robot do you want to attack with? Type 1 for R2-D2, 2 for WALL-E, and 3 for Rosie: ')
                if (user_robo_index != 1 or 2 or 3):
                    print('Invalid input, Type 1, 2, or 3')
                elif (self.fleet.robots[int(user_robo_index) - 1].health <= 0):
                    print('That robot is dead! Pick another robot.')
                else:
                    valid = True

            user_robo = self.fleet.robots[int(user_robo_index) - 1]
            self.robo_turn(user_robo)

            # Checks if all dinosaurs are 0 health
            count = 0
            for obj in self.herd.dinosaurs:
                if obj.health <= 0:
                    count += 1
            if count == 3:
                break

    def dino_turn(self, dinosaur):
        self.show_dino_opponent_options()

        user_attack = input(': ')
        dinosaur.attack(self.fleet.robots[int(user_attack) - 1])

        # Print results of attack
        print(
            f'{dinosaur.name} attacked {self.fleet.robots[int(user_attack) - 1].name} for {dinosaur.attack_power}')
        if self.fleet.robots[int(user_attack) - 1].health <= 0:
            print(
                f'{self.fleet.robots[int(user_attack) - 1].name} has been defeated!')

    def robo_turn(self, robot):
        self.show_robo_opponent_options()

        user_attack = input(': ')
        robot.attack(self.herd.dinosaurs[int(user_attack) - 1])

        # Print results of attack
        print(
            f'{robot.name} attacked {self.herd.dinosaurs[int(user_attack) - 1].name} for {robot.weapon.attack_power}')
        if self.herd.dinosaurs[int(user_attack) - 1].health <= 0:
            print(
                f'{self.herd.dinosaurs[int(user_attack) - 1].name} has been defeated!')

    def show_dino_opponent_options(self):
        print('Attack! 1 for R2-D2, 2 for WALL-E, and 3 for Rosie.')

    def show_robo_opponent_options(self):
        print('Attack! 1 for Tyrannosaurus Rex, 2 for Triceratops, and 3 for Velociraptor.')

    def display_winners(self):
        count = 0
        for obj in self.fleet.robots:
            if obj.health <= 0:
                count += 1
        if count == 3:
            print('The dinosaurs have defeated the robots!')
        else:
            print('The robots have defeated the dinosaurs!')
