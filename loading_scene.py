from pico2d import *
import game_framework
import select_scene

name = "loading"
image1, image2, image3 = None, None, None
time = 0.0


def enter():
    global image1, image2, image3
    image1 = load_image('resource/@Using/start_image1.jpg')
    image2 = load_image('resource/@Using/start_image2.png')
    image3 = load_image('resource/@Using/loading_image.png')


def exit():
    global image1, image2, image3
    del image1
    del image2
    del image3


def update():
    global time

    if time > 2.0:
        time = 0
        game_framework.change_state(select_scene)
    delay(0.01)
    time += 0.01


def draw():
    global image1, image2
    clear_canvas()
    if time < 0.7:
        image1.draw(400, 145, 800, 290)
    elif 0.7 <= time < 1.3:
        image2.draw(400, 145, 800, 290)
    elif time >= 1.3:
        image3.draw(400, 145, 800, 290)
    update_canvas()


def handle_events():
    events = get_events()


def pause():
    pass


def resume():
    pass
