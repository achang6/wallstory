import pygame
import os
import sys
from pygame.locals import *
from wallcon import *

pygame.init()

screen = pygame.display.set_mode(WINS)

pygame.display.set_caption('board games')

clock = pygame.time.Clock()

# click_sound = pygame.mixer.sound('soundfile.wav')

background_position = [0,0]

background_image = pygame.image.load('pyimages/Plain_Block.png').convert()
player_image = pygame.image.load('pyimages/princess.png').convert()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True
        # if event.type == pygame.MOUSEBUTTONDOWN:
            # click_sound.play()

    screen.blit(background_image, background_position)

    player_pos = pygame.mouse.get_pos()
    x = player_pos[0]
    y = player_pos[1]

    screen.blit(player_image, [x,y])

    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()

