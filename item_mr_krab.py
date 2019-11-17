from pico2d import *
import random

name = "krab"


class Mr_krab:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(1500, 3000), 40

        if Mr_krab.image is None:
            Mr_krab.image = load_image('resource/@Using/item_mr.krab.png')

    def update(self):
        if self.x <= 0:
            self.x = random.randint(1500, 3000)
        self.x -= 10

    def draw(self):
        self.image.clip_draw(0, 0, 50, 50, self.x, self.y, 60, 60)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x +20, self.y + 20
