import game_framework
import game_start
from pico2d import *

name = "select"
image = None


def enter():
    global image
    image = load_image('resource/@Using/select.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(game_start)


def update():
    pass


def draw():
    clear_canvas()
    image.draw(400, 145, 800, 290)
    update_canvas()


def pause():
    pass


def resume():
    pass

