import pygame
import os
import sys
from pygame.locals import *
from wallcon import *

pygame.init()

screen = pygame.display.set_mode(WINS)
pygame.display.set_caption('Instruction Screen')

clock = pygame.time.Clock()

rect_x = 50
rect_y = 50

rect_dx = 5
rect_dy = 5

font = pygame.font.Font(None, 36)

display_instructions = True
instruction_page = 1

while not done and display_instructions:

    for even in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            instruction_page += 1
            if instruction_page == 3:
                display_instructions = False

    screen.fill(BLACK)

    if instruction_page == 1:
        text = font.render('Instructions', True, WHITE)
        screen.blit(text, [10,10])
        
        text = font.render('Page 1', True, WHITE)
        screen.blit(text, [10,40])

    if instruction_page == 2:
        text = font.render['This program bounces a triangle', True, WHITE)
        screen.blit
