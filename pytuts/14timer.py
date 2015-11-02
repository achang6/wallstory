import pygame
import sys
import os
from pygame.locals import *
from wallcon import *

pygame.init()

screen = pygame.display.set_mode(WINS)

pygame.display.set_caption('My Game')

clock = pygame.time.Clock()

font = pygame.font.Font(None, 25)

frame_count = 0
start_time = 90

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True

    screen.fill(WHITE)

    total_seconds = frame_count // FPS

    minutes = total_seconds // 60

    seconds = total_seconds % 60

    output_string = '      Time: {0:02}:{1:02}'.format(minutes, seconds)

    text = font.render(output_string, True, BLACK)
    screen.blit(text, [250,250])

    total_seconds = start_time - frame_count // FPS
    if total_seconds < 0:
        total_seconds = 0

    minutes = total_seconds // 60
    
    seconds = total_seconds % 60

    output_string = 'Time left: {0:02}:{1:02}'.format(minutes, seconds)

    text = font.render(output_string, True, BLACK)

    screen.blit(text,[250,350])

    frame_count += 1

    clock.tick(FPS)

    pygame.display.update()

pygame.quit()
