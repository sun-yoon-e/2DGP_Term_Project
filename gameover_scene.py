import game_framework
from pico2d import *

over = None


class Over:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


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
        pass



def pause():
    pass


def resume():
    pass
