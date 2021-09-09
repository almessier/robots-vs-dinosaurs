from robot import Robot
from weapon import Weapon


class Fleet:
    def __init__(self):
        self.robots = []
        self.create_fleet()

    def create_fleet(self):
        robot1 = Robot('R2-D2')
        robot2 = Robot('WALL-E')
        robot3 = Robot('Rosie')
        self.robots = [robot1, robot2, robot3]

    def assign_weapons(self):
        weapon1 = Weapon('Orbital Ion Cannon', 60)
        weapon2 = Weapon('Laser Sword', 50)
        weapon3 = Weapon('Radiation Gun', 40)
        weapons = [weapon1, weapon2, weapon3]

        for robo in self.robots:
            valid = False
            while(valid == False):
                user_input = input(
                    f'Which weapon do you want on {robo.name}? Type 1 for Oribital Ion Cannon, 2 for Laser Sword, or 3 for Radiation Gun. ')
                if int(user_input) == 1:
                    robo.weapon = weapons[0]
                    valid = True
                elif int(user_input) == 2:
                    robo.weapon = weapons[1]
                    valid = True
                elif int(user_input) == 3:
                    robo.weapon = weapons[2]
                    valid = True
                else:
                    print('Invalid input, try again.')
