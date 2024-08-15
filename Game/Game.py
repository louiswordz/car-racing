# import gaming libraries
import pygame
import sys
from settings import Settings
from car import Car

class Racing:
    """A class that models the assets and properties of our game"""
    def __init__(self):
        """Initialize  game function"""
        pygame.init()
        self.Settings = Settings()
        
        # Set screen size
        self.screen = pygame.display.set_mode((self.Settings.screen_width,
                                               self.Settings.screen_height))
        pygame.display.set_caption("Car Racing")
        self.Car = Car(self.screen)
        
        self.bg_color = self.Settings.bg_color
        
    def run_game(self):
        """Helps create a loop to manage our game"""
        while True:
            self.check_event()
            self.update_screen()
            
    def check_event(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                    
           
        pygame.display.flip()
         
        
        
    def update_screen(self):
        x = 120
        y = 300
        self.screen.fill(self.bg_color)
        self.Car.car_obj(x,y)   
        
            
        pygame.display.update()
if __name__ == "__main__":
    Game = Racing()
    Game.run_game()
        
        
