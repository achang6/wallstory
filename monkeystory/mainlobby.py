import pygame
from player import User
from filereader import readmapsfile
from filereader import readplayerfile
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
playpos = readplayerfile('startpos.txt')
print(playpos)

# Loop variables:
loading = True          # for function that loads level 
levelindex = 0          # index to track current level

# sprite groups
sprite_list = pygame.sprite.Group()
wall_list = pygame.sprite.Group()



#### function zone ############################################
def spritesassemble(levelnow):
    for p in range(len(levelnow)):
        platform = Platform(levelnow[p])
        wall_list.add(platform)
        sprite_list.add(platform)
        print(str(levelnow[p]))

def playeradvance(levelnow):
    ball = pygame.image.load('wimages/ball.png')
    print(levelnow)
    player_x = levelnow[0]
    player_y = levelnow[1]
    player = User(ball, player_x, player_y)
    player.walls = wall_list
    sprite_list.add(player)



#### main-loop zone ############################################
while not done:
    
    # main loop set up #
    if loading:
        spritesassemble(levels[levelindex])     
        playeradvance(playpos[levelindex])
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
