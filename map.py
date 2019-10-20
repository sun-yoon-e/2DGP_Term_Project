from pico2d import*

open_canvas(1200, 290)

map1 = load_image('map1.png')
map2 = load_image('map2.png')
map3 = load_image('map3.png')
map4 = load_image('map4.png')
b1, b2 = 1441, 2882

while True:
    clear_canvas()
    map1.clip_draw(0, 0, 2882, 350, b1, 145)
    map1.clip_draw(0, 600, 2882, 365, b1, 120)
    map1.clip_draw(0, 305, 2882, 340, b1, 150)

    if b1 <= -241 and b2 >= 1441:
        map1.clip_draw(0, 0, 2882, 350, b1, 145)
        map1.clip_draw(0, 600, 2882, 365, b1, 120)
        map1.clip_draw(0, 305, 2882, 340, b1, 150)
        map2.clip_draw(0, 0, 2882, 350, b2, 150)
        update_canvas()

    update_canvas()
    b1 -= 30
    b2 -= 30
    delay(0.03)


close_canvas()
