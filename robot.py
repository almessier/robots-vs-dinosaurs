from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.power_level = 9000
        self.weapon = Weapon('Laser Sword', 50)

    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_power
