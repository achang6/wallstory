import pygame
import os
import sys
import random
from pygame.locals import *
from wallcon import *

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(Block,self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

class Player(Block):
    carry_block_list = []

    def update(self):
        pos = pygame.mouse.get_pos()

        x_diff = self.rect.x - pos[0]
        y_diff = self.rect.y - pos[1]

        for block in self.carry_block_list:
            block.rect.x -= x_diff
            block.rect.y -= y_diff

        self.rect.x = pos[0]
        self.rect.y = pos[1]

pygame.init()

screen = pygame.display.set_mode(WINS)
pygame.display.set_caption('Pick up example')

block_list = pygame.sprite.Group()
sprite_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK, 20, 15)

    block.rect.x = random.randrange(WINW)
    block.rect.y = random.randrange(WINH)

    block_list.add(block)
    sprite_list.add(block)

player = Player(RED, 20, 15)
sprite_list.add(player)

clock = pygame.time.Clock()

pygame.mouse.set_visible(False)

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            blocks_hit_list = pygame.sprite.spritecollide(player,block_list, False)
            player.carry_block_list = blocks_hit_list

        elif event.type == pygame.MOUSEBUTTONUP:
            player.carry_block_list = []

    sprite_list.update()
    
    screen.fill(WHITE)

    sprite_list.draw(screen)

    clock.tick(FPS)

    pygame.display.update()

pygame.quit()
