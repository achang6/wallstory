import pygame
import os
import sys
from pygame.locals import *
from wallcon import *

def recursive_draw(x,y,width,height):
    pygame.draw.rect(screen, BLACK, [x,y,width,height], 1)

    if (width > 14):
        x += width * 0.02
        y += height * 0.02
        width *= .96
        height *= .96
        recursive_draw(x,y,width,height)
        # recursive since it calls on itself within itself

pygame.init()

screen = pygame.display.set_mode(WINS)

pygame.display.set_caption('My Game')

clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True

    screen.fill(WHITE)

    recursive_draw(0,0,WINW,WINH)

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
