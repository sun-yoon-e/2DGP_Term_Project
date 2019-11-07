import random
import json
import os

from pico2d import *

import game_framework
import game_world
import select_scene
import pause_scene

from obstacle_pink_jellyfish import Pink_Jellyfish
from obstacle_violet_jellyfish import Violet_Jellyfish
from obstacle_hand import Hand
from background import Background
from character_patrick import Patrick
from character_spongebob import Spongebob
from item_mr_krab import Mr_krab
from item_bubble import Bubble
from item_balloon import Balloon

name = "game_main"

background = None
obstacle_hand = None
obstacle_pink_jellyfish = None
obstacle_violet_jellyfish = None
item_balloon = None
item_bubble = None
item_mr_krab = None
character_spongebob = None
character_patrick = None


def enter():
    global obstacle_pink_jellyfish, obstacle_violet_jellyfish, obstacle_hand, character_spongebob, character_patrick, item_mr_krab, item_bubble, item_balloon, background
    background = Background()
    obstacle_hand = Hand()
    obstacle_pink_jellyfish = Pink_Jellyfish()
    obstacle_violet_jellyfish = Violet_Jellyfish()
    item_balloon = Balloon()
    item_bubble = Bubble()
    item_mr_krab = Mr_krab()
    character_spongebob = Spongebob()
    #character_patrick = Patrick()

    game_world.add_object(background, 0)
    game_world.add_object(obstacle_hand, 1)
    game_world.add_object(obstacle_pink_jellyfish, 2)
    game_world.add_object(obstacle_violet_jellyfish, 3)
    game_world.add_object(item_balloon, 4)
    game_world.add_object(item_bubble, 5)
    game_world.add_object(item_mr_krab, 6)
    game_world.add_object(character_spongebob, 7)
    #game_world.add_object(character_patrick, 8)


def exit():
    global obstacle_pink_jellyfish, obstacle_violet_jellyfish, obstacle_hand, character_spongebob, character_patrick, item_mr_krab, item_bubble, item_balloon, background
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        #elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            #game_framework.change_state(select_scene)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_scene)
        else:
            character_spongebob.handle_events(event)
            #character_patrick.handle_events(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
    delay(0.03)
