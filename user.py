import pygame as pg
import item, main
import constants as c
import random
class User:
    def __init__(self,  keys, items):
        # 지렁이 생성[x, y, direction]
        self.earth_w_init()
        self.items = items
        self. keys = keys
        self.score = 0

    def earth_w_init(self):
        self.earth_w = []
        self.score = 0
        for i in range(0, 3):
            self.earth_w.append([c.RECT_X, c.RECT_Y, 0])

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
        if self.earth_w[0][2] == self.keys[0]:
            dots.append([self.earth_w[0][0] + c.RECT_WIDTH, self.earth_w[0][1]])
            dots.append([self.earth_w[0][0] + c.RECT_WIDTH, self.earth_w[0][1] + c.RECT_HEIGHT])
        elif self.earth_w[0][2] == self.keys[1]:
            dots.append([self.earth_w[0][0], self.earth_w[0][1]])
            dots.append([self.earth_w[0][0], self.earth_w[0][1] + c.RECT_HEIGHT])
        elif self.earth_w[0][2] == self.keys[2]:
            dots.append([self.earth_w[0][0], self.earth_w[0][1]])
            dots.append([self.earth_w[0][0] + c.RECT_WIDTH, self.earth_w[0][1]])
        elif self.earth_w[0][2] == self.keys[3]:
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
                        self.earth_w_init()
                        return 1
        return 0

    def Moving(self, speed):
        self.speed = speed
        earth_w = self.get_earwh_w()
        for index, xy in enumerate(earth_w):
            next = index + 1
            if index == 0:
                cur_x, cur_y = earth_w[index][0], earth_w[index][1]
                pre_x = earth_w[next][0]
                pre_y = earth_w[next][1]
                earth_w[next][0], earth_w[next][1] = cur_x, cur_y
                earth_w[index][0], earth_w[index][1] = self.auto_moved(xy)
                earth_w[index][0], earth_w[index][1], earth_w[index][2] = self.limit(xy)
            elif index < len(earth_w) - 1:
                cur_x, cur_y = pre_x, pre_y
                pre_x = earth_w[next][0]
                pre_y = earth_w[next][1]
                earth_w[next][0], earth_w[next][1] = cur_x, cur_y

    def edged(self):
        dir_choice = random.choice(self.keys)
        return dir_choice

    def limit(self, xy):
        x = xy[0]
        y = xy[1]
        tmp_key = xy[2]
        if c.WIDTH - c.RECT_WIDTH < x:  # 막는 동시에 방향을 바꿔준다.
            x -= c.SPEED + self.speed
            tmp_key = self.edged()
        elif 0 > x:
            x = 0
            tmp_key = self.edged()

        if c.HEIGHT - c.RECT_HEIGHT < y:
            y -= c.SPEED + self.speed
            tmp_key = self.edged()
        elif 0 > y:
            y = 0
            tmp_key = self.edged()

        return (x, y, tmp_key)

    def auto_moved(self, box_one):
        x = box_one[0]
        y = box_one[1]
        key = box_one[2]

        if key == self.keys[0]:
            x += c.SPEED + self.speed
        elif key == self.keys[1]:
            x -= c.SPEED + self.speed
        elif key == self.keys[2]:
            y -= c.SPEED + self.speed
        elif key == self.keys[3]:
            y += c.SPEED + self.speed
        return (x, y)

    def get_earwh_w(self):
        return self.earth_w
    def get_key(self):
        return self.keys
    def set_item(self, item):
        self.items = item
    def get_score(self):
        return self.score
    def set_score(self, score):
        self.score = score



