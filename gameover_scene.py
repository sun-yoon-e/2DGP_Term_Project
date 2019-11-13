import game_framework
from pico2d import *

over = None


class Over:
    def __init__(self):
        self.image_logo = load_image('resource/@Using/game over logo.png')
        self.image_character1 = load_image('resource/@Using/over.png')
        self.image_character2 = load_image('resource/@Using/over2.png')
        self.image_back = load_image('resource/@Using/over&success.png')

    def update(self):
        pass

    def draw(self):
        self.image_back.clip_draw(0, 0, 482, 140, 400, 145, 800, 290)


def enter():
    global over
    over = Over()


def exit():
    global over
    del over


def update():
    global over
    over.update()


def draw():
    global over
    clear_canvas()
    over.update()
    over.draw()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()



def pause():
    pass


def resume():
    pass
