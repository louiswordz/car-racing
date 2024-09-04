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
            
            click = pygame.mouse.get_pressed()
            
            
            mouse = pygame.mouse.get_pos()
            pygame.draw.rect(self.screen,self.Intro.green,(240,330,150,40))
            pygame.draw.rect(self.screen,self.Intro.blue,(440,330,150,40))
            pygame.draw.rect(self.screen,self.Intro.red,(640,330,150,40))
            
            
            if mouse[0] > 240 and mouse[0] < 390 and mouse[1] >330 and mouse[1] <370:
                pygame.draw.rect(self.screen, self.Intro.light_green,(240,330,150,40))
                if click == (True,False,False):
                    self.run_game()
            else:
                pygame.draw.rect(self.screen, self.Intro.green, (240,330,150,40))
            
            
            # Call the text_obj function on start button 
            small_text = pygame.font.Font('freesansbold.ttf',20)
            textSurface, textRect = self.Intro.text_object("START", small_text)
            textRect.center = ((240+(150/2))),((330+(40/2)))
            self.screen.blit(textSurface, textRect)
            
                
            if mouse[0] > 440 and mouse[0] < 590 and mouse[1] >330 and mouse[1] <370:
                pygame.draw.rect(self.screen, self.Intro.light_blue,(440,330,150,40))
                if click == (True,False,False):
                    self.Instruction()
                
                
            else:
                pygame.draw.rect(self.screen, self.Intro.blue, (440,330,150,40))
                
            # Call the text_obj function on description button 
            small_text = pygame.font.Font('freesansbold.ttf',20)
            textSurface, textRect = self.Intro.text_object("INSTRUCTION", small_text)
            textRect.center = ((440+(150/2))),((330+(40/2)))
            self.screen.blit(textSurface, textRect)
            
                
            if mouse[0] > 640 and mouse[0] < 790 and mouse[1] >330 and mouse[1] <370:
                pygame.draw.rect(self.screen, self.Intro.light_red,(640,330,150,40))
                if click == (True,False,False):
                    pygame.quit()
                    sys.exit()
                    
            else:
                pygame.draw.rect(self.screen, self.Intro.red, (640,330,150,40))
                
            # Call the text_obj function on END button 
            small_text = pygame.font.Font('freesansbold.ttf',20)
            textSurface, textRect = self.Intro.text_object("END", small_text)
            textRect.center = ((640+(150/2))),((330+(40/2)))
            self.screen.blit(textSurface, textRect)
            

            pygame.display.update()
            
    def Paused(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()            
                    
            ## Load Image
            bg = pygame.image.load('Assets/background2.jpg')
            bg_resize = pygame.transform.scale(bg, (1000, 400))
            self.screen.blit(bg_resize, (0,0))
            
            text = pygame.font.Font('freesansbold.ttf', 100)
            textSurface, textRect = self.Intro.text_object("PAUSED", text)
            textRect.center = (500,120)
            self.screen.blit(textSurface, textRect)
            
            
            # Draw buttons
            pygame.draw.rect(self.screen,self.Intro.green,(240,330,150,40))
            pygame.draw.rect(self.screen,self.Intro.blue,(440,330,150,40))
            pygame.draw.rect(self.screen,self.Intro.red,(640,330,150,40))
            
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if mouse[0] > 240 and mouse[0] < 390 and mouse[1] >330 and mouse[1] <370:
                pygame.draw.rect(self.screen, self.Intro.light_green,(240,330,150,40))
                if click == (True,False,False):
                    self.Intro_loop()
            else:
                pygame.draw.rect(self.screen, self.Intro.green, (240,330,150,40))
            
            
            # Call the text_obj function on start button 
            small_text = pygame.font.Font('freesansbold.ttf',20)
            textSurface, textRect = self.Intro.text_object("Continue", small_text)
            textRect.center = ((240+(150/2))),((330+(40/2)))
            self.screen.blit(textSurface, textRect)
            
                
            if mouse[0] > 440 and mouse[0] < 590 and mouse[1] >330 and mouse[1] <370:
                pygame.draw.rect(self.screen, self.Intro.light_blue,(440,330,150,40))
                if click == (True,False,False):
                    self.run_game()
                
                
            else:
                pygame.draw.rect(self.screen, self.Intro.blue, (440,330,150,40))
                
            # Call the text_obj function on description button 
            small_text = pygame.font.Font('freesansbold.ttf',20)
            textSurface, textRect = self.Intro.text_object("Restart", small_text)
            textRect.center = ((440+(150/2))),((330+(40/2)))
            self.screen.blit(textSurface, textRect)
            
                
            if mouse[0] > 640 and mouse[0] < 790 and mouse[1] >330 and mouse[1] <370:
                pygame.draw.rect(self.screen, self.Intro.light_red,(640,330,150,40))
                if click == (True,False,False):
                    self.Instruction()
            else:
                pygame.draw.rect(self.screen, self.Intro.red, (640,330,150,40))
                
            # Call the text_obj function on END button 
            small_text = pygame.font.Font('freesansbold.ttf',20)
            textSurface, textRect = self.Intro.text_object("MAIN MENU", small_text)
            textRect.center = ((640+(150/2))),((330+(40/2)))
            self.screen.blit(textSurface, textRect)
            
            
            
            
            pygame.display.update()
        
        
    
       
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
        pygame.draw.rect(self.screen, (122,200,122),(700,20,150,40))
        text = pygame.font.Font('freesansbold.ttf',20)
        textSurface, textRect = self.Intro.text_object("Pause", text)
        textRect.center = ((700+(150/2))),((20+(40/2)))
        self.screen.blit(textSurface, textRect)
        

        
        click = pygame.mouse.get_pressed()
        mouse = pygame.mouse.get_pos()
        
        if mouse[0] > 700 and mouse[0] < 850 and mouse[1] > 20 and mouse[1] < 60:
            pygame.draw.rect(self.screen, (100,150,100),(700,20,150,40))
            text = pygame.font.Font('freesansbold.ttf',20)
            textSurface, textRect = self.Intro.text_object("Pause", text)
            textRect.center = ((700+(150/2))),((20+(40/2)))
            self.screen.blit(textSurface, textRect)
            
            if click == (True,False,False):
                self.Paused()
        else:
           pygame.draw.rect(self.screen, (122,200,122),(700,20,150,40))
           text = pygame.font.Font('freesansbold.ttf',20)
           textSurface, textRect = self.Intro.text_object("Pause", text)
           textRect.center = ((700+(150/2))),((20+(40/2)))
           self.screen.blit(textSurface, textRect)
         
        
        
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
        
    def Instruction(self):
        Instruction = True
        while Instruction:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            self.screen.blit( self.Car.Iresize, (0,0))
            
            largeText = pygame.font.Font('freesansbold.ttf', 80)
            mediumText = pygame.font.Font('freesansbold.ttf',30)
            smallText = pygame.font.Font('freesansbold.ttf', 20)
            
            textSurface, textRect = self.Intro.text_object("Ancient Game", mediumText)
            textRect.center = (500,100)
            self.screen.blit(textSurface, textRect)
            
            
            textSurface, textRect = self.Intro.text_object("Instructions", largeText)
            textRect.center = (500,50)
            self.screen.blit(textSurface, textRect)
            
            textSurface, textRect = self.Intro.text_object("Controls", mediumText)
            textRect.center = (500,160)
            self.screen.blit(textSurface, textRect)
            
            textSurface, textRect = self.Intro.text_object("p:-> Pause", smallText)
            textRect.center = (500,200)
            self.screen.blit(textSurface, textRect)
            
            textSurface, textRect = self.Intro.text_object("ArrowUp:-> Move Left", smallText)
            textRect.center = (500,240)
            self.screen.blit(textSurface, textRect)
            
            textSurface, textRect = self.Intro.text_object("ArrowDown:->  Move Right", smallText)
            textRect.center = (500,280)
            self.screen.blit(textSurface, textRect)
            
            textSurface, textRect = self.Intro.text_object("b:->  Accelerator", smallText)
            textRect.center = (500,320)
            self.screen.blit(textSurface, textRect)
            
            textSurface, textRect = self.Intro.text_object("k:->   Decelerator", smallText)
            textRect.center = (500,360)
            self.screen.blit(textSurface, textRect)
            
            pygame.draw.rect(self.screen,self.Intro.blue,(800, 200,150,50))
            textSurface, textRect = self.Intro.text_object("BACK", smallText)
            textRect.center = (800+(150/2)),(200+(50/2))
            self.screen.blit(textSurface, textRect)
            
            
            click = pygame.mouse.get_pressed()
            mouse = pygame.mouse.get_pos()
            if mouse[0] > 800 and mouse[0] < 950 and mouse[1] >200 and mouse[1] < 250:
                 pygame.draw.rect(self.screen,self.Intro.light_blue,(800, 200,150,50))
                 textSurface, textRect = self.Intro.text_object("BACK", smallText)
                 textRect.center = (800+(150/2)),(200+(50/2))
                 self.screen.blit(textSurface, textRect)
                 
                 if click == (True,False,False):
                     self.Intro_loop()
            else:
                 pygame.draw.rect(self.screen,self.Intro.blue,(800, 200,150,50))
                 textSurface, textRect = self.Intro.text_object("BACK", smallText)
                 textRect.center = (800+(150/2)),(200+(50/2))
                 self.screen.blit(textSurface, textRect)
                  
                 
                
                
            
          
            
            pygame.display.update()
        
          
        self.Sound.Car_sound.play()            
        pygame.display.update()
if __name__ == "__main__":
    Game = Racing()
    Game.Intro_loop()
        
        
