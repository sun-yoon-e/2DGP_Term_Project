from pico2d import *
import random

name = "balloon"


class Balloon:
    image = None

    def __init__(self):
        self.x, self.y = random.randint(3000, 6000), 40
        self.frame = random.randint(0, 3)

        if Balloon.image is None:
            Balloon.image = load_image('resource/@Using/item_balloon.png')

    def update(self):
        if self.x <= 0:
            self.x = random.randint(3000, 6000)
            self.frame = random.randint(0, 3)
        self.x -= 10

    def draw(self):
        self.image.clip_draw(self.frame * 55, 0, 55, 40, self.x, self.y)

