import pygame
import os
import sys
import math
from pygame.locals import *
from wallcon import *

pygame.init()

screen = pygame.display.set_mode(WINS)

my_clock = pygame.time.Clock()

angle = 0

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True

    screen.fill(WHITE)

    box_dim = [20,20,250,250]

    pygame.draw.ellipse(screen, GREEN, box_dim, 2)

    pygame.draw.rect(screen, BLACK, box_dim, 2)

    y = 125 * math.sin(angle) + 145
    x = 125 * math.cos(angle) + 145

    pygame.draw.line(screen, GREEN, [145,145], [x,y], 2)

    angle += 0.03

    if angle > 2 * PI:
        angle -= 2 * PI

    pygame.display.update()

    my_clock.tick(FPS)

pygame.quit()
