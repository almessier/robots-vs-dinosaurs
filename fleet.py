from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self):
        robot1 = Robot('R2-D2')
        robot2 = Robot('WALL-E')
        robot3 = Robot('Rosie')
        self.robots = [robot1, robot2, robot3]
