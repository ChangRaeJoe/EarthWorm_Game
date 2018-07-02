import pygame as pg
import constants as c
import item, user
from time import sleep

class Arena:
    def __init__(self):
        pg.init()
        pg.display.set_caption('EarthWorm Game()')
        self.screen = pg.display.set_mode((c.FULL_WIDTH, c.FULL_HEIGHT))
        self.clock = pg.time.Clock()
        self.game_initing()

    def game_initing(self):
        self.init_x = 0
        self.init_y = 0
        self.change_width = 0
        self.change_height = 0

        # 아이템 생성
        self.items = item.item_init()
        # 값들 변경
        self.smile = False
        self.speed = 0
        self.score = 0

    def menu(self):
        pg.draw.line(self.screen, c.RED, (c.WIDTH, 0), (c.WIDTH, c.HEIGHT), 1)

        score_str = "score: " + str(self.score)
        time_str = "time: " + str(int(pg.time.get_ticks() / 1000)) + "s"
        speed_str = "speed: " + str(self.speed)
        score_pos = (c.WIDTH + 10, 10)
        time_pos = (c.WIDTH + 10, 30)
        speed_pos = (c.WIDTH + 10, 50)

        font = pg.font.Font('freesansbold.ttf', 15)
        text = font.render(score_str, True, c.RED)
        text2 = font.render(time_str, True, c.RED)
        text3 = font.render(speed_str, True, c.RED)

        self.screen.blit(text, score_pos)
        self.screen.blit(text2, time_pos)
        self.screen.blit(text3, speed_pos)

    def textObj(self, text, font):
        textSurface = font.render(text, True, c.RED)
        return textSurface, textSurface.get_rect()

    def dispMessage(self, text):
        largeText = pg.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = self.textObj(text, largeText)
        TextRect.center = ((c.WIDTH / 2), (c.HEIGHT / 2))
        self.screen.blit(TextSurf, TextRect)
        pg.display.update()
        sleep(2)
        self.game_initing()



    def time_attack(self):
        min = 60
        tick = pg.time.get_ticks()
        # +1 2 3 4 6 8 10 13
        # item add <- speed up !!
        if tick / 1000 < min:
            self.speed = 0
        elif tick / 1000 < min * 1.2:
            self.speed = 1
        elif tick / 1000 < min * 1.5:
            self.speed = 2
        elif tick / 1000 < min * 1.7:
            self.speed = 3
        elif tick / 1000 < min * 1.8:
            self.speed = 4
        elif tick / 1000 < min * 2:
            self.speed = 6
        elif tick / 1000 < min * 2.2:
            self.speed = 8
        else:
            self.speed = 10

    def get_screen(self):
        return self.screen
    def get_item(self):
        return self.items
    def get_score(self):
        return self.score
    def set_score(self, score):
        self.score = score
    def set_FPS(self, fps):
        self.clock.tick(c.SCREEN_FPS)
    def get_speed(self):
        return self.speed

if __name__ == '__main__':
    arena = Arena()
    screen = arena.get_screen()
    tmp_keys = [pg.K_RIGHT, pg.K_LEFT, pg.K_UP, pg.K_DOWN]
    tmp_keys2 = [pg.K_d, pg.K_a, pg.K_w, pg.K_s]
    # 2 player
    player = []
    player.append(user.User(tmp_keys, arena.get_item()))
    player.append(user.User(tmp_keys2, arena.get_item()))

    while not arena.smile:
        items = arena.get_item()
        player[0].set_item(items)
        player[1].set_item(items)
        ##요기에 1p만 되는 이유가???
        # Press Keyboard
        for event in pg.event.get():
            for i in range(0, len(player)):
                earth_w = player[i].get_earwh_w()
                tmp_key = player[i].get_key()
                if event.type == pg.QUIT:
                    arena.smile = True
                if event.type == pg.KEYDOWN:
                    if event.key == tmp_key[0]:
                        earth_w[0][2] = tmp_key[0]
                    elif event.key == tmp_key[1]:
                        earth_w[0][2] = tmp_key[1]
                    elif event.key == tmp_key[2]:
                        earth_w[0][2] = tmp_key[2]
                    elif event.key == tmp_key[3]:
                        earth_w[0][2] = tmp_key[3]

        # Moving: pre value->next value
        for i in range(0, len(player)):
            player[i].Moving(arena.get_speed())
        for i in range(0, len(player)):
            # Eating item
            tmp_score = arena.get_score() + 10 * player[i].eat()
            arena.set_score(tmp_score)
            # crashed
            if player[i].crash():
                arena.dispMessage('Crasheed!!')

        #time attack - speed
        arena.time_attack()
        #Drawing screen, items, eartwh_worm
        screen.fill(0)
        arena.menu()
        for index, xy in enumerate(items):
            pg.draw.rect(screen, c.BLUE, (xy[0], xy[1], c.RECT_WIDTH, c.RECT_HEIGHT))

        for i in range(0, len(player)):
            earth_w = player[i].get_earwh_w()
            for index, xy in enumerate(earth_w):
                if index % 2 == 0:
                    pg.draw.rect(screen, c.GREEN, (earth_w[index][0], earth_w[index][1], c.RECT_WIDTH, c.RECT_HEIGHT))
                else:
                    pg.draw.rect(screen, c.RED, (earth_w[index][0], earth_w[index][1], c.RECT_WIDTH, c.RECT_HEIGHT))

        pg.display.flip()
        arena.set_FPS(c.SCREEN_FPS)
        if arena.smile==True:
            pg.quit()