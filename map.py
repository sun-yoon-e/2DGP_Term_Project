from pico2d import*

open_canvas(1300, 600)

background = load_image('back.png')

frame = 0
b1, b2 = 2560, 2560

while True:
    clear_canvas()
    background.draw(b1, 390)
    background.draw(b2, -240)

    update_canvas()

    frame = (frame + 1) % 6
    b1 -= 1
    b2 -= 1
    delay(0.03)

close_canvas()
