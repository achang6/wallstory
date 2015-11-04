import pygame
from filereader import readmapsfile
from pygame.sprite import spritecollide
from pygame.locals import *
from wallcom import * 


#### set-up zone ################################################

# initiate pygame
pygame.init()

# initiate pygame window
screen = pygame.display.set_mode(WINS)
pygame.display.set_caption('Wallstory')

# set up clock
clock = pygame.time.Clock()

# read levels data from text
levels = readmapsfile('wallspec.txt')

# 



#### main-loop zone ############################################

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True

    screen.fill(WHITE)

    clock.tick(FPS)

    pygame.display.update()

pygame.quit()
