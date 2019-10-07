from pico2d import*

def key_event():
    global frame
    global playing
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            playing = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                playing = False
            elif event.key == SDLK_UP:
                character.clip_draw(frame * 35, 0, 35, 40, 20, 40)
                update_canvas()
                frame = (frame + 1) % 4
    pass

open_canvas(800, 107)
background = load_image('back.png')
character = load_image('char.png')

playing = True
frame = 0
b1 = 633
b2 = 633

while playing:
    clear_canvas()
    background.draw(b1, 80)
    background.draw(b2, -30)
    character.clip_draw(frame* 35, 45, 35, 40, 20, 20)
    update_canvas()

    key_event()
    frame = (frame + 1) % 6
    b1 -= 1
    b2 -= 1
    delay(0.03)
    get_events()

close_canvas()
