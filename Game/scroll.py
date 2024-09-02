# Import Pygame
import pygame

# Write a Class that manages scrolling the background!!
class Scroll:
    def __init__(self):
        # Set timer
        self.clock = pygame.time.Clock()
        
        # Upload image that serves as background image     
        self.bg = pygame.image.load('Assets/images12.jpeg')
        self.bg_scale = pygame.transform.scale(self.bg, (1400,400)) # Rescale the image size
        
        self.bg_size = self.bg_scale.get_size() # Get the size size of the background and assign it to a variable
    
        self.bg_rect = self.bg_scale.get_rect() # Get the rect of the background!
        
        self.w, self.h = self.bg_size # destructure the background size
        
        self.x = 0
        self.y = 0
        
        self.x1 = 0
        self.y1  = -self.w
        