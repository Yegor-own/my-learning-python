import pygame as pg

pg.init()
win = pg.display.set_mode((500, 500))

pg.display.set_caption("Cubes Game")

width = 10
height = 10
speed = 5

run = True
while run:
    # pg.time.delay(100)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    pg.draw.rect(win, (0, 100, 100), (50, 50, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (50, 60, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (50, 70, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (50, 80, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (50, 90, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (60, 70, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (70, 70, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (80, 70, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (90, 70, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (90, 50, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (90, 60, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (90, 70, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (90, 80, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (90, 90, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (110, 50, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (110, 60, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (110, 70, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (110, 80, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (110, 90, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (110, 90, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (120, 90, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (130, 90, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (140, 90, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (150, 90, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (120, 50, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (130, 50, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (140, 50, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (150, 50, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (120, 70, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (130, 70, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (140, 70, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (150, 70, width, height))
    pg.time.delay(100)
    pg.display.update()

    pg.draw.rect(win, (0, 100, 100), (170, 50, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (170, 60, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (170, 70, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (170, 80, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (170, 90, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (180, 90, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (190, 90, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (200, 90, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (210, 90, width, height))
    pg.time.delay(100)
    pg.display.update()

    pg.draw.rect(win, (0, 100, 100), (230, 50, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (230, 60, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (230, 70, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (230, 80, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (230, 90, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (240, 90, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (250, 90, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (260, 90, width, height))
    pg.time.delay(100)
    pg.display.update()
    pg.draw.rect(win, (0, 100, 100), (270, 90, width, height))
    pg.time.delay(100)
    pg.display.update()

pg.quit()