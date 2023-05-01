import pygame, sys
from Trainer import Trainer
from Ennemy import Ennemy
class Game:
    screen = None

    def __init__(self, size, map):
        self.size = size; #size should be e.g 1080,1920 (pixels) 
        self.map = map #image
        self.position = pygame.Vector2(80, 80)
        self.clock = pygame.time.Clock()
        self.shape = None #can be anything image, square, polygon (triangle), circle, rect
        self.t = Trainer()
        self.e = Ennemy()
        self.groups = pygame.sprite.Group()
        self.groups.add(self.t)
        self.groups.add(self.e)
    
    # initialize th pygame and set size and fps of the screen 
    def _start_view(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Pokemon")
        
    # Load all images, sound, fonts ...
    def load_asset(self):
        pass #no assets yet just working with shapes



#define the game loop in which you will play
    def start_game_loop(self):
        running = True
        self._start_view()

        while(running):
            # this for loop is necessary to read or handle events ! without it the keypress event wont work
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.update()
        
            self.screen.fill("white")
            self.groups.update()
            self.groups.draw(self.screen)
       
            
            if pygame.sprite.collide_rect(self.t, self.e):
                running = False;
                self._start_battle_loop()
         
            #set the fps at 60
            self.dt = self.clock.tick(120)
    def _start_battle_loop(self):
         # begin battle
        # Create a font object
        font = pygame.font.SysFont("Arial", 30)

        # Render the text
        text_surface = font.render("Hello, pygame!", True, (0, 0, 0))

        # Position the text
        text_rect = text_surface.get_rect()
        text_rect.center = (400, 300)
     

        self.screen.fill("white");
        self.screen.blit(text_surface, text_rect)
        self.groups.remove(1)
        pygame.display.flip()


        
        
        
game = Game((800,600), "")
game.start_game_loop()
