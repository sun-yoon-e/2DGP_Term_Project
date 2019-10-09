from pico2d import*

open_canvas(1500, 780)

background = load_image('p1.png')

frame = 0
b1, b2, b3 = 2883, 2883, 2883

while True:
    while b1 > - 2882:
        clear_canvas()
        background.draw(0, 0)
        background.draw(b1, 1182)
        background.draw(b2, 390)
        background.draw(b3, -400)

        update_canvas()

        frame = (frame + 1) % 6
        b1 -= 3
        b2 -= 3
        b3 -= 3
        delay(0.03)

close_canvas()
