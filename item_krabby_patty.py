from pico2d import *
import random

name = "balloon"


class Krabby_Patty:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(2000, 4000), 40

        if Krabby_Patty.image is None:
            Krabby_Patty.image = load_image('resource/@Using/krabby_patty.png')

    def update(self):
        if self.x <= 0:
            self.x = random.randint(2000, 4000)
        self.x -= 10

    def draw(self):
        self.image.clip_draw(0, 0, 55, 50, self.x, self.y, 60, 60)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20
