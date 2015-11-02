import pygame
import random
from pygame.locals import * 
from wallcon import *

class Block(pygame.sprite.Sprite):

    # non graphic backup
    '''
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load('image.png').convert()

        self.image.set_colorkey(BGC)

        self.rect = self.image.get_rect()
    '''

    # graphic init
    def __init__(self, filename):
        super(Block, self).__init__()

        self.image = pygame.image.load(filename).convert()

        self.image.set_colorkey(BGC)

        self.rect = self.image.get_rect()

pygame.init()

screen = pygame.display.set_mode(WINS)

block_list = pygame.sprite.Group()
sprite_list = pygame.sprite.Group()

for i in range(50):
    block = Block('pyimages/Plain_Block.png')

    block.rect.x = random.randrange(WINW)
    block.rect.y = random.randrange(WINH)

    block_list.add(block)
    sprite_list.add(block)

player = Block('pyimages/princess.png')
sprite.ist.add(player)

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


