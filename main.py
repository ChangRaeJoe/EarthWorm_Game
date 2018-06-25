import pygame as pg
import constants as c
from time import sleep
import random

def edged():
    global keys
    direction = [pg.K_DOWN, pg.K_LEFT, pg.K_UP, pg.K_RIGHT]
    i = random.choice(direction)
    keys = i

def limit(x, y):
    global speed
    if c.WIDTH - c.RECT_WIDTH < x: #막는 동시에 방향을 바꿔준다.
        x -= c.SPEED + speed
        edged()
    elif 0>x:
        x = 0
        edged()

    if c.HEIGHT - c.RECT_HEIGHT< y:
        y -= c.SPEED + speed
        edged()
    elif 0>y:
        y = 0
        edged()
    return (x, y)

def auto_moved(x, y, keys):
    global speed

    if keys == pg.K_RIGHT:
        x += c.SPEED + speed
    elif keys == pg.K_LEFT:
        x -= c.SPEED + speed
    elif keys == pg.K_UP:
        y -= c.SPEED + speed
    elif keys == pg.K_DOWN:
        y += c.SPEED + speed
    return (x, y)

if __name__ == '__main__':
    pg.init()
    pg.display.set_caption('EarthWorm Game()')
    screen = pg.display.set_mode((c.WIDTH, c.HEIGHT))
    clock = pg.time.Clock()
    change_x = 0
    change_y = 0
    change_width = 0
    change_height = 0

    smile = False
    keys = 0
    speed = 0
    while not smile:
        #키 동작
        for event in pg.event.get():
            if event.type == pg.QUIT:
                smile = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    change_x += c.SPEED + speed
                    keys = pg.K_RIGHT
                elif event.key == pg.K_LEFT:
                    change_x -= c.SPEED+ speed
                    keys = pg.K_LEFT
                elif event.key == pg.K_UP:
                    change_y -= c.SPEED+ speed
                    keys = pg.K_UP
                elif event.key == pg.K_DOWN:
                    change_y += c.SPEED+ speed
                    keys = pg.K_DOWN
        change_x, change_y = auto_moved(change_x, change_y, keys)
        #상태값바꾸기
        change_x, change_y = limit(change_x, change_y)
        print (change_x, change_y, keys)
        #화면그리기
        screen.fill(0)
        pg.draw.rect(screen, c.RED, (change_x, change_y, c.RECT_WIDTH, c.RECT_HEIGHT))
        pg.draw.circle(screen, c.BLUE, (100,100), 10)
        pg.display.flip()
        clock.tick(c.SCREEN_FPS)
        if smile==True:
            pg.quit()