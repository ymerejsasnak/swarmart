import pygame
from random import randint


BG_COLOR = (250, 250, 120)
SCR_WIDTH, SCR_HEIGHT = 500, 500


class Bug:
    
    def __init__(self, size, minchange, maxchange):
        
        self.color = (randint(0, 50), randint(100, 200), randint(50, 100))
        self.size = size
        
        # random start position
        self.x = randint(0, SCR_WIDTH - self.size)
        self.y = randint(0, SCR_HEIGHT - self.size)
        
        # random direction
        self.dx = randint(-1, 1)
        self.dy = randint(-1, 1)
        
        # direction change frequency (every x turns)
        self.change = randint(minchange, maxchange)
        self.turn_count = 0
        
        # randomish color
        
    
    def update(self):
        
        # update position
        self.x = (self.x + self.dx)
        self.y = (self.y + self.dy)
        
        # make sure it stays in bounds
        if self.x < 0:
            self.x = 0
        elif self.x > SCR_WIDTH - self.size - 1:
            self.x = SCR_WIDTH - self.size - 1
        
        if self.y < 0:
            self.y = 0
        elif self.y > SCR_HEIGHT - self.size - 1:
            self.y = SCR_HEIGHT - self.size - 1
        
        # update turn count and if time to, change direction
        self.turn_count = (self.turn_count + 1) % self.change
        
        if self.turn_count == 0:
            self.dx = randint(-1, 1)
            self.dy = randint(-1, 1)
    
    def draw(self, surf):
        pygame.draw.rect(surf, self.color, (self.x, self.y, self.size, self.size))
        

def run(swarm_size, bug_size, minchange, maxchange):
    # Initialize game and create screen object.
    pygame.init()
    screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    pygame.display.set_caption('SWARM ART!')
    
    swarm = [Bug(bug_size, minchange, maxchange) for x in range(swarm_size)]
    
    running = True
    
    # Start the main loop for the game.
    while running:
        
        screen.fill(BG_COLOR)        
        
        for bug in swarm:
            bug.update()
            bug.draw(screen)
    
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False
        
        # Make the most recently drawn screen visible
        pygame.display.flip()


# cool numbers:
# swarmsize=200, bugsize=3, minchange=1, maxchange=100
# swarmsize=2000, bugsize=20, minchange=5, maxchange=10

run(2000, 20, 5, 10)
