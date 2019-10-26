from pico2d import *

character = None
background = None


class Character:
    def __init__(self):
        self.x, self.y = 100, 70
        self.frame = 0
        self.image = load_image('character.png')

    def update(self):
        self.frame = (self.frame + 1) % 6

    def draw(self):
        self.image.clip_draw(self.frame * 83, 110, 83, 90, self.x, self.y)


class Background:
    def __init__(self):
        self.x1, self.x2, self.x3, self.x4 = 1441, 2882, 2882, 2882
        self.image1 = load_image('map1.png')
        self.image2 = load_image('map2.png')
        self.image3 = load_image('map3.png')
        self.image4 = load_image('map4.png')

    def update(self):
        if self.x1 >= -1441:
            self.x1 -= 5
        if self.x1 <= 0 and self.x2 >= -1441:
            self.x2 -= 5
        if self.x2 <= 0 and self.x3 >= -1441:
            self.x3 -= 5
        if self.x3 <= 0 and self.x4 >= -1441:
            self.x4 -= 5

    def draw(self):
        if self.x1 >= -1441:
            self.image1.clip_draw(0, 0, 2882, 350, self.x1, 145)
            self.image1.clip_draw(0, 600, 2882, 365, self.x1, 120)
            self.image1.clip_draw(0, 305, 2882, 340, self.x1, 150)

        if self.x1 <= 0 and self.x2 >= -1441:
            self.image2.clip_draw(0, 300, 2882, 330, self.x2, 160)
            self.image2.clip_draw(0, 600, 2882, 400, self.x2, 120)
            self.x2 -= 5

        if self.x2 <= 0 and self.x3 >= -1441:
            self.image3.clip_draw(0, 300, 2882, 330, self.x3, 310)
            self.image3.clip_draw(0, 500, 2882, 325, self.x3, 160)
            self.x3 -= 5

        if self.x3 <= 0 and self.x4 >= -1441:
            self.image4.clip_draw(0, 0, 2882, 350, self.x4, 145)
            self.image4.clip_draw(0, 600, 2882, 340, self.x4, 100)
            self.image4.clip_draw(0, 305, 2882, 330, self.x4, 160)
            self.x4 -= 5


def enter():
    global character, background
    character = Character()
    background = Background()


def exit():
    global character, background
    del(character)
    del(background)


def pause():
    pass


def resume():
    pass


def handle_events():
    pass


def update():
    character.update()
    background.update()


def draw():
    clear_canvas()
    character.draw()
    background.draw()
    update_canvas()
    delay(0.03)
