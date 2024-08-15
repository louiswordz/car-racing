import pygame

class Car:
    """A class that manages the car images"""
    def __init__(self, car_game):
        self.screen = car_game
        
        self.car_img = pygame.image.load("Assets/image1.png") 
        self.resize= pygame.transform.scale(self.car_img, (150,150))
        
    def car_obj(self,x,y):
        self.screen.blit(self.resize, (x,y))
        