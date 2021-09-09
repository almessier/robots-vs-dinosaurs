class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = name
        self.health = 100
        self.energy = 100
        self.attack_power = attack_power
        self.attacks = ('Charge', 'Bite', 'Tail Whip')

    def attack(self, robot):
        robot.health = robot.health - self.attack_power
