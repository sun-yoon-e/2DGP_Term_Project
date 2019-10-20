from pico2d import*

open_canvas(1441, 320)

map1 = load_image('map1.png')
map2 = load_image('map2.png')
map3 = load_image('map3.png')
map4 = load_image('map4.png')
b1, b2, b3, b4 = 1441, 2182, 2189, 2216

while True:
    clear_canvas()
    map1.draw(b1, 0)

    update_canvas()
    #b1 -= 50
   # delay(0.03)

close_canvas()
