import pygame
import os 
import sys
from pygame.locals import *
from wallcon import *

pygame.init()

screen = pygame.display.set_mode(WINS)
pygame.display.set_caption('Bouncing Rectangle')

clock = pygame.time.Clock()

rect_x = 50
rect_y = 50

rect_dx = 20
rect_dy = 20

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True

    rect_x += rect_dx
    rect_y += rect_dy

    if rect_y > WINH - 50 or rect_y < 0:
        rect_dy *= -1
    if rect_x > WINW - 50 or rect_y < 0:
        rect_dx *= -1

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    pygame.draw.rect(screen, RED  , [rect_x + 10, rect_y + 10, 30, 30])

    clock.tick(FPS)

    pygame.display.update()

pygame.quit()
