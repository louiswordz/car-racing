import pygame

class Car:
    """A class that manages the car images"""
    def __init__(self, car_game):
        self.screen = car_game
        self.screen_rect = car_game.get_rect()

        #Load first car
        self.car_img = pygame.image.load("Assets/image4.png") 
        self.resize= pygame.transform.scale(self.car_img, (100,100))
        self.rect = self.resize.get_rect()
        
        #Load Second car
        self.car_img2 = pygame.image.load("Assets/image3.png") 
        self.resize2= pygame.transform.scale(self.car_img2, (100,100))
        self.rect_2 = self.resize2.get_rect()
        
        # Load Grass
        self.grass = pygame.image.load('Assets/1723993511899.jpg')
        self.rect_grass1 = self.grass.get_rect()
        
        # Load Grass
        self.grass2 = pygame.image.load("Assets/1723993511899.jpg")
        self.rect_grass2 = self.grass2.get_rect()
        
        # Backround image 1
        self.background = pygame.image.load("Assets/background.jpg")
        self.b_rect1 = self.background.get_rect()
        
        #Background image 2
        self.background2 = pygame.image.load("Assets/background2.jpg")
        
        #Load yellow_strip
        self.yellow_strip = pygame.image.load("Assets/yellow_strip.jpg")
        self.yellow_rect = self.yellow_strip.get_rect()
        
        #Load white line
        self.strip = pygame.image.load("Assets/strip.jpg")
        
        
        # time module
        self.clock = pygame.time.Clock()
        
        
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom =  self.screen_rect.midbottom
        self.rect_2.bottomleft = self.screen_rect.bottomleft
        
        self.moving_right = False
        
    def update_self(self):
        """Updating the Cars position based on the movement flag!"""
        if self.moving_right:
            self.rect.x +=1
        
    def car_obj(self):
        self.screen.blit(self.resize, self.rect)
        self.screen.blit(self.resize2, self.rect_2)
    
    # Grass Object1   
    def LGrass(self):
        self.screen.blit(self.grass, (0,0))
    
    #Grass Object2    
    def RGrass(self):
        self.screen.blit(self.grass2, (600,0))
        
    # background image
    def Background(self):
        self.screen.blit(self.background2, (0,0))
    
    #Yellow Strip     
    def Yellow_Strip(self):
        for i in range(1, 700, 30):
            self.screen.blit(self.yellow_strip, (330,i))
        