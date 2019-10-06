from pico2d import*
open_canvas(1266, 712)
background = load_image('background.png')
character = load_image('s3.png')

x = 0
b1 = 633
b2 = 0

while x < 800:
    clear_canvas()
    background.draw(b1, 356)
    b1 += 3
    background.draw(b2, 356)
    b2 += 3
    character.draw(x, 90)
    update_canvas()
    x += 5
    delay(0.05)
    get_events()

close_canvas()
