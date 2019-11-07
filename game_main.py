import random
import json
import os

from pico2d import *

import game_framework
import game_world
import select_scene

from obstacle_pink_jellyfish import Pink_Jellyfish
from obstacle_violet_jellyfish import Violet_Jellyfish
from obstacle_hand import Hand
from background import Background
from character_patrick import Patrick
from character_spongebob import Spongebob
from item_mr_krab import Mr_krab
from item_bubble import Bubble
from item_balloon import Balloon

name = "main"

obstacle_pink_jellyfish = None
obstacle_violet_jellyfish = None
obstacle_hand = None
character_spongebob = None
character_patrick = None
item_mr_krab = None
item_bubble = None
item_balloon = None
background = None


def enter():
    global obstacle_pink_jellyfish, obstacle_violet_jellyfish, obstacle_hand, character_spongebob, character_patrick, item_mr_krab, item_bubble, item_balloon, background
    obstacle_pink_jellyfish = Pink_Jellyfish()
    obstacle_violet_jellyfish = Violet_Jellyfish()
    obstacle_hand = Hand()
    character_spongebob = Spongebob()
    #character_patrick = Patrick()
    item_mr_krab = Mr_krab()
    item_bubble = Bubble()
    item_balloon = Balloon()
    background = Background()


def exit():
    global obstacle_pink_jellyfish, obstacle_violet_jellyfish, obstacle_hand, character_spongebob, character_patrick, item_mr_krab, item_bubble, item_balloon, background
    del obstacle_pink_jellyfish
    del obstacle_violet_jellyfish
    del obstacle_hand
    del character_spongebob
    #del character_patrick
    del item_mr_krab
    del item_bubble
    del item_balloon
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
    obstacle_hand.update()
    character_spongebob.update()
    #character_patrick.update()
    item_mr_krab.update()
    item_bubble.update()
    item_balloon.update()
    background.update()


def draw():
    clear_canvas()
    background.draw()
    character_spongebob.draw()
    #character_patrick.draw()
    obstacle_pink_jellyfish.draw()
    obstacle_violet_jellyfish.draw()
    obstacle_hand.draw()
    item_mr_krab.draw()
    item_bubble.draw()
    item_balloon.draw()
    update_canvas()
    delay(0.03)
