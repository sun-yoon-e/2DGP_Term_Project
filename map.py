from pico2d import*

open_canvas(1500, 290)

map1 = load_image('map1.png')
map2 = load_image('map2.png')
map3 = load_image('map3.png')
map4 = load_image('map4.png')
b1, b2, b3, b4 = 1441, 2641, 2641, 2641

while True:
    clear_canvas()

    if b1 >= -1441:
        map1.clip_draw(0, 0, 2882, 350, b1, 145)
        map1.clip_draw(0, 600, 2882, 365, b1, 120)
        map1.clip_draw(0, 305, 2882, 340, b1, 150)
        b1 -= 20

    if b1 <= -241 and b2 >= -1441:
        map2.clip_draw(0, 300, 2882, 330, b2, 160)
        map2.clip_draw(0, 600, 2882, 400, b2, 120)
        b2 -= 20

    if b2 <= -241 and b3 >= -1441:
        map3.clip_draw(0, 300, 2882, 330, b3, 310)
        map3.clip_draw(0, 500, 2882, 325, b3, 160)
        b3 -= 20

    if b3 <= -241 and b4 >= -1441:
        map4.clip_draw(0, 0, 2882, 350, b4, 145)
        map4.clip_draw(0, 600, 2882, 340, b4, 110)
        map4.clip_draw(0, 305, 2882, 330, b4, 160)
        b4 -= 20

    update_canvas()
    delay(0.03)

close_canvas()
