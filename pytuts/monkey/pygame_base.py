import pygame
import os
import sys

# define colors
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

# set fps
fps = 60

pygame.init()

# set width and height of screen
WINW = 800
WINH = 600
win_size = (WINW,WINH)

screen = pygame.display.set_mode(win_size)
pygame.display.set_caption('My Game')

# loop until user exits
done = False

# manage frame refresh rate
clock = pygame.time.Clock()

# main loop
while not done:
    # event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True
    
    # game logic region ###############

    # drawing code region #############
    # 1. refresh screen
    screen.fill(WHITE)

    # update screen
    pygame.display.update()

    # limit frame rate
    clock.tick(fps)

pygame.quit()
