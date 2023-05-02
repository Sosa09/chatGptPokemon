import pygame, sys
from Trainer import Trainer
from Ennemy import Ennemy
class Game:
    screen = None
    collidedItem = None
    def __init__(self, size, map):
        self.size = size; #size should be e.g 1080,1920 (pixels) 
        self.map = map #image
        self.position = pygame.Vector2(80, 80)
        self.clock = pygame.time.Clock()
        self.shape = None #can be anything image, square, polygon (triangle), circle, rect
        self.t = Trainer("Ash")
        self.e = []
        self.groups = pygame.sprite.Group()
        self.groups.add(self.t)
        self._load_asset()
    
    # initialize th pygame and set size and fps of the screen 
    def _start_view(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("Pokemon")
        
    # Load all images, sound, fonts ...
    def _load_asset(self):
        self.e.append(Ennemy("./Assets/pokemons/bullbizar.png", "Bullbizar"))
        self.e.append(Ennemy("./Assets/pokemons/eve.png", "Eve"))
        self.e.append(Ennemy("./Assets/pokemons/squirtle.png", "Squirtle"))
        for x in self.e:
            self.groups.add(x)



#define the game loop in which you will play
    def start_game_loop(self):
        running = True
        self._start_view()
        #loop through the game to until battle begins or user quit game
        while(running):
            # this for loop is necessary to read or handle events ! without it the keypress event wont work
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            #update the view
            pygame.display.update()
            #fill the background in white
            self.screen.fill("white")
            #update all sprite elements
            self.groups.update()
            #draw all sprite elements
            self.groups.draw(self.screen)
       
            # check if the player collide with on of the elements
            for x in self.e: 
                if pygame.sprite.collide_rect(self.t, x):
                    running = False;
                    self.collidedItem = x
                    self._start_battle_loop()
         
            #set the fps at 60
            self.dt = self.clock.tick(120)
    def _start_battle_loop(self):
        # begin battle
        battleState = True
        try:
            while(battleState): 
                # Create a font object
                font = pygame.font.SysFont("Arial", 30)

                # Render the text
                text_surface = font.render(f"Battle Begins!\nTrainer: Ash VS {self.collidedItem.name}", True, (0, 0, 0))

                # Position the text
                text_rect = text_surface.get_rect()
                text_rect.center = (400, 300)
                # Fill the background in white
                self.screen.fill("white");
                # draw it on the screen
                self.screen.blit(text_surface, text_rect)
           
                #update the display
                pygame.display.update()
                
                keys = pygame.key.get_pressed()
                if keys[pygame.MOUSEBUTTONDOWN]:    
                    #remove element after it has collided
                    self.groups.remove(self.collidedItem)
                    # Update groups
                    self.groups.update()
                    battleState = False
                  
        except Exception as e:
            print(e);
    
     
game = Game((800,600), "")
game.start_game_loop()
