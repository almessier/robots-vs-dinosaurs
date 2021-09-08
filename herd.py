from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []
        self.create_herd()

    def create_herd(self):
        dino1 = Dinosaur('tyrannosaurus rex', 30)
        dino2 = Dinosaur('triceratops', 25)
        dino3 = Dinosaur('velociraptor', 20)
        self.dinosaurs = [dino1, dino2, dino3]
