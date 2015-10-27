import pygame
import os
import sys
import random
from pygame.locals import *
from wallcon import *

pygame.init()

screen = pygame.display.set_mode(WINS)
pygame.display.set_caption('Snow Animation')

snow_list = []

for i in range(50):
    x = random.randrange(0,WINW)
    y = random.randrange(0,WINH)
    snow_list.append([x,y])

clock = pygame.time.Clock()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key ==  K_ESCAPE:
                done = True

    screen.fill(BLACK)

    for i in range(len(snow_list)):

        pygame.draw.circle(screen, WHITE, snow_list[i], 2)

        snow_list[i][1] += 1

        if snow_list[i][1] > WINH:
            y = random.randrange(-50,-10)
            snow_list[i][1] = y
            x = random.randrange(0, WINW)
            snow_list[i][0] = x

    pygame.display.update()
    
    clock.tick(FPS-40)

pygame.quit()
