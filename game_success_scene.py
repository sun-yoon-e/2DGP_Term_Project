from pico2d import *
import game_framework
import re_loading_scene
import score_scene

name = "success"
success = None
time = 0.0
ranking = False


class Success:
    image_logo1 = None
    image_logo2 = None
    image_logo3 = None
    image_character = None
    image_back = None

    def __init__(self):
        if Success.image_logo1 is None:
            self.image_logo1 = load_image('resource/@Using/start button.png')
        if Success.image_logo2 is None:
            self.image_logo2 = load_image('resource/@Using/complete.png')
        if Success.image_logo3 is None:
            self.image_logo3 = load_image('resource/@Using/quit.png')
        if Success.image_character is None:
            self.image_character = load_image('resource/@Using/success.png')
        if Success.image_back is None:
            self.image_back = load_image('resource/@Using/over&success.png')

    def update(self):
        global time

        delay(0.01)
        time += 0.01

    def draw(self):
        self.image_back.clip_draw(0, 0, 482, 128, 400, 145, 805, 295)
        self.image_back.clip_draw(0, 135, 482, 150, 400, 145, 800, 290)
        self.image_logo2.draw(160, 228, 300, 40)
        self.image_character.draw(270, 100)

        if time > 2.5:
            self.image_logo1.draw(650, 65)
            self.image_logo3.draw(650, 25, 75, 20)


def enter():
    global success
    success = Success()


def exit():
    global success, ranking
    del success
    ranking = False


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
    global ranking
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
            game_framework.change_state(score_scene)
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if 650 - 75 < event.x < 650 + 75 and 65 - 13 < 290 - 1 - event.y < 65 + 13:
                game_framework.change_state(re_loading_scene)
            elif 650 - 37 < event.x < 650 + 37 and 25 - 10 < 290 - 1 - event.y < 25 + 10:
                game_framework.quit()


def pause():
    pass


def resume():
    pass
