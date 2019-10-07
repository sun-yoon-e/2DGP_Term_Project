from pico2d import*

def key_event():
    frame = 0
    b1 = 633
    b2 = 633

    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                character.clip_draw(frame * 35, 0, 35, 40, 20, 40)
                update_canvas()
                frame = (frame + 1) % 4
                delay(0.05)
        elif event.key == SDL_KEYUP:
            clear_canvas()
            background.draw(b1, 80)
            background.draw(b2, -30)
            character.clip_draw(frame * 35, 45, 35, 40, 20, 20)
            update_canvas()

            frame = (frame + 1) % 6
            b1 -= 1
            b2 -= 1

            delay(0.03)
    pass

open_canvas(800, 107)

background = load_image('back.png')
character = load_image('char.png')

key_event()

close_canvas()