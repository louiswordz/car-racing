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
        self.green = (0,180,0)
        self.blue = (0,0,170)
        self.red = (200,0,0)
        self.light_green = (0,255,0)
        self.light_blue = (0,0,255)
        self.light_red = (255,0,0)
        
        
        self.Intro = True
        
        
    def text_object(self, text, font):
        textSurface = font.render(text, True, (0,0,0))
        return textSurface, textSurface.get_rect()
        
    
        
    