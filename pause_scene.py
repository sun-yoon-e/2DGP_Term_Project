from pico2d import *
import game_framework
import game_over_scene

name = "pause"
pause = None


class Pause:
    def __init__(self):
        self.image_back = load_image('resource/@Using/pause.png')
        self.image_continue = load_image('resource/@Using/continue.png')
        self.image_quit = load_image('resource/@Using/quit.png')

    def update(self):
        pass

    def draw(self):
        #self.image_back.draw(400, 145, 800, 290) #회전 x
        self.image_back.composite_draw(3.141592 / 2, '', 400, 145, 290, 800) #회전 o
        self.image_continue.draw(400, 210)
        self.image_quit.draw(400, 70)


def enter():
    global pause
    pause = Pause()


def exit():
    global pause
    del pause


def update():
    global pause
    pause.update()


def draw():
    global pause
    clear_canvas()
    pause.update()
    pause.draw()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if 100 < event.x < 700 and 170 < 290 - 1 - event.y < 250:
                game_framework.pop_state()
            elif 250 < event.x < 550 and 30 < 290 - 1 - event.y < 110:
                game_framework.change_state(game_over_scene)


def pause():
    pass


def resume():
    pass

