import pygame
from random import choice, randint, randrange


BG_COLOR = (250, 250, 120)
SCR_WIDTH, SCR_HEIGHT = 500, 500


class Bug:
    
    def __init__(self, size, minchange, maxchange):
        
        self.color = (randint(0, 50), randint(100, 200), randint(50, 100))
        self.size = size
        
        # random start position
        self.x = randrange(0, SCR_WIDTH - self.size, self.size)
        self.y = randrange(0, SCR_HEIGHT - self.size, self.size)
        
        # random direction
        self.dx = choice([-self.size, 0, self.size])
        self.dy = choice([-self.size, 0, self.size])
        
        # direction change frequency (every x turns)
        self.change = randint(minchange, maxchange)
        self.turn_count = 0
        
        self.alive = True
        
    
    def update(self, grid):
        
        # if next to the sticky center, or a bug stuck there, stop moving
        if (self.x - self.size, self.y) in grid or (self.x + self.size, self.y) in grid or \
                (self.x, self.y + self.size) in grid or (self.x, self.y - self.size) in grid:            
            
            self.alive = False
            
            grid[(self.x, self.y)] = self.color
            return
            
        # update position
        if self.x + self.dx >= 0 and self.x + self.dx <= SCR_WIDTH - self.size:
            self.x = (self.x + self.dx)
        if self.y + self.dy >= 0 and self.y + self.dy <= SCR_HEIGHT - self.size:
            self.y = (self.y + self.dy)
        
        
        # update turn count and if time to, change direction
        self.turn_count = (self.turn_count + 1) % self.change
        
        if self.turn_count == 0:
            self.dx = choice([-self.size, 0, self.size])
            self.dy = choice([-self.size, 0, self.size])
            
        return
    
       
    def draw(self, surf):
        pygame.draw.rect(surf, self.color, (self.x, self.y, self.size, self.size))


def run(swarm_size, bug_size, minchange, maxchange):
    # Initialize game and create screen object.
    pygame.init()
    screen = pygame.display.set_mode((SCR_WIDTH, SCR_HEIGHT))
    pygame.display.set_caption('SWARM ART!')
    
    swarm = [Bug(bug_size, minchange, maxchange) for x in range(swarm_size)]
    grid = {(SCR_WIDTH // 2 - (SCR_WIDTH // 2) % bug_size,
            SCR_HEIGHT // 2 - (SCR_HEIGHT // 2) % bug_size): (25, 150, 75)}
    
    running = True
        
    # Start the main loop for the game.
    while running:
        
        screen.fill(BG_COLOR)
         
        for bug in swarm:
            bug.update(grid)
            bug.draw(screen)
            # delete dead bugs after drawn to speed things up:
            if not bug.alive:
                swarm.remove(bug)
        
        for pos, col in grid.items():
            pygame.draw.rect(screen, col, (pos[0], pos[1], bug_size, bug_size))
        
                
            
    
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               running = False
        
        # Make the most recently drawn screen visible
        pygame.display.flip()


# cool numbers:
# swarmsize=1000, bugsize=5, minchange=5, maxchange=10
# 200, 20, 1, 10
# best so far: 10000, 2, 1, 10   looks like a plant growing and eating the bugs!

run(10000, 2, 1, 10)
