import pygame
import sys
import os
import random
from pygame.locals import * 
from wallcon import *

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(Block, self).__init__()
        
        self.image = pygame.Surface([width,height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

    def reset_pos(self):
        self.rect.y = random.randrange(-300,-20)
        self.rect.x = random.randrange(0, WINW)

    def update(self):
        self.rect.y += 1

        if self.rect.y > WINH:
            self.reset_pos()

class Player(Block):
    def update(self):
        pos = pygame.mouse.get_pos()

        self.rect.x = pos[0]
        self.rect.y = pos[1]

pygame.init()

screen = pygame.display.set_mode(WINS)
pygame.display.set_caption('Sprites example')

block_list = pygame.sprite.Group()
sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK, 20, 15)

    block.rect.x = random.randrange(WINW)
    block.rect.y = random.randrange(WINH)

    block_list.add(block)
    sprites_list.add(block)

player = Player(RED, 20,15)
sprites_list.add(player)

clock = pygame.time.Clock()

score = 0

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True

    screen.fill(WHITE)

    sprites_list.update()

    block_hit_list = pygame.sprite.spritecollide(player, block_list, False)

    for block in block_hit_list:
        score += 1
        print(score)
        
        block.reset_pos()

    sprites_list.draw(screen)

    clock.tick(FPS)

    pygame.display.update()

pygame.quit()
