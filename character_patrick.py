from pico2d import *
import game_main

name = "patrick"

SPACE_UP, SPACE_DOWN = range(2)

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP
}

pi = 3.141592
angle = 0


class RunState:
    @staticmethod
    def enter(character_patrick, event):
        character_patrick.frame = 0
        character_patrick.x = 100
        character_patrick.y = 50

    @staticmethod
    def exit(character_patrick, event):
        pass

    @staticmethod
    def do(character_patrick):
        character_patrick.frame = (character_patrick.frame + 1) % 3

    @staticmethod
    def draw(character_patrick):
        if game_main.Giant:
            character_patrick.image.clip_draw(character_patrick.frame * 93, 0, 93, 105, character_patrick.x, character_patrick.y + 10, 140, 130)
        else:
            character_patrick.image.clip_draw(character_patrick.frame * 93, 0, 93, 105, character_patrick.x, character_patrick.y)


class JumpState:
    @staticmethod
    def enter(character_patrick, event):
        global angle
        angle = 0.0
        character_patrick.frame = 0

    @staticmethod
    def exit(character_patrick, event):
        pass

    @staticmethod
    def do(character_patrick):
        global angle, radian, pi
        character_patrick.frame = (character_patrick.frame + 1) % 3
        radian = math.radians(angle)
        character_patrick.y = 180 * math.sin(radian * pi) + 100

    @staticmethod
    def draw(character_patrick):
        if game_main.Giant:
            character_patrick.image.clip_draw(character_patrick.frame * 93, 105, 93, 105, character_patrick.x,
                                              character_patrick.y, 140, 120)
        else:
            character_patrick.image.clip_draw(character_patrick.frame * 93, 105, 93, 105, character_patrick.x, character_patrick.y)


next_state_table = {
    RunState: {SPACE_DOWN: JumpState, SPACE_UP: RunState},
    JumpState: {SPACE_DOWN: JumpState, SPACE_UP: RunState}
}


class Patrick:
    image = None

    def __init__(self):
        if Patrick.image is None:
            self.image = load_image('resource/@Using/patrick.png')

        self.x, self.y = 100, 50
        self.frame = 0
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
