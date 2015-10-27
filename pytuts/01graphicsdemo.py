import pygame
import os 
import sys
from pygame.locals import *
from wallcon import *

# set up screen
screen = pygame.display.set_mode(WINS)
# set up clock
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

    # refresh screen
    screen.fill(WHITE)

    # action
    # draw.line(surface, color, point a, point b, width
    pygame.draw.line(screen, GREEN, [0,0], [50,30], 5)
    pygame.draw.lines(screen, BLACK, False, [[0,80], [50,90], [200,80], [220,30]], 5)
    pygame.draw.aaline(screen, GREEN, [0,50], [50,80], True)
    pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])
    pygame.draw.rect(screen, BLACK, [75,10,50,20], 2)
    pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2)
    pygame.draw.ellipse(screen, RED, [300, 10, 50, 20])
    pygame.draw.polygon(screen, BLACK, [[100,100], [0,200], [200,200]], 5)
    pygame.draw.arc(screen, BLACK, [210,75,150,125], 0, PI/2, 2)
    pygame.draw.arc(screen, GREEN, [210,75,150,125], PI/2, PI, 2)
    pygame.draw.arc(screen, BLUE , [210,75,150,125], PI, PI*3/2, 2)
    pygame.draw.arc(screen, RED  , [210,75,150,125], 3*PI/2, 2*PI, 2)
    pygame.draw.circle(screen, BLUE, [60,250],40)

    # update screen
    pygame.display.update()

    # limit loops per second
    clock.tick(FPS)

# exit pygame
pygame.quit()
