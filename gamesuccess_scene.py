import game_framework
from pico2d import *

success = None


class Success:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


def enter():
    global success
    success = Success()


def exit():
    global success
    del success


def update():
    global success
    success.update()


def draw():
    global success
    clear_canvas()
    success.update()
    success.draw()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        pass



def pause():
    pass


def resume():
    pass
