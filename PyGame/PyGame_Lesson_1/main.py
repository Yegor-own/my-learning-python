import pygame as pg
import sys

sc = pg.display.set_mode((500, 500))
# figure drawing
pg.draw.line(sc, (15, 150, 25), [10, 210], [10, 260], 5)
pg.draw.line(sc, (15, 150, 25), [10, 260], [200, 260], 5)
pg.draw.line(sc, (15, 150, 25), [200, 260], [200, 300], 5)
pg.draw.rect(sc, (62, 107, 129), (10, 150, 60, 60))
i = 25
j = 150
k = 75
x = 150
y = 10
while True:
    pg.draw.rect(sc, (i % 255, j % 255, k % 255), (10, 10, 60, 60))
    pg.draw.rect(sc, ((i + 50) % 255, (j + 50) % 255, (k + 50) % 255), (10, 80, 60, 60))
    pg.draw.rect(sc, (148, 126, 36), (x, y, 60, 60))
    pg.display.update()
    i += 10
    j += 10
    k += 10
    if x != 300:
        x += 2
    for f in pg.event.get():
        if f.type == pg.QUIT:
            sys.exit()
        pg.time.delay(1000)