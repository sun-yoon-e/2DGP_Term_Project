import game_framework
import pico2d
import loading_scene

name = "exe"

pico2d.open_canvas(800,290)
game_framework.run(loading_scene)
pico2d.close_canvas()