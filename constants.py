import pygame as pg

RED = (255,0,0)
BLUE = (0,0,255)
GREEN= (0,255,0)


SCREEN_FPS = 50

#user사각형 기본 가로위치, 세로위치, 너비,높이
RECT_X = 0
RECT_Y = 0
RECT_WIDTH = 15 #100
RECT_HEIGHT = 15
#speed 초기값= [2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 24, 25, 30, 40, 50, 60, 75, 100, 120, 150, 200, 300]
# speed>15 than RECT_WIDTH=15...
SPEED =15

#SCRENN SIZE
WIDTH = 600 + RECT_WIDTH
HEIGHT = 600 + RECT_HEIGHT