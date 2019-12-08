from pico2d import *
import game_framework
import select_scene

name = "re-loading"
re_loading = None
time = 0.0
bgm = None


def enter():
    global bgm, re_loading
    re_loading = load_image('resource/@Using/few.png')

    bgm = load_music('resource/bgm/loading.mp3')
    bgm.set_volume(64)
    bgm.play(1)

def exit():
    global bgm, re_loading
    del re_loading
    bgm.stop()


def update():
    global time

    if time > 2.0:
        time = 0
        game_framework.change_state(select_scene)
    delay(0.01)
    time += 0.01


def draw():
    global re_loading
    clear_canvas()
    re_loading.draw(400, 145, 800, 290)
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
