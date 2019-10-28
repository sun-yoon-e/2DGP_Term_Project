import game_framework
import game_start
from pico2d import *

name = "select"
image = None
spongebob = None
patrick = None


def enter():
    global image, spongebob, patrick, frame1, frame2
    image = load_image('resource/@Using/select.png')
    spongebob = load_image('resource/@Using/spongebob_select.png')
    patrick = load_image('resource/@Using/patrick_select.png')
    frame1, frame2 = 0, 0


def exit():
    global image, spongebob, patrick
    del image
    del spongebob
    del patrick


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
    global frame1, frame2
    frame1 = (frame1 + 1) % 5
    frame2 = (frame2 + 1) % 4


def draw():
    global frame1, frame2
    clear_canvas()
    image.draw(400, 145, 800, 290)
    spongebob.clip_draw(frame1 * 100, 0, 100, 120, 300, 80)
    #patrick.clip_draw(frame2 * 109, 0, 109, 130, 500, 80)
    patrick.clip_draw(frame2 * 100, 0, 100, 141, 500, 90)
    update_canvas()
    delay(0.13)


def pause():
    pass


def resume():
    pass

