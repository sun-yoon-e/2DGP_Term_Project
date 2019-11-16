from pico2d import *
import random

name = "bubble"


class Bubble:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(2000, 6000), 100

        if Bubble.image is None:
            Bubble.image = load_image('resource/@Using/item_bubble.png')

    def update(self):
        if self.x <= 0:
            self.x = random.randint(2000, 6000)
        self.x -= 10

    def draw(self):
        self.image.clip_draw(0, 0, 65, 45, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 20, self.x, self.y + 20