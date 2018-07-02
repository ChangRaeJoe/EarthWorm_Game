import pygame as pg
from random import *
import constants as c

def item_init():
    items = []
    for i in range(0, 5):
        x = randint(0, c.WIDTH - c.RECT_WIDTH)
        y = randint(0, c.HEIGHT - c.RECT_HEIGHT)
        items.append([x, y])
    print (items)
    return items

def item_remove(items, index):
    del(items[index])
    return items

def item_add(items):
    x = randint(10, c.WIDTH - c.RECT_WIDTH)
    y = randint(10, c.HEIGHT - c.RECT_HEIGHT)
    items.append([x,y])
    return items

