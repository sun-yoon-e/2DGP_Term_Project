from pico2d import *
import game_framework
import game_world
import game_over_scene
import game_main

name = "pause"
pause = None


class Pause:
    image_back = None
    image_continue = None
    image_quit = None

    def __init__(self):
        if Pause.image_back is None:
            self.image_back = load_image('resource/@Using/pause.png')
        if Pause.image_continue is None:
            self.image_continue = load_image('resource/@Using/continue.png')
        if Pause.image_quit is None:
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
    pause.draw()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            if 400 - 300 < event.x < 400 +300 and 210 - 40 < 290 - 1 - event.y < 210 + 40:
                game_framework.pop_state()
                game_main.bgm.resume()
            elif 400 - 150 < event.x < 400 + 150 and 70 - 40 < 290 - 1 - event.y < 70 + 40:
                game_framework.change_state(game_over_scene)
                game_world.clear()
                game_main.bgm.stop()


def pause():
    pass


def resume():
    pass
