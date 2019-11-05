import random
import json
import os

from pico2d import *

import game_framework
import select_scene

from obstacle_pink_jellyfish import Pink_Jellyfish
from obstacle_violet_jellyfish import Violet_Jellyfish
from background import Background
from character_patrick import Patrick
from character_spongebob import Spongebob
from item_mr_krab import Mr_krab
from item_bubble import Bubble

name = "main"

obstacle_pink_jellyfish = None
obstacle_violet_jellyfish = None
character_spongebob = None
character_patrick = None
mr_krab = None
bubble = None
background = None


def enter():
    global obstacle_pink_jellyfish, obstacle_violet_jellyfish, character_spongebob, character_patrick, mr_krab, bubble, background
    obstacle_pink_jellyfish = Pink_Jellyfish()
    obstacle_violet_jellyfish = Violet_Jellyfish()
    character_spongebob = Spongebob()
    #character_patrick = Patrick()
    mr_krab = Mr_krab()
    bubble = Bubble()
    background = Background()


def exit():
    global obstacle_pink_jellyfish, obstacle_violet_jellyfish, character_spongebob, character_patrick, mr_krab, bubble, background
    del obstacle_pink_jellyfish
    del obstacle_violet_jellyfish
    del character_spongebob
    #del character_patrick
    del mr_krab
    del bubble
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
            #character_patrick.handle_events(event)


def update():
    obstacle_pink_jellyfish.update()
    obstacle_violet_jellyfish.update()
    character_spongebob.update()
    #character_patrick.update()
    mr_krab.update()
    bubble.update()
    background.update()


def draw():
    clear_canvas()
    background.draw()
    character_spongebob.draw()
    #character_patrick.draw()
    obstacle_pink_jellyfish.draw()
    obstacle_violet_jellyfish.draw()
    mr_krab.draw()
    bubble.draw()
    update_canvas()
    delay(0.03)
