from pico2d import*

open_canvas(1500, 780)

map1 = load_image('p1.png')
map2 = load_image('p2.png')
b1, b2 = 2883, 5764

while True:
    if b1 > -5000:
        clear_canvas()
        map1.draw(b1, 1182)
        map1.draw(b1, 390)
        map1.draw(b1, -400)

        update_canvas()
        b1 -= 30
        delay(0.03)

        if b1 <= -1264 and b2 > -2882:
            clear_canvas()
            map2.draw(b2, 1182)
            map2.draw(b2, 390)
            map2.draw(b2, -400)

            update_canvas()
            b2 -= 3
            delay(0.03)


close_canvas()
