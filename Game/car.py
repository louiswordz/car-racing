import pygame
from settings import Settings

class Car:
    """A class that manages the car images"""
    def __init__(self, car_game):
        
        
        self.screen = car_game
        self.screen_rect = car_game.get_rect()
        self.Settings = Settings()

        #Load first car
        self.car_img = pygame.image.load("Assets/Car/car1.jpg")
        self.resize = pygame.transform.scale(self.car_img, (30,60))
        self.rotate = pygame.transform.rotate(self.resize, (270))
        self.rect = self.rotate.get_rect()
        
        
        # Load Grass
        self.grass = pygame.image.load('Assets/grass.jpg')
        self.resize_g = pygame.transform.scale(self.grass, (1400, 70))                                                              
        self.rect_grass1 = self.resize_g.get_rect()
        
        # Load Grass
        self.grass2 = pygame.image.load("Assets/grass.jpg")
        self.resize_g2 = pygame.transform.scale(self.grass, (1400, 70))
        self.rect_grass2 = self.resize_g2.get_rect()
        
        #Load Ustrip
        self.Lstrip = pygame.image.load("Assets/strip.jpg")
        self.L_resize = pygame.transform.scale(self.Lstrip, (1500, 3))
        self.L_rect = self.L_resize.get_rect()
        
        #Load Nstrip
        self.Dstrip = pygame.image.load("Assets/strip.jpg")
        self.D_resize = pygame.transform.scale(self.Dstrip, (1500,3 ))
        self.s_rect = self.D_resize.get_rect()
        
        # Backround image 1
        self.background2 = pygame.image.load("Assets/background.jpg")
        self.B_size = pygame.transform.scale(self.background2, (500,0))
        self.b_rect1 = self.B_size.get_rect()
        
    
    
        
        #Load yellow_strip
        self.yellow_strip = pygame.image.load("Assets/yellow_strip.jpg")
        self.resize_y = pygame.transform.scale(self.yellow_strip, (100, 8))
        self.yellow_rect = self.resize_y.get_rect()
        
       
        
        # time module
        self.clock = pygame.time.Clock()
        
        
        # Start each new ship at the bottom center of the screen.
        self.rect.midleft =  self.screen_rect.midleft
       
        
        self.moving_right = True
        
    def update_self(self):
        """Updating the Cars position based on the movement flag!"""
        if self.moving_right:
            self.rect.x +=10
        
    def car_obj(self):
        self.screen.blit(self.rotate, self.rect)
        
        
        
    
    # Grass Object1   
    def Car_theme(self):
        self.screen.blit(self.resize_g, (0,0))
        self.screen.blit(self.resize_g2, (0,335))
        self.screen.blit(self.B_size, self.b_rect1)
        self.screen.blit(self.L_resize, (0,75))
        self.screen.blit(self.D_resize, (0, 327))
   
        
    
    #Yellow Strip     
    def Yellow_Strip(self):
        for i in range(1, 2000, 130):
            self.screen.blit(self.resize_y, (i,150))
            self.screen.blit(self.resize_y, (i,230))

            
    def Obstacle(self, x_cord, y_cord, z_cord):
        # Load the image based on the z_cord (random car type)
        obs_pic = pygame.image.load(f'Assets/Car/car{z_cord}.jpg')
    
        # Resize the car image
        obs_size = pygame.transform.scale(obs_pic, (30, 60))
    
        # Rotate the car image by 90 degrees
        obs_rotate = pygame.transform.rotate(obs_size, 90)
    
        # Draw the car on the screen at the specified coordinates
        self.screen.blit(obs_rotate, (x_cord, y_cord))

    
    
            
        
                
    
           
            

       
        