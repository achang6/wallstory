import pygame
import sys
import os
from pygame.locals import *
from wallcon import *


def draw_stick_figure(screen, x, y):
    # head
    pygame.draw.ellipse(screen, BLACK, [1+x, y, 10,10], 0)
    # legs
    pygame.draw.line(screen, BLACK, [5+x, 17+y], [10+x, 27+y], 2)
    pygame.draw.line(screen, BLACK, [5+x, 17+y], [x, 27+y], 2)
    # body
    pygame.draw.line(screen, RED, [5+x, 17+y], [5+x, 7+y], 2)
    # arms
    pygame.draw.line(screen, RED, [5+x, 7+y], [9+x, 17+y], 2)
    pygame.draw.line(screen, RED, [5+x, 7+y], [1+x, 17+y], 2)


pygame.init()

screen = pygame.display.set_mode(WINS)
pygame.display.set_caption('My Game')

clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True

    pos  = pygame.mouse.get_pos()
    x = pos[0]
    y = pos[1]

    screen.fill(WHITE)
    draw_stick_figure(screen, x, y)

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
