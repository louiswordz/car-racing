# import gaming libraries
import pygame
import sys
import time
from settings import Settings
from car import Car
from sound import Sound
from random import randrange
from scroll import Scroll
from intro import Intro



class Racing:
    """A class that models the assets and properties of our game"""
    def __init__(self):
        """Initialize  game function"""
        pygame.init()
        self.Settings = Settings()
        self.Sound = Sound()
        self.Scroll = Scroll()
        self.Intro = Intro()
        
        # Set screen size
        self.screen = pygame.display.set_mode((self.Settings.screen_width,
                                               self.Settings.screen_height))
        #self.Settings.screen_width = self.screen.get_rect().width
        #self.Settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Car Racing")
        self.Car = Car(self.screen)
        self.enemy = pygame.sprite.Group()
        
        self.font = pygame.font.SysFont("Arial", 60)
        self.render_text = self.font.render("Car Crashed!", 0, (255,0,0))
        
        
        
        self.bg_color = self.Settings.bg_color
        self.bumped = False
        self.car_crashed = True
        
    # Intro Image
        
    def Intro_loop(self):
        while self.Intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    

            self.screen.blit(self.Intro.Intro_bg_scale, (0,0))
            self.screen.blit(self.Intro.title, (200,50))
            
            pygame.draw.rect(self.screen,self.Intro.green,(140,300,120,40))
            pygame.draw.rect(self.screen,self.Intro.blue,(370,300,120,40))
            pygame.draw.rect(self.screen,self.Intro.red,(570,300,120,40))
            
            if self.Intro.mouse[0] > 40 and self.Intro.mouse[0] < 180:
                pygame.draw.rect(self.screen, self.Intro.light_green,(80,500,150,50))
            else:
                pygame.draw.rect(self.screen, self.Intro.green, (80,500,150,50))
            pygame.display.update()
        
        
    
       
    def run_game(self):
        """This function helps create a loop to manage our game"""
        while not self.bumped:
            self.Intro_loop()
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
                    self.Car.rect.y +=8
                    
                if event.key == pygame.K_s:
                    self.Settings.obstacle_speed +=2
                if event.key == pygame.K_b:
                    self.Settings.obstacle_speed -= 2
                self.Sound.game_sound.play()
                           
  
        pygame.display.flip()
        
    def update_screen(self):
        #self.screen.fill(self.bg_color)
        # Draw Background
        self.Car.update_self()
        self.Car.Scroll_bg()  # Scroll the background
        self.Car.Car_theme()  # Draw the background elements
        self.Car.Yellow_Strip()  # Draw the yellow strips
        self.enemy.update()
        self.Car.score_card(self.Settings.car_passed, self.Settings.score)
        
        # Check if the car has crashed by going off-road
        if self.Car.rect.y > 300 or self.Car.rect.y < 75:
            self.screen.blit(self.render_text, (60, 80))
            self.Sound.crash_sound.play()
            pygame.display.update()
            time.sleep(1)
            self.Car.rect.y = 170
            self.bumped != True  # End the game loop

        # Update obstacle position
        self.Settings.obs_x -= self.Settings.obstacle_speed
    
        # Draw the obstacle
        self.Car.Obstacle(self.Settings.obs_x, self.Settings.obs_y, self.Settings.obs)
    
        # Reset the obstacle if it goes off-screen
        if self.Settings.obs_x < 0 - self.Settings.enemy_width:
            self.Settings.obs_x = self.Settings.screen_width
            self.Settings.obs_y = randrange(80, 300)
            self.Settings.obs = randrange(1, 7)
            self.Settings.car_passed += 1
            
            
            if int(self.Settings.car_passed % 10 == 0):
                self.Settings.level += 1
                self.Settings.score = self.Settings.car_passed 
                self.Settings.obstacle_speed +=2
                myFont = pygame.font.SysFont('Arial', 60)
                level_text = myFont.render(f"level {self.Settings.level}", 1,(0,0,0) )
                self.screen.blit(level_text, (100,200))
                pygame.display.update()
                time.sleep(3)
                
            #if self.car_crashed:
            #    lst = []
            #    lst.append(self.render_text)
            #    if len(lst) == 3:
            #        self.Settings.level = 0
            #        self.Settings.car_passed = 0
                
         
                # Collision detection: Check if the car hits the obstacle on either axis
        if (
        (self.Car.rect.x < self.Settings.obs_x + self.Settings.enemy_width and  # Car's right side crosses obstacle's left
        self.Car.rect.x + self.Car.rect.width > self.Settings.obs_x) and  # Car's left side crosses obstacle's right
        (self.Car.rect.y < self.Settings.obs_y + self.Settings.enemy_height and  # Car's bottom crosses obstacle's top
         self.Car.rect.y + self.Car.rect.height > self.Settings.obs_y)  # Car's top crosses obstacle's bottom
            ):
            # Collision detected: Display crash message and reset car position
            self.screen.blit(self.render_text, (60, 80))
            self.Sound.crash_sound.play()
            pygame.display.update()
            time.sleep(3)
            self.Car.rect.y = 170
            self.Settings.obs_x = self.Settings.screen_width  # Reset obstacle position
            self.bumped != True  # Mark the game as not bumped
        
        # Draw the car object
        self.Car.car_obj()
        
          
        self.Sound.Car_sound.play()            
        pygame.display.update()
if __name__ == "__main__":
    Game = Racing()
    Game.run_game()
        
        
