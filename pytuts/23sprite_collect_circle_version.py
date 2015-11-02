import pygame
import random
from pygame.locals import *
from wallcon import *

class Block(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        super(Block, self).__init__()

        self.image = pygame.Surface([width, height])
        
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        
        pygame.draw.ellipse(self.image, color, [0,0,width,height])

        self.rect = self.image.get_rect()

pygame.init()

screen = pygame.display.set_mode(WINS)

block_list = pygame.sprite.Group()
sprite_list = pygame.sprite.Group()

for i in range(50):
    
    block = Block(BLACK, 20, 15)

    block.rect.x = random.randrange(WINW)
    block.rect.y = random.randrange(WINH)

    block_list.add(block)
    sprite_list.add(block)

player = Block(RED, 20, 15)
sprite_list.add(player)

done = False

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

    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    blocks_hit_list =  pygame.sprite.spritecollide(player, block_list, True)

    for block in blocks_hit_list:
        score += 1
        print(score)

    sprite_list.draw(screen)

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
