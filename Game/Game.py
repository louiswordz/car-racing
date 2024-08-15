# import gaming libraries
import pygame
import sys

class Racing:
    """A class that models the assets and properties of our game"""
    def __init__(self):
        """Initialize  game function"""
        pygame.init()
        
        # Set screen size
        self.screen = pygame.display.set_mode((700, 500))
        pygame.display.set_caption("Car Racing")
        
        self.bg_color = (0, 255, 0)
        
    def run_game(self):
        """Helps create a loop to manage our game"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    
            self.screen.fill(self.bg_color)        
            pygame.display.flip()
         
            
if __name__ == "__main__":
    Game = Racing()
    Game.run_game()
        
        
