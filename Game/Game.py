# import gaming libraries
import pygame
import sys
import time
from settings import Settings
from car import Car
from sound import Sound


class Racing:
    """A class that models the assets and properties of our game"""
    def __init__(self):
        """Initialize  game function"""
        pygame.init()
        pygame.mixer.init()
        self.Settings = Settings()
        self.Sound = Sound()
        
        # Set screen size
        self.screen = pygame.display.set_mode((self.Settings.screen_width,
                                               self.Settings.screen_height))
        pygame.display.set_caption("Car Racing")
        self.Car = Car(self.screen)
        
        self.font = pygame.font.SysFont("None", 100)
        self.render_text = self.font.render("Car Crashed!", 1, (255,0,0))
        
        
        
        self.bg_color = self.Settings.bg_color
        self.bumped = False
    
       
    def run_game(self):
        """This function helps create a loop to manage our game"""
        while not self.bumped:
            self.check_event()
            self.update_screen()
            
    def check_event(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #Move the car to the right
                    self.Car.rect.x +=2
            
                
                if event.key == pygame.K_LEFT:
                    #Move the car to the left
                    self.Car.rect.x -= 2
                    
                if event.key == pygame.K_UP:
                    # Move the car Up ward
                    self.Car.rect.y -=5
                    
                if event.key == pygame.K_DOWN:
                    # Move the car Down ward
                    self.Car.rect.y +=5
                    
                if event.key == pygame.K_LCTRL:
                    # Move the car Upward
                    self.Car.rect.y +=2
                self.Sound.game_sound.play()
            
                    
                    
            
                
  
        pygame.display.flip()
           
    def update_screen(self):
        self.screen.fill(self.bg_color)
        self.Car.clock.tick(1000)
        self.Car.Yellow_Strip()
        self.Car.Car_theme()
        self.Car.Yellow_Strip()
        self.Car.car_obj()
        
        if self.Car.rect.y > 275 or self.Car.rect.y < 85:
            self.screen.blit(self.render_text, (80,100))
            self.Sound.crash_sound.play()
            pygame.display.update()
            time.sleep(1)
            self.bumped != True
            
        self.Settings.obs_x -= (self.Settings.obstacle_speed/4)
        self.Car.Obstacle(self.Settings.obs_x, self.Settings.obs_y, self.Settings.obs)
        self.Settings.obs_y += self.Settings.obstacle_speed
            
        
             
            
        self.Sound.Car_sound.play()            
        pygame.display.update()
if __name__ == "__main__":
    Game = Racing()
    Game.run_game()
        
        
