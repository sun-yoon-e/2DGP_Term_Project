from pico2d import *
import game_framework
import re_loading_scene

name = "over"
over = None
time = 0.0


class Over:
    def __init__(self):
        self.image_logo1 = load_image('resource/@Using/start button.png')
        self.image_logo2 = load_image('resource/@Using/game over logo.png')
        self.image_logo3 = load_image('resource/@Using/quit.png')
        self.image_character1 = load_image('resource/@Using/over.png')
        self.image_character2 = load_image('resource/@Using/over2.png')
        self.image_back = load_image('resource/@Using/over&success.png')

    def update(self):
        global time

        delay(0.01)
        time += 0.01

    def draw(self):
        self.image_back.clip_draw(0, 0, 482, 128, 400, 145, 805, 295)
        self.image_back.clip_draw(0, 135, 482, 150, 400, 145, 800, 290)
        self.image_logo2.draw(160, 230, 300, 40)

        if time < 2.0:
            self.image_character1.draw(220, 100)
        elif time >= 2.0:
            self.image_character2.draw(220, 100)
            self.image_logo1.draw(650, 65)
            self.image_logo3.draw(650, 25, 75, 20)



def enter():
    global over
    over = Over()


def exit():
    global over, time
    del over
    time = 0

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
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if 650 - 75 < event.x < 650 + 75 and 65 - 13 < 290 - 1 - event.y < 65 + 13:
                game_framework.change_state(re_loading_scene)
            elif 650 - 37 < event.x < 650 + 37 and 25 - 10 < 290 - 1 - event.y < 25 + 10:
                game_framework.quit()


def pause():
    pass


def resume():
    pass
