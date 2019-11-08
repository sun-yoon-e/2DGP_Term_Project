import game_framework
from pico2d import *

pause = None

class Pause:
    def __init__(self):
        self.image_back = load_image('resource/@Using/pause.png')
        self.image_continue = load_image('resource/@Using/continue.png')
        self.image_quit = load_image('resource/@Using/quit.png')

    def update(self):
        pass

    def draw(self):
        #self.image_back.draw(400, 145, 800, 290)
        self.image_back.composite_draw(3.141592 / 2, '', 400, 145, 290, 800)
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
        if event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.pop_state()
        elif event.type == SDL_QUIT:
            game_framework.quit()


def pause():
    pass


def resume():
    pass
