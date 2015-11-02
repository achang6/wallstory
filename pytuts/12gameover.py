import pygame
import sys
import os
from pygame.locals import *
from wallcon import *

pygame.init()

screen = pygame.display.set_mode(WINS)

pygame.display.set_caption('Game Over Example')

clock = pygame.time.Clock()

rect_x = 50
rect_y = 50

rect_dx = 5
rect_dy = 5

font = pygame.font.Font(None, 36)

game_over = False

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            game_over = True

    if not game_over:
        rect_x += rect_dx
        rect_y += rect_dy
        
        if rect_y > WINH - 50 or rect_y < 0:
            rect_dy *= -1
        if rect_x > WINW - 50 or rect_y < 0:
            rect_dx *= -1

    screen.fill(BLACK)

    pygame.draw.rect(screen, GREEN, [rect_x, rect_y, 50,50])

    if game_over:
        text = font.render('Game Over', True, WHITE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])

    else:
        text = font.render('Click to end game', True, WHITE)
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])

    clock.tick(60)

    pygame.display.update()

pygame.quit()
