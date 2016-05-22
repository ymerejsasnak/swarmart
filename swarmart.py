import pygame
from random import randint


BG_COLOR = (220, 220, 220)
SCR_WIDTH, SCR_HEIGHT = 500, 500
BUG_SIZE = 5
BUG_COLOR = (0, 0, 0)


class Bug:
    
    def __init__(self):
        self.x = randint(0, SCR_WIDTH - BUG_SIZE)
        self.y = randint(0, SCR_HEIGHT - BUG_SIZE)
        self.dx = randint(-1, 1)
        self.dy = randint(-1, 1)
    
    def move(self):
        self.x = (self.x + self.dx) % SCR_WIDTH
        self.y = (self.y + self.dy) % SCR_HEIGHT
        
        self.dx = randint(-1, 1)
        self.dy = randint(-1, 1)
    
    def draw(self, surf):
        pygame.draw.rect(surf, BUG_COLOR, (self.x, self.y, BUG_SIZE, BUG_SIZE))
        

def run():
    # Initialize game and create screen object.
    pygame.init()
    screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    pygame.display.set_caption('SWARM ART!')
    
    swarm = [Bug() for x in range(100)]
    
    running = True
    
    screen.fill(BG_COLOR)
    
    # Start the main loop for the game.
    while running:
    
        
        
        for bug in swarm:
            bug.move()
            bug.draw(screen)
    
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False
        
        # Make the most recently drawn screen visible
        pygame.display.flip()

run()
