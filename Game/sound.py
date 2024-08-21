import pygame

class Sound:
    def __init__(self):
        pygame.mixer.init()
        
        self.crash_sound = pygame.mixer.Sound('Assets\Slack-Drop.mp3')
        self.game_sound = pygame.mixer.Sound('Assets/Slack-Whoa.mp3')
        self.Car_sound = pygame.mixer.Sound('Assets/Slack-Wow.mp3')
        
