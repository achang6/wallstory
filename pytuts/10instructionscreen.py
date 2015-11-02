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

    for event in pygame.event.get():
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
        text = font.render('This program bounces a rectangle', True, WHITE)
        screen.blit(text, [10,10])

        text = font.render('Page 2', True, WHITE)
        screen.blit(text, [10,40])

    clock.tick(FPS)

    pygame.display.update()


while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True

    screen.fill(BLACK)

    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])

    rect_x += rect_dx
    rect_y += rect_dy
    if rect_y > WINH or rect_y < 0:
        rect_dy *= -1
    if rect_x > WINW or rect_x < 0:
        rect_dx *= -1

    clock.tick(FPS)

    pygame.display.update()

pygame.quit()
