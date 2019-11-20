import random
import json
import os

from pico2d import *
import game_framework
import game_world
import game_success_scene
import game_over_scene
import select_scene
import pause_scene

from obstacle_pink_jellyfish import Pink_Jellyfish
from obstacle_violet_jellyfish import Violet_Jellyfish
from obstacle_hand import Hand
from background import Background
from character_patrick import Patrick
from character_spongebob import Spongebob
from item_krabby_patty import Krabby_Patty
from item_mr_krab import Mr_krab

name = "main"

background = None
obstacles = None

#obstacle_hand = None
#obstacle_pink_jellyfish = None
#obstacle_violet_jellyfish = None
#items = None

item_krabby_patty = None
item_mr_krab = None
character_spongebob = None
character_patrick = None

Giant = False
Giant_time = 0.0


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def enter():
    global obstacle_pink_jellyfish, obstacle_violet_jellyfish, obstacle_hand, character_spongebob, character_patrick, item_mr_krab, item_krabby_patty, background
    background = Background()
    obstacle_hand = Hand()
    obstacle_pink_jellyfish = Pink_Jellyfish()
    obstacle_violet_jellyfish = Violet_Jellyfish()
    item_krabby_patty = Krabby_Patty()
    item_mr_krab = Mr_krab()
    if select_scene.select == 1:
        character_spongebob = Spongebob()
    elif select_scene.select == 2:
        character_patrick = Patrick()

    game_world.add_object(background, 0)

    # global obstacles
    # obstacles = [Hand() for i in range(1)] + [Pink_Jellyfish() for i in range(1)] + [Violet_Jellyfish() for i in range(1)]
    # game_world.add_objects(obstacles, 1)

    game_world.add_object(obstacle_hand, 1)
    game_world.add_object(obstacle_pink_jellyfish, 1)
    game_world.add_object(obstacle_violet_jellyfish, 1)

    # global items
    # items = [Krabby_Patty() for i in range(1)] + [Mr_krab() for i in range(1)]
    # game_world.add_objects(items, 1)

    game_world.add_object(item_krabby_patty, 1)
    game_world.add_object(item_mr_krab, 1)

    if select_scene.select == 1:
        game_world.add_object(character_spongebob, 1)
    elif select_scene.select == 2:
        game_world.add_object(character_patrick, 1)


def exit():
    global obstacle_pink_jellyfish, obstacle_violet_jellyfish, obstacle_hand, character_spongebob, character_patrick, item_mr_krab, item_krabby_patty, background
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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_state(pause_scene)

        # (확인용) 키 입력 시 화면 전환
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.change_state(game_success_scene)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_o:
            game_framework.change_state(game_over_scene)
        else:
            if select_scene.select == 1:
                character_spongebob.handle_events(event)
            elif select_scene.select == 2:
                character_patrick.handle_events(event)


def update():
    global Giant, Giant_time

    for game_object in game_world.all_objects():
        game_object.update()

    if Giant:
        Giant_time += 0.01
        if Giant_time >= 2.0:
            Giant_time = 0.0
            Giant = False

    if select_scene.select == 1:
        if collide(character_spongebob, obstacle_hand):
            if Giant:
                obstacle_hand.x = -10
            if not Giant:
                game_framework.change_state(game_over_scene)
                game_world.clear()
        if collide(character_spongebob, obstacle_pink_jellyfish):
            if Giant:
                obstacle_pink_jellyfish.x = -10
            if not Giant:
                game_framework.change_state(game_over_scene)
                game_world.clear()
        if collide(character_spongebob, obstacle_violet_jellyfish):
            if Giant:
                obstacle_violet_jellyfish.x = -10
            if not Giant:
                game_framework.change_state(game_over_scene)
                game_world.clear()

        if collide(character_spongebob, item_krabby_patty):
            Giant = True
            Giant_time = 0.0
            item_krabby_patty.x = -10

        if collide(character_spongebob, item_mr_krab):
            obstacle_hand.x = -10
            obstacle_pink_jellyfish.x = -10
            obstacle_violet_jellyfish.x = -10
            item_mr_krab.x = -10

    elif select_scene.select == 2:
        if collide(character_patrick, obstacle_hand):
            if Giant:
                obstacle_hand.x = -10
            if not Giant:
                game_framework.change_state(game_over_scene)
                game_world.clear()
        if collide(character_patrick, obstacle_pink_jellyfish):
            if Giant:
                obstacle_pink_jellyfish.x = -10
            if not Giant:
                game_framework.change_state(game_over_scene)
                game_world.clear()
        if collide(character_patrick, obstacle_violet_jellyfish):
            if Giant:
                obstacle_violet_jellyfish.x = -10
            if not Giant:
                game_framework.change_state(game_over_scene)
                game_world.clear()

        if collide(character_patrick, item_krabby_patty):
            Giant = True
            Giant_time = 0.0
            item_krabby_patty.x = -10

        if collide(character_patrick, item_mr_krab):
            obstacle_hand.x = -10
            obstacle_pink_jellyfish.x = -10
            obstacle_violet_jellyfish.x = -10
            item_mr_krab.x = -10


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
    delay(0.03)
