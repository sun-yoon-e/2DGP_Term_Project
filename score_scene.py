import json
import pickle

from pico2d import *
import game_framework
import game_world
import game_over_scene
import game_success_scene


font = None
record = None
ranking = []


def enter():
    global font, ranking
    if font is None:
        font = load_font('resource/font/ENCR10B.TTF', 20)

    with open('ranking.txt', 'r') as f:
        ranking = json.load(f)

    ranking.append(record)
    ranking.sort()
    ranking.reverse()

    while ranking.__len__() > 5:
        ranking.remove(ranking[-1])

    with open('ranking.txt', 'w') as f:
        json.dump(ranking, f)


def exit():
    game_world.clear()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE and game_success_scene.ranking:
            game_framework.change_state(game_success_scene)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE and game_over_scene.ranking:
            game_framework.change_state(game_over_scene)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    font.draw(get_canvas_width() // 2, get_canvas_height() // 2 + 70, "[My Record : %.2f]" % record)
    font.draw(get_canvas_width() // 2, get_canvas_height() // 40, "[Total Score]")

    for i in range(0, ranking.__len__()):
        font.draw(get_canvas_width() // 2 - 80, get_canvas_height() // 2 + 100 - 20 * i, "#" + str(i+1) + ". " + '%.2f' % ranking[i])
    update_canvas()


def pause():
    pass


def resume():
    pass
