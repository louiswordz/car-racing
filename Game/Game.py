# import gaming libraries
import pygame
import sys
import time
from settings import Settings
from car import Car
from sound import Sound
from random import randrange


class Racing:
    """A class that models the assets and properties of our game"""
    def __init__(self):
        """Initialize  game function"""
        pygame.init()
        self.Settings = Settings()
        self.Sound = Sound()
        
        # Set screen size
        self.screen = pygame.display.set_mode((self.Settings.screen_width,
                                               self.Settings.screen_height))
        pygame.display.set_caption("Car Racing")
        self.Car = Car(self.screen)
        
        self.font = pygame.font.SysFont("None", 80)
        self.render_text = self.font.render("sorry but Car Crashed!,game over", 0, (255,0,0))
        
        
        
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
                    self.Car.rect.x +=20
            
                
                if event.key == pygame.K_LEFT:
                    #Move the car to the left
                    self.Car.rect.x -= 20
                    
                if event.key == pygame.K_UP:
                    # Move the car Up ward
                    self.Car.rect.y -=20
                    
                if event.key == pygame.K_DOWN:
                    # Move the car Down ward
                    self.Car.rect.y +=20
                    
                if event.key == pygame.K_LCTRL:
                    # Move the car Upward
                    self.Car.rect.y +=20
                self.Sound.game_sound.play()
                
            
                    
                    
            
                
  
        pygame.display.flip()
           
    def update_screen(self):
        self.screen.fill(self.bg_color)
    
        # Draw the car and the road strips
        self.Car.Car_theme()
        self.Car.Yellow_Strip()

        # Check if the car has crashed by going off-road
        if self.Car.rect.y > 275 or self.Car.rect.y < 85:
            self.screen.blit(self.render_text, (10, 100))
            self.Sound.crash_sound.play()
            pygame.display.update()
            time.sleep(1)
            self.Car.rect.y = 170
            self.bumped = True  # End the game loop

        # Update obstacle position
        self.Settings.obs_x -= self.Settings.obstacle_speed
    
        # Draw the obstacle
        self.Car.Obstacle(self.Settings.obs_x, self.Settings.obs_y, self.Settings.obs)
    
        # Reset the obstacle if it goes off-screen
        if self.Settings.obs_x < 0 - self.Settings.enemy_width:
            self.Settings.obs_x = self.Settings.screen_width
            self.Settings.obs_y = randrange(80, 300)
            self.Settings.obs = randrange(1, 7)
            
        # Collision detection: Check if the car hits the obstacle
        print(f"Car position: {self.Car.rect.x}, {self.Car.rect.y}, width: {self.Car.rect.width}, height: {self.Car.rect.height}")
        print(f"Obstacle position: {self.Settings.obs_x}, {self.Settings.obs_y}, width: {self.Settings.enemy_width}, height: {self.Settings.enemy_height}")


        # Collision detection: Check if the car hits the obstacle
        if (self.Car.rect.x < self.Settings.obs_x + self.Settings.enemy_width and
            self.Car.rect.x + self.Car.rect.width > self.Settings.obs_x and
            self.Car.rect.y < self.Settings.obs_y + self.Settings.enemy_height and
            self.Car.rect.y + self.Car.rect.height > self.Settings.obs_y):
        
            # Collision detected: Display crash message and reset car position
            self.screen.blit(self.render_text, (60, 80))
            self.Sound.crash_sound.play()
            pygame.display.update()
            time.sleep(3)
            self.Car.rect.y = 170
            self.Settings.obs_x = self.Settings.screen_width  # Reset obstacle position
        
        # Draw the car object
        self.Car.car_obj()

             
        
        self.Sound.Car_sound.play()            
        pygame.display.update()
if __name__ == "__main__":
    Game = Racing()
    Game.run_game()
        
        
