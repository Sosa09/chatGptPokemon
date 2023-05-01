import pygame, sys

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.rect = self.image.get_rect();

    # reset player position
    def reset(self):
        pass