import pygame
import os
import sys
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
pygame.display.set_caption('Some Game')

clock = pygame.time.Clock()

pygame.mouse.set_visible(0)

dx = 0
dy = 0

x_pos = 10
y_pos = 10

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True
            if event.key == pygame.K_LEFT:
                dx = -3
            elif event.key == K_RIGHT:
                dx = 2
            elif event.key == K_UP:
                dy = -3
            elif event.key == K_DOWN:
                dy = 3
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                dx = 0
            elif event.key == pygame.K_RIGHT:
                dx = 0
            elif event.key == pygame.K_UP:
                dy = 0
            elif event.key == pygame.K_DOWN:
                dy = 0

    x_pos += dx
    y_pos += dy

    screen.fill(WHITE)

    draw_stick_figure(screen, x_pos, y_pos)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
