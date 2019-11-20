from pico2d import *
import game_main

name = "spongebob"

SPACE_UP, SPACE_DOWN = range(2)

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP
}

pi = 3.141592
angle = 0


class RunState:
    @staticmethod
    def enter(character_spongebob, event):
        character_spongebob.frame = 0
        character_spongebob.x = 100
        character_spongebob.y = 50

    @staticmethod
    def exit(character_spongebob, event):
        pass

    @staticmethod
    def do(character_spongebob):
        character_spongebob.frame = (character_spongebob.frame + 1) % 6

    @staticmethod
    def draw(character_spongebob):
        if game_main.Giant:
            character_spongebob.image.clip_draw(character_spongebob.frame * 83, 110, 83, 90, character_spongebob.x, character_spongebob.y + 10, 130, 120)
        else:
            character_spongebob.image.clip_draw(character_spongebob.frame * 83, 110, 83, 90, character_spongebob.x, character_spongebob.y)


class JumpState:
    @staticmethod
    def enter(character_spongebob, event):
        global angle
        angle = 0.0
        character_spongebob.frame = 0

    @staticmethod
    def exit(character_spongebob, event):
        pass

    @staticmethod
    def do(character_spongebob):
        global angle, radian, pi
        character_spongebob.frame = (character_spongebob.frame + 1) % 3
        radian = math.radians(angle)
        character_spongebob.y = 180 * math.sin(radian * pi) + 100

    @staticmethod
    def draw(character_spongebob):
        if game_main.Giant:
            character_spongebob.image.clip_draw(character_spongebob.frame * 75, 0, 75, 105, character_spongebob.x,
                                                character_spongebob.y, 130, 150)
        else:
            character_spongebob.image.clip_draw(character_spongebob.frame * 75, 0, 75, 105, character_spongebob.x, character_spongebob.y)


next_state_table = {
    RunState: {SPACE_DOWN: JumpState, SPACE_UP: RunState},
    JumpState: {SPACE_DOWN: JumpState, SPACE_UP: RunState}
}


class Spongebob:
    def __init__(self):
        self.x, self.y = 100, 50
        self.frame = 0
        self.image = load_image('resource/@Using/spongebob.png')
        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x, self.y - 45, self.x + 35, self.y + 45

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
