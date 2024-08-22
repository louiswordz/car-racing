import pygame

class Sound:
    def __init__(self):
        pygame.mixer.init()
        
        self.crash_sound = pygame.mixer.Sound('Assets\Slack-wow.mp3')
        self.game_sound = pygame.mixer.Sound('Assets/Slack - Tada.mp3')
        self.Car_sound = pygame.mixer.Sound('Assets\Slack - Knock brush.mp3')
        
