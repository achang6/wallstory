import pygame
import os
import sys
from pygame.locals import *
from wallcon import *


def draw_snowman(screen, x, y):
    pygame.draw.ellipse(screen, WHITE, [35+x, 0+y, 25, 25])
    pygame.draw.ellipse(screen, WHITE, [23+x, 20+y, 50, 50])
    pygame.draw.ellipse(screen, WHITE, [0+x, 65+y, 100, 100])


pygame.init()

screen = pygame.display.set_mode(WINS)

clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True

    screen.fill(BLACK)

    draw_snowman(screen, 10, 10)
    draw_snowman(screen, 300, 10)
    draw_snowman(screen, 10, 300)

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
