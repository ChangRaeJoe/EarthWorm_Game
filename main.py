import pygame as pg
import constants as c
from time import sleep
import random

def edged():
    direction = [pg.K_DOWN, pg.K_LEFT, pg.K_UP, pg.K_RIGHT]
    dir_choice = random.choice(direction)
    return dir_choice

def limit(xy):
    global speed
    x = xy[0]
    y = xy[1]
    tmp_key = xy[2]
    if c.WIDTH - c.RECT_WIDTH < x: #막는 동시에 방향을 바꿔준다.
        x -= c.SPEED + speed
        tmp_key = edged()
    elif 0>x:
        x = 0
        tmp_key = edged()

    if c.HEIGHT - c.RECT_HEIGHT< y:
        y -= c.SPEED + speed
        tmp_key = edged()
    elif 0>y:
        y = 0
        tmp_key = edged()
    return (x, y, tmp_key)

def auto_moved(box_one):
    global speed
    x = box_one[0]
    y = box_one[1]
    keys = box_one[2]

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
    init_x = 0
    init_y = 0
    change_width = 0
    change_height = 0
    #지렁이 [x, y, direction]
    earth_w = []
    for i in range(0, 50):
        earth_w.append([c.RECT_X, c.RECT_Y, 0])


    #값들 변경
    smile = False
    speed = 0
    while not smile:
        #키 동작
        for event in pg.event.get():
            if event.type == pg.QUIT:
                smile = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RIGHT:
                    earth_w[0][2] = pg.K_RIGHT
                elif event.key == pg.K_LEFT:
                    earth_w[0][2] = pg.K_LEFT
                elif event.key == pg.K_UP:
                    earth_w[0][2] = pg.K_UP
                elif event.key == pg.K_DOWN:
                    earth_w[0][2] = pg.K_DOWN

        #상태값바꾸기
        #for index, xy in enumerate(earth_w):
        #   earth_w[index][0], earth_w[index][1] = auto_moved(xy)
        #   earth_w[index][0], earth_w[index][1], earth_w[index][2] = limit(xy)

        for index, xy in enumerate(earth_w):

            next = index+1
            if index == 0:
                cur_x, cur_y = earth_w[index][0], earth_w[index][1]
                pre_x = earth_w[next][0]
                pre_y = earth_w[next][1]
                earth_w[next][0], earth_w[next][1] = cur_x, cur_y
                earth_w[index][0], earth_w[index][1] = auto_moved(xy)
                earth_w[index][0], earth_w[index][1], earth_w[index][2] = limit(xy)
            elif index < len(earth_w)-1:
                cur_x, cur_y = pre_x, pre_y
                pre_x = earth_w[next][0]
                pre_y = earth_w[next][1]
                earth_w[next][0], earth_w[next][1] = cur_x, cur_y
                print(earth_w[index][2])
        #print (keys)
        #화면그리기
        screen.fill(0)
        for index, xy in enumerate(earth_w):
            pg.draw.rect(screen, c.RED, (earth_w[index][0], earth_w[index][1], c.RECT_WIDTH, c.RECT_HEIGHT))

        pg.draw.circle(screen, c.BLUE, (100,100), 10)
        pg.display.flip()
        clock.tick(c.SCREEN_FPS)
        if smile==True:
            pg.quit()