from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino1 = Dinosaur('Tyrannosaurus Rex', 60)
        dino2 = Dinosaur('Yriceratops', 50)
        dino3 = Dinosaur('Velociraptor', 40)
        self.dinosaurs = [dino1, dino2, dino3]
