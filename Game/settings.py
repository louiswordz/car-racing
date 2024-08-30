from random import randrange

class Settings:
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 400
        self.bg_color = (200, 200, 200)
        self.obstacle_speed = 2
        self.obs = randrange(1, 7)  # Random car type for obstacle       
        self.obs_y = randrange(100, 300,10)  # Adjusted obstacle y-range
        self.obs_x = self.screen_width  # Start the obstacle off-screen
        self.enemy_width = 50
        self.enemy_height = 40
        self.car_passed = 0
        self.score = 0
        self.level = 0
        