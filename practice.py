from pico2d import*

def key_event():
    global frame
    global b1, b2

    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                #update_canvas()
                character.clip_draw(frame * 35, 0, 35, 40, 20, 40)
                update_canvas()
                frame = (frame + 1) % 4
                delay(0.03)

    pass

open_canvas(800, 155)

background = load_image('p2.png')
character = load_image('char.png')

frame = 0
b1, b2 = 633, 633

while True:
    clear_canvas()
    background.draw(b1, 101)
    background.draw(b2, -60)

    character.clip_draw(frame * 35, 45, 35, 40, 20, 20)
    update_canvas()

    frame = (frame + 1) % 6
    b1 -= 1
    b2 -= 1
    delay(0.03)

    key_event()

close_canvas()
