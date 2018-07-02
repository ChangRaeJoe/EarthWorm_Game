import pygame as pg
import item, main
import constants as c

class User:
    def __init__(self, earth_w, items):
        self.set_data(earth_w, items)

    def set_data(self, earth_w, items):
        self.earth_w = earth_w
        self.items = items

    def eat(self):
        for i, xy in enumerate(self.earth_w):
            center_x = xy[0] + c.RECT_WIDTH * 2 / 3
            center_y = xy[1] + c.RECT_HEIGHT * 2 / 3
            for j, mn in enumerate(self.items):
                if center_x > mn[0] and center_x < mn[0] + c.RECT_WIDTH and center_y > mn[1] and center_y < mn[
                    1] + c.RECT_HEIGHT:
                    items = item.item_remove(self.items, j)
                    self.earth_w = self.add()
                    self.items = item.item_add(items)
                    return 1
        return 0
    def add(self):
        last_x = self.earth_w[len(self.earth_w) - 1][0]
        last_y = self.earth_w[len(self.earth_w) - 1][1]
        self.earth_w.append([last_x, last_y, 0])
        print(self.earth_w)
        return self.earth_w

    def crash(self):
        dots = []
        if self.earth_w[0][2] == pg.K_RIGHT:
            dots.append([self.earth_w[0][0] + c.RECT_WIDTH, self.earth_w[0][1]])
            dots.append([self.earth_w[0][0] + c.RECT_WIDTH, self.earth_w[0][1] + c.RECT_HEIGHT])
        elif self.earth_w[0][2] == pg.K_LEFT:
            dots.append([self.earth_w[0][0], self.earth_w[0][1]])
            dots.append([self.earth_w[0][0], self.earth_w[0][1] + c.RECT_HEIGHT])
        elif self.earth_w[0][2] == pg.K_UP:
            dots.append([self.earth_w[0][0], self.earth_w[0][1]])
            dots.append([self.earth_w[0][0] + c.RECT_WIDTH, self.earth_w[0][1]])
        elif self.earth_w[0][2] == pg.K_DOWN:
            dots.append([self.earth_w[0][0] + c.RECT_WIDTH, self.earth_w[0][1] + c.RECT_HEIGHT])
            dots.append([self.earth_w[0][0], self.earth_w[0][1] + c.RECT_HEIGHT])

        for i, xy in enumerate(dots):
            cnt = 0
            for j, mn in enumerate(self.earth_w):
                if j == 0: continue  # first box<- head
                # 1. xy[1] is rect along
                # 2. xy[0] is small than mn's x
                if xy[1] >= mn[1] and xy[1] <= mn[1] + c.RECT_HEIGHT:
                    if xy[0] >= mn[0] and xy[0] <= mn[0] + c.RECT_WIDTH:
                        return 1
        return 0





