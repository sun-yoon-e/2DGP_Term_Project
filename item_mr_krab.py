from pico2d import *
import random


class Mr_krab:
    image = None

    def __init__(self):
        self.x, self.y = 3000, 30

        if Mr_krab.image is None:
            Mr_krab.image = load_image('resource/@Using/item_mr.krab.png')

    def update(self):
        if self.x <= 0:
            self.x = 3000
        self.x -= 10

    def draw(self):
        self.image.clip_draw(0, 0, 50, 50, self.x, self.y)
