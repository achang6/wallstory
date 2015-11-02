import pygame
import sys
import os
from pygame.locals import *
from wallcon import *

pygame.init()

screen = pygame.display.set_mode(WINS)

pygame.display.set_caption('My Game')

clock = pygame.time.Clock()

# http://freemusicarchive.org/music/MIT_Concert_Choir/Carmina_Burana_Carl_Orff/01_1355
# pygame.mixer.music.load('MIT_Concert_Choir_0_Fortuna.ogg')
# pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
# pygame.music.play()

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True
        # elif event.type == pygame.constants.USEREVENT:
            # http://freemusicarchive.org/music/Saito_Koji/Again/01-Alone
            # pygame.mixer.music.load('Saito_Koji_-_01_-_Alone.ogg')

    screen.fill(WHITE)

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
