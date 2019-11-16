from pico2d import *
import random

name = "hand"


class Hand:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(1000, 2000), 200
        if Hand.image is None:
            Hand.image = load_image('resource/@Using/obstacle_hand.png')

    def update(self):
        if self.x <= 0:
            self.x = random.randint(1000, 2000)
        self.x -= 10

    def draw(self):
        self.image.clip_draw(0, 0, 70, 180, self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 90, self.x, self.y + 90
    