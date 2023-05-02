from Player import Player
import pygame, sys
class Trainer(Player):
    def __init__(self, name):
        super().__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("./Assets/trainers/ash.png"), (50,50))
        self.rect.topleft = (10,10)
        self.name = name
        
    def update(self):
        #handle user key pressed events and set colission detection to not pass the screen size !
        keys = pygame.key.get_pressed()
        if keys[pygame.K_DOWN]:
            #get the rect of the user if it is less or equal to  the size of the screen - the size of the shape then go down 
            if self.rect.y <= (600 - self.rect.height):
                self.rect.y += 1
                # if pygame.sprite.collide_rect()
        elif keys[pygame.K_UP]:
            # get the rect of the player if it is greater or equal the it self comparing the size of the screen then go up
            if self.rect.y >= 10:
                self.rect.y -= 1
        elif keys[pygame.K_RIGHT]:
            if self.rect.x <= (800 - self.rect.width): #10 equals the size of the object
                self.rect.x += 1
        elif keys[pygame.K_LEFT]:
            if self.rect.x >= 10: #10 equals the size of the object
                self.rect.x -= 1
