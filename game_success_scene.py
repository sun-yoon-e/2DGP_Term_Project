import game_framework
import re_loading_scene
from pico2d import *

success = None
time = 0.0


class Success:
    def __init__(self):
        self.image_logo1 = load_image('resource/@Using/start button.png')
        self.image_logo2 = load_image('resource/@Using/complete.png')
        self.image_character = load_image('resource/@Using/success.png')
        self.image_back = load_image('resource/@Using/over&success.png')

    def update(self):
        global time

        delay(0.01)
        time += 0.01

    def draw(self):
        self.image_back.clip_draw(0, 0, 482, 128, 400, 145, 805, 295)
        self.image_back.clip_draw(0, 135, 482, 150, 400, 145, 800, 290)
        self.image_logo2.draw(160, 230, 300, 40)
        self.image_character.draw(270, 100)

        if time > 2.5:
            self.image_logo1.draw(650, 50)


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
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if 575 < event.x < 725 and 37 < 290 - 1 - event.y < 63:
                game_framework.change_state(re_loading_scene)


def pause():
    pass


def resume():
    pass
