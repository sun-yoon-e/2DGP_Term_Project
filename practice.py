from pico2d import*
open_canvas(800, 107)
background = load_image('back.png')
character = load_image('char.png')

frame = 0
b1 = 633
b2 = 633

while True:
    clear_canvas()
    background.draw(b1, 80)
    background.draw(b2, -30)
    character.clip_draw(frame* 35, 0, 35, 40, 20, 20)
    update_canvas()
    frame = (frame + 1) % 6
    b1 -= 3
    b2 -= 3
    delay(0.05)
    get_events()

close_canvas()
