from pico2d import *

class Patrick:
    def __init__(self):
        self.x, self.y = 100, 50
        self.frame = 0
        self.image = load_image('resource/@Using/patrick.png')

    def update(self):
        self.frame = (self.frame + 1) % 6

    def draw(self):
        self.image.clip_draw(self.frame * 78, 0, 78, 93, self.x, self.y)
