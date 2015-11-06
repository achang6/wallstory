import pygame
from filereader import readmapsfile
from pygame.sprite import spritecollide
from pygame.locals import *
from wallcon import * 
from platform import Platform



#### set-up zone ################################################
# initiate pygame
pygame.init()

# initiate pygame window
screen = pygame.display.set_mode(WINS)
pygame.display.set_caption('Wallstory')

# set up clock
clock = pygame.time.Clock()

# read levels data from text
levels = readmapsfile('wallspec.txt')

# Loop variables:
loading = True          # for function that loads level 
levelindex = 0          # index to track current level

# sprite groups
sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()



#### function zone ############################################
def spritesassemble(clevel):
    for p in range(len(clevel)):
        platform = Platform(clevel[p])
        wall_list.add(platform)
        sprite_list.add(platform)
        print(str(clevel[p]))



#### main-loop zone ############################################
while not done:
    
    # main loop set up #
    if loading:
        spritesassemble(levels[levelindex])
        loading = False

    #### event handling loop ##################################
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                done = True
    
    # last words #
    sprite_list.update()

    screen.fill(BGC)

    sprite_list.draw(screen)

    pygame.display.update()

    clock.tick(FPS)

pygame.quit()
