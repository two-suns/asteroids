import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    my_clock = pygame.time.Clock()
    dt = 0
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, radius=PLAYER_RADIUS)
    
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        
        dt = my_clock.tick(60) / 1000 # Calculate delta time (always after updates)
        # Update the game state (before rendering)    
        updatable.update(dt) # Update the player's rotation and other state
        
        
        # Render the updated state to the screen    
        screen.fill((0,0,0))
        drawable.draw(screen)
        pygame.display.flip()
            

if __name__ == "__main__":
    main()