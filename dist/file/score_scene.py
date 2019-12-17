import json
import pickle

from pico2d import *
import game_framework
import game_world
import game_over_scene
import game_success_scene

score = None
record = None
font = None
ranking = []


class Score:
    image = None

    def __init__(self):
        if Score.image is None:
            self.image = load_image('resource/@Using/rank.png')
            #self.image = load_image('resource/@Using/etc.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 145, 800, 290)

def enter():
    global score, font, ranking
    score = Score()

    if font is None:
        font = load_font('resource/font/ENCR10B.TTF', 20)

    with open('ranking.txt', 'r') as f:
        ranking = json.load(f)

    ranking.append(record)
    ranking.sort()
    ranking.reverse()

    while ranking.__len__() > 7:
        ranking.remove(ranking[-1])

    with open('ranking.txt', 'w') as f:
        json.dump(ranking, f)


def exit():
    global score
    del score


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
    global score
    score.update()

def draw():
    global score
    clear_canvas()
    score.draw()

    font.draw(get_canvas_width() // 2 - 250, get_canvas_height() // 2, "[My Record : %.2f]" % record)
    #font.draw(get_canvas_width() // 2 - 250, get_canvas_height() // 2, "[My Record : %.2f]" % record, (255, 255, 0))

    font.draw(get_canvas_width() // 2 + 50, get_canvas_height() // 2 + 105, "[Total Score]")
    #font.draw(get_canvas_width() // 2 + 50, get_canvas_height() // 2 + 105, "[Total Score]", (255, 255, 0))

    for i in range(0, ranking.__len__()):
        font.draw(get_canvas_width() // 2 + 80, get_canvas_height() // 2 + 70 - (30 * i),
                  "#" + str(i + 1) + ". " + '%.2f' % ranking[i])
        #font.draw(get_canvas_width() // 2 + 80, get_canvas_height() // 2 + 70 - (30 * i), "#" + str(i+1) + ". " + '%.2f' % ranking[i], (255, 255, 0))
    update_canvas()


def pause():
    pass


def resume():
    pass
