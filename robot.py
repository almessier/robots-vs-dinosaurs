from weapon import Weapon


class Robot:
    def __init__(self, name):
        laser_sword = Weapon('laser sword', 50)
        self.name = name
        self.health = 100
        self.weapon = laser_sword

    def attack(self, dinosaur):
        dinosaur.health = dinosaur.health - self.weapon.attack_power

    def assign_weapon():
        pass
