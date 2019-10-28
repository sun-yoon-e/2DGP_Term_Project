from pico2d import *
import random

class Jellyfish:
    def __init__(self):
        self.x, self.y = 900, 30
        self.random_x = random.randint(200, 500)
        self.frame = 0
        self.pink = load_image('resource/@Using/obstacle_pink.png')
        self.violet = load_image('resource/@Using/obstacle_violet.png')

    def update(self):
        self.frame = (self.frame + 1) % 4
        if (self.x + self.random_x + 300 <= -0):
            self.x = 900
            self.random_x = random.randint(200, 500)
        self.x -= 10

    def draw(self):
        self.pink.clip_draw(self.frame * 30, 0, 30, 35, self.x, self.y)
        self.violet.clip_draw(self.frame * 30, 0, 30, 35, self.x + self.random_x, self.y)
        if (self.x <= 300):
            self.violet.clip_draw(self.frame * 30, 0, 30, 35, self.x + 300, self.y)
            self.pink.clip_draw(self.frame * 30, 0, 30, 35, self.x + self.random_x + 300, self.y)
