import pygame
import random
from pygame.locals import *
from wallcon import *

class Block(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super(Block, self).__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        self.rect = self.image.get_rect()

pygame.init()

screen = pygame.display.set_mode(WINS)

block_list = pygame.sprite.Group()
sprite_list = pygame.sprite.Group()

for i in range(10):
    block = Block(BLACK, 20, 15)

    block.rect.x = random.randrange(WINW)
    block.rect.y = random.randrange(WINH)

    block_list.add(block)
    sprite_list.add(block)

player = Block(RED, 20, 15)
sprite_list.add(player)

clock = pygame.time.Clock()

font = pygame.font.Font(None, 36)

score = 0
level = 1

while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True

    pos = pygame.mouse.get_pos()

    player.rect.x = pos[0]
    player.rect.y = pos[1]

    blocks_hit_list = pygame.sprite.spritecollide(player,block_list, True)

    for block in blocks_hit_list:
        score += 1
        print(score)

    if len(block_list) == 0:
        level += 1
        
        for i in range (level * 10):
            block = Block(BLACK, 20, 15)

            block.rect.x = random.randrange(WINW)
            block.rect.y = random.randrange(WINH)

            block_list.add(block)
            sprite_list.add(block)

    screen.fill(WHITE)

    sprite_list.draw(screen)

    text = font.render('Score: ' + str(score), True, BLACK)
    screen.blit(text, [10, 10])

    text = font.render('Level: ' + str(level), True, BLACK)
    screen.blit(text, [10, 40])

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
