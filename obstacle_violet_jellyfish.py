from pico2d import *
import random

name = "violet_jellyfish"


class Violet_Jellyfish:
    image = None

    def __init__(self):
        self.x, self.y = 1000, 30
        self.random_x = random.randint(0, 500)
        self.frame = 0
        if Violet_Jellyfish.image is None:
            Violet_Jellyfish.image = load_image('resource/@Using/obstacle_violet.png')

    def update(self):
        self.frame = (self.frame + 1) % 4
        if self.x + self.random_x <= 0:
            self.x = 1000
            self.random_x = random.randint(0, 500)
        self.x -= 10

    def draw(self):
        self.image.clip_draw(self.frame * 30, 0, 30, 35, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 10, self.y - 15, self.x, self.y + 15
