import pygame
import os
import sys
from pygame.locals import *
from wallcon import *

pygame.init()

screen = pygame.display.set_mode(WINS)
pygame.display.set_caption('rotate text')

clock = pygame.time.Clock()

text_rotate_degrees = 0

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True

    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK, [100,50], [200,50])
    pygame.draw.line(screen, BLACK, [100,50], [100,150])

    font = pygame.font.SysFont('Calibri', 25, True, False)

    text = font.render('Sideways text', True, BLACK)
    text = pygame.transform.rotate(text, 90)
    screen.blit(text, [0,0])

    text = font.render('Upside down text', True, BLACK)
    text = pygame.transform.rotate(text, 180)
    screen.blit(text, [30,0])

    text = font.render('Flipped text', True, BLACK)
    text = pygame.transform.flip(text, False, True)
    screen.blit(text,[30,20])

    text = font.render('Rotating text', True, BLACK)
    text = pygame.transform.rotate(text, text_rotate_degrees)
    text_rotate_degrees += 1
    screen.blit(text, [100,50])

    pygame.display.update()
    
    clock.tick(60)

pygame.quit()
