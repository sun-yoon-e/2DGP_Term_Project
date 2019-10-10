from pico2d import*

open_canvas(1500, 780)

map1 = load_image('p1.png')
map2 = load_image('p2.png')
map3 = load_image('p3.png')
map4 = load_image('p4.png')
b1, b2, b3, b4 = 2882, 4365, 4379, 4432

while True:
    if b1 > -2882:
        clear_canvas()
        map1.draw(b1, 1182)
        map1.draw(b1, 390)
        map1.draw(b1, -400)

        update_canvas()
        b1 -= 50
        delay(0.03)

        # 내일 해볼 것 : map1이 마지막 1500픽셀이 지나갈때 and map2가 처음 1500픽셀이 지나갈때 둘이 한꺼번에 update_canvas() 해보기
        if b1 <= -1382 and b2 > -2882:
            clear_canvas()
            map2.draw(b2, 1182)
            map2.draw(b2, 390)
            map2.draw(b2, -400)

            update_canvas()
            b2 -= 50
            delay(0.03)

            if b2 <= -1352 and b3 > -2882:
                clear_canvas()
                map3.draw(b3, 1182)
                map3.draw(b3, 390)
                map3.draw(b3, -400)

                update_canvas()
                b3 -= 50
                delay(0.03)

                if b3 <= -1322 and b4 > -2882:
                    clear_canvas()
                    map4.draw(b4, 1182)
                    map4.draw(b4, 390)
                    map4.draw(b4, -400)

                    update_canvas()
                    b4 -= 50
                    delay(0.03)

close_canvas()
