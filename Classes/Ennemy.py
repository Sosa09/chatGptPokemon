from Player import Player
class Ennemy(Player):
    def __init__(self):
        super().__init__()
        self.image.fill("red");
        self.rect.topleft = (100,200)