from pico2d import *
name = "background"


class Background:
    def __init__(self):
        self.x1, self.x2, self.x3, self.x4 = 1441, 2882, 2882, 2882
        self.image1 = load_image('resource/@Using/map1.png')
        self.image2 = load_image('resource/@Using/map2.png')
        self.image3 = load_image('resource/@Using/map3.png')
        self.image4 = load_image('resource/@Using/map4.png')

    def update(self):
        if self.x1 >= -1441:
            self.x1 -= 5
        if self.x1 <= 0 and self.x2 >= -1441:
            self.x2 -= 5
        if self.x2 <= 0 and self.x3 >= -1441:
            self.x3 -= 5
        if self.x3 <= 0:# and self.x4 >= -1441:
            self.x4 -= 5
        if self.x4 <= -641:
            self.x4 = -641

    def draw(self):
        if self.x1 >= -1441:
            self.image1.clip_draw(0, 0, 2882, 350, self.x1, 145)
            self.image1.clip_draw(0, 600, 2882, 365, self.x1, 120)
            self.image1.clip_draw(0, 305, 2882, 340, self.x1, 150)

        if self.x1 <= 0 and self.x2 >= -1441:
            self.image2.clip_draw(0, 300, 2882, 330, self.x2, 160)
            self.image2.clip_draw(0, 600, 2882, 400, self.x2, 120)

        if self.x2 <= 0 and self.x3 >= -1441:
            self.image3.clip_draw(0, 300, 2882, 330, self.x3, 310)
            self.image3.clip_draw(0, 500, 2882, 325, self.x3, 160)

        if self.x3 <= 0 and self.x4 >= -1441:
            self.image4.clip_draw(0, 0, 2882, 350, self.x4, 155)
            self.image4.clip_draw(0, 600, 2882, 340, self.x4, 100)
            self.image4.clip_draw(0, 305, 2882, 330, self.x4, 160)
