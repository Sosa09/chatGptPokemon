import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.rect = self.image.get_rect();
        self.name = name
    # reset player position
    def reset(self):
        pass