from Player import Player
import pygame
import random
class Ennemy(Player):
    def __init__(self, image, name):
        super().__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(image), (50,50))
        self.rect.bottomright = (random.randrange(100, 600),random.randrange(100, 600))
        self.name = name