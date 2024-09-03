import pygame


class Intro:
    def __init__(self):
        # Intro Background
        self.Intro_bg = pygame.image.load('Assets/background.jpg')
        self.Intro_bg_scale = pygame.transform.scale(self.Intro_bg, (1000,400))
        
        #Intro Text
        self.ifont = pygame.font.SysFont("Arial", 140)
        self.title = self.ifont.render('Car Game',True,(0,0,0))
        
        # Intro button color
        self.green = (0,255,0)
        self.blue = (0,0,255)
        self.red = (255,0,0)
        self.light_green = (0,125,0)
        
        # Mouse  event
        self.mouse = pygame.mouse.get_pos()
        
        self.Intro = True
        
    