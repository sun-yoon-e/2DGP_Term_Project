import game_framework
import title
from pico2d import *

name = "start"
image = None
time = 0.0

def enter():
    global  image
    image = load_image()