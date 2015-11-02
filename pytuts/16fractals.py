import pygame
import os
import sys
from pygame.locals import *
from wallcon import *

def recursive_draw(x,y,width,height,count):
    pygame.draw.line(screen,
            BLACK, 
            [x + width * .25, height // 2 + y],
            [x + width * .75, height // 2 + y],
            3)
    pygame.draw.line(screen,
            RED,
            [x + width * .25, (height * 0.5) // 2 + y],
            [x + width * .25, (height * 1.5) // 2 + y],
            3)
    pygame.draw.line(screen,
            WHITE,
            [x + width * .75, (height * 0.5) // 2 + y],
            [x + width * .75, (height * 1.5) // 2 + y],
            3)

    if count > 0:
        count -= 1
        #TL
        recursive_draw(x,y,width // 2, height // 2, count)
        #TR
        recursive_draw(x + width // 2, y, width // 2, height // 2, count)
        #BL
        recursive_draw(x, y + width // 2, width // 2, height // 2, count)
        #BR
        recursive_draw(x + width // 2, y + width // 2, width // 2, height // 2, count)



pygame.init()

screen = pygame.display.set_mode(WINS)

pygame.display.set_caption('My Game')

clock = pygame.time.Clock()

fractal_level = 3

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True
            elif event.key == K_UP:
                if fractal_level < 10:
                    fractal_level += 1
            elif event.key == K_DOWN:
                if fractal_level > 1:
                    fractal_level -= 1

    screen.fill(BLACK)

    recursive_draw(0,0,WINW,WINH,fractal_level)

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
