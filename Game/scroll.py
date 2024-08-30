import pygame


class Scroll:
    def __init__(self):
        self.clock = pygame.time.Clock()
        
        self.bg = pygame.image.load('Assets/images12.jpeg')
        self.bg_scale = pygame.transform.scale(self.bg, (1400,400))
        
        self.bg_size = self.bg_scale.get_size()
    
        self.bg_rect = self.bg_scale.get_rect()
        
        self.w, self.h = self.bg_size
        
        self.x = 0
        self.y = 0
        
        self.x1 = 0
        self.y1  = -self.w