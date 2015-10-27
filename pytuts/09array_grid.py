import pygame
import sys
import os
from pygame.locals import *
from wallcon import *

gridw = 20
gridh = 20

margin = 5

grid = []
for row in range(10):
    grid.append([])
    for column in range(10):
        grid[row].append(0)

grid[1][5] = 1

pygame.init()

screen = pygame.display.set_mode((255,255))
pygame.display.set_caption('Array Backed Grid')

clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (gridw + margin)
            row = pos[1] // (gridh + margin)
            grid[row][column] = 1
            print('Click', pos, 'grid coordinates: ', row, column)

    screen.fill(BLACK)

    for row in range(10):
        for column in range(10):
            color = WHITE
            if grid[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen,
                    color,
                    [(margin + gridw) * column + margin,
                        (margin + gridh) * row + margin,
                        gridw,
                        gridh,])

    clock.tick(FPS)

    pygame.display.update()

pygame.quit()
