import game_framework
from pico2d import *

re_loading = None


class Re_loading:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


def enter():
    global re_loading
    re_loading = Re_loading()


def exit():
    global re_loading
    del re_loading


def update():
    global re_loading
    re_loading.update()


def draw():
    global re_loading
    clear_canvas()
    re_loading.update()
    re_loading.draw()
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
