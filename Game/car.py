import pygame

class Car:
    """A class that manages the car images"""
    def __init__(self, car_game):
        self.screen = car_game
        self.screen_rect = car_game.get_rect()

        
        self.car_img = pygame.image.load("Assets/image4.png") 
        self.resize= pygame.transform.scale(self.car_img, (60,60))
        self.rect = self.resize.get_rect()
        
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom =  self.screen_rect.midbottom
        
        self.moving_right = False
        
    def update_self(self):
        """Updating the Cars position based on the movement flag!"""
        if self.moving_right:
            self.rect.x +=1
        
    def car_obj(self):
        self.screen.blit(self.resize, self.rect)
        