from pico2d import*
open_canvas()
background = load_image('background.png')
character = load_image('s3.png')

x = 0

while x < 800:
    clear_canvas()
    background.draw(400, 350)
    character.draw(x, 90)
    update_canvas()
    x += 5
    delay(0.05)
    get_events()

close_canvas()
