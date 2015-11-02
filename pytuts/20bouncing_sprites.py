import pygame
import os
import sys
import random
from pygame.locals import *
from wallcon import *

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(Block, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

        self.left_boundary = 0
        self.right_boundary = 0
        self.top_boundary = 0
        self.bottom_boundary = 0

        self.dx = 0
        self.dy = 0

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.right >= self.right_boundary or self.rect.left <= self.left_boundary:
            self.dx *= -1
        if self.rect.bottom >= self.bottom_boundary or self.rect.top <= self.top_boundary:
            self.dy *= -1

class Player(Block):
    def update(self):
        pos = pygame.mouse.get_pos()

        self.rect.x = pos[0]
        self.rect.y = pos[1]

pygame.init()

screen = pygame.display.set_mode(WINS)
pygame.display.set_caption('bouncing sprites')

block_list = pygame.sprite.Group()
sprites_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK, 20, 15)

    block.rect.x = random.randrange(WINW)
    block.rect.y = random.randrange(WINH)

    block.dy = random.randrange(-3,4)
    block.dx = random.randrange(-3,4)
    block.left_boundary = 0
    block.top_boundary = 0
    block.right_boundary = WINW
    block.bottom_boundary = WINH

    block_list.add(block)
    sprites_list.add(block)

player = Player(RED, 50, 50)
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

    blocks_hit_list = pygame.sprite.spritecollide(player,block_list,True)

    for block in blocks_hit_list:
        score += 1
        print(score)

    sprites_list.draw(screen)

    clock.tick(FPS)

    pygame.display.update()

pygame.quit()
