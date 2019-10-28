import random
import json
import os

from pico2d import *

import game_framework
import select_scene

from obstacle_jellyfish import Jellyfish
from background import Background
from character_patrick import Patrick
from character_spongebob import Spongebob

name = "main"

obstacle_jellyfish = None
character_spongebob = None
background = None


def enter():
    global obstacle_jellyfish, character_spongebob, background
    obstacle_jellyfish = Jellyfish()
    character_spongebob = Spongebob()
    background = Background()


def exit():
    global obstacle_jellyfish, character_spongebob, background
    del obstacle_jellyfish
    del character_spongebob
    del background


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(select_scene)
        else:
            character_spongebob.handle_events(event)


def update():
    obstacle_jellyfish.update()
    character_spongebob.update()
    background.update()


def draw():
    clear_canvas()
    background.draw()
    character_spongebob.draw()
    obstacle_jellyfish.draw()
    update_canvas()
    delay(0.03)

