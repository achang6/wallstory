import pygame
import os
import sys
import random
import math
from pygame.locals import *
from wallcon import *

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(Block, self).__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

        self.center_x = 0
        self.center_y = 0

        self.angle = 0
        self.radius = 0

        self.speed = 0.05

    def update(self):
        self.rect.x = self.radius * math.sin(self.angle) + self.center_x
        self.rect.y = self.radius * math.cos(self.angle) + self.center_y 

        self.angle += self.speed
class Player(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(Player, self).__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]

pygame.init()

screen = pygame.display.set_mode(WINS)
pygame.display.set_caption('moving in circles')

block_list = pygame.sprite.Group()
sprite_list = pygame.sprite.Group()

for i in range(50):
    block = Block(BLACK, 20, 15)
    
    block.center_x = random.randrange(WINW)
    block.center_y = random.randrange(WINH)

    block.radius = random.randrange(10, 200)
    block.angle = random.random() * 2 * math.pi
    block.speed = 0.008
    
    block_list.add(block)
    sprite_list.add(block)

    player = Player(RED, 40,40)
    sprite_list.add(player)

clock = pygame.time.Clock()

score = 0

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True

    sprite_list.update()

    screen.fill(WHITE)

    blocks_hit_list = pygame.sprite.spritecollide(player, block_list, True)

    for block in blocks_hit_list:
        score += 1
        print(score)

    sprite_list.draw(screen)

    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()
