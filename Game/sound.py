# Import libraries
import pygame

class Sound:
    '''
        A class that manages the sound of our game
    '''
    def __init__(self):
        pygame.mixer.init()
        
        # Using the pygame Mixer to load and set sound!
        self.crash_sound = pygame.mixer.Sound('Assets\Slack-wow.mp3')
        self.game_sound = pygame.mixer.Sound('Assets/Slack - Tada.mp3')
        self.Car_sound = pygame.mixer.Sound('Assets\Slack - Knock brush.mp3')
        
