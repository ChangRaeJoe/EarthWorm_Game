import pygame as pg
import item, main
import constants as c

def eat(earth_w, items):
    for i, xy in enumerate(earth_w):
        center_x = xy[0]+ c.RECT_WIDTH*2/3
        center_y = xy[1] + c.RECT_HEIGHT*2/3
        for j, mn in enumerate(items):
            if center_x> mn[0] and center_x<mn[0]+c.RECT_WIDTH and center_y >mn[1] and center_y<mn[1]+c.RECT_HEIGHT:
                items = item.item_remove(items, j)
                earth_w =user_add(earth_w)
                items = item.item_add(items)
                break;
    return earth_w, items

def user_add(earth_w):
    earth_w.append([c.RECT_X, c.RECT_Y, 0])
    print (earth_w)
    return earth_w

def crash(earth_w):
    dots = []
    if earth_w[0][2] == pg.K_RIGHT:
        dots.append([earth_w[0][0] + c.RECT_WIDTH, earth_w[0][1]])
        dots.append([earth_w[0][0] + c.RECT_WIDTH, earth_w[0][1] + c.RECT_HEIGHT])
    elif earth_w[0][2] == pg.K_LEFT:
        dots.append([earth_w[0][0], earth_w[0][1]])
        dots.append([earth_w[0][0], earth_w[0][1] + c.RECT_HEIGHT])
    elif earth_w[0][2] == pg.K_UP:
        dots.append([earth_w[0][0], earth_w[0][1]])
        dots.append([earth_w[0][0] + c.RECT_WIDTH, earth_w[0][1]])
    elif earth_w[0][2] == pg.K_DOWN:
        dots.append([earth_w[0][0] + c.RECT_WIDTH, earth_w[0][1] + c.RECT_HEIGHT])
        dots.append([earth_w[0][0], earth_w[0][1] + c.RECT_HEIGHT])


    for i, xy in enumerate(dots):
        cnt = 0
        for j, mn in enumerate(earth_w):
            if j == 0: continue #first box<- head
            # 1. xy[1] is rect along
            # 2. xy[0] is small than mn's x
            if xy[1]>=mn[1] and xy[1]<=mn[1]+c.RECT_HEIGHT:
                if xy[0] >= mn[0] and xy[0] <= mn[0]+c.RECT_WIDTH:
                    return 1
    return 0



